import asyncio
import json
import logging
import selectors
from inspect import iscoroutinefunction
from socket import AF_INET, SHUT_RDWR, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket
from sys import platform as sys_platform

logger = logging.getLogger("Client")

# Apparently on windows using shutdown on a socket that isn't actually connected throws an error.
# So to be safe I'm just gonna, not use shutdown on windows I guess. There's probably a better way to handle that,
# But it probably also involves touching the win32 API which I'd prefer not to.

class EBF5AsyncSocket:
    def __init__(self, timeouts_seconds: float = 30):
        self.server_sock: None | socket = None

        self.select_task: asyncio.Task | None = None
        self.wait_for_empty_buffers_to_close_client_socket_task: asyncio.Task | None = None
        #self.exit_event: asyncio.Event = asyncio.Event()
        self.client_disconnect_event = asyncio.Event()

        self.client_sock: None | socket = None

        self.message_bytes_to_send = bytearray()
        self.received_message_bytes = bytearray()
        self.incoming_message_final_length: int = 0
        self.is_waiting_for_new_message: bool = True

        self.disconnect_scheduled = False

        self.timeouts_seconds = timeouts_seconds

    async def start(self, host: str, port: int):
        if self.does_server_exist():
            self.disconnect_server()
        if self.does_client_exist():
            logger.info("Disconnecting EBF5...")
            self.schedule_client_disconnect()
            await self.client_disconnect_event.wait()

        self.client_disconnect_event.clear()
        self._clear_buffers()
        # Supporting IPV6 would probably be nice.
        # But it'll probably just be running on localhost or a local network with IPV4 LAN addresses anyway.
        self.server_sock = socket(AF_INET, SOCK_STREAM)

        # maybe FIXME: this should probably(?) be removed when we aren't just debug testing stuff.
        # Maybe I'll remove it for release or if the address isn't localhost or something.
        self.server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        try:
            self.server_sock.bind((host, port))
        except Exception as e:
            #logger.debug("Error trying to bind socket. Did you enter a valid address?\nError: %s", e, exc_info=True)
            logger.error(f"Invalid address. Error: {e}")
            self.server_sock.close()
            self.server_sock = None
            return

        self.server_sock.listen(1)
        self.server_sock.setblocking(False)
        logger.info(f"Started listening for connections from EBF5 on {host}:{port}.")
        if self.select_task is None or (self.select_task is not None and self.select_task.done()):
            self.select_task = asyncio.create_task(self.select_loop(), name="EBF5AP socket select loop")

        if self.timeouts_seconds >= 0:
            self.server_sock.settimeout(self.timeouts_seconds)

        self.selector = selectors.DefaultSelector()
        self.selector.register(self.server_sock, selectors.EVENT_READ, data=self.accept_connection_callback)

        #await self.exit_event.wait()

    def _does_socket_exist(self, socket_) -> bool:
        return isinstance(socket_, socket) and socket_.fileno() != -1

    def does_server_exist(self):
        return self._does_socket_exist(self.server_sock)

    def does_client_exist(self):
        return self._does_socket_exist(self.client_sock)

    def add_utf8_message_to_send_queue(self, utf8_message: str) -> bool:
        """Add a message to the internal message send queue, to be sent later by the select loop.\n
        Note: messages will not be added to the queue if `self.disconnect_scheduled` is `True`!\n
        Messages also will not be added to the queue if the client socket doesn't exist.

        :return: Whether the message was added to the internal message send queue or not.
        """
        if self.disconnect_scheduled or not self.does_client_exist():
            logger.debug(f"**NOT** adding to send queue: {utf8_message}, socket is closing or doesn't exist")
            return False

        logger.debug(f"adding to send queue: {utf8_message}")
        message_bytes = utf8_message.encode("utf-8")
        length_bytes = len(message_bytes).to_bytes(4, "big", signed=False)
        self.message_bytes_to_send += length_bytes
        self.message_bytes_to_send += message_bytes
        return True

    def accept_connection_callback(self, sock: socket, mask):
        if self.does_client_exist():
            logger.info("Something attempted to connect while the previous EBF5 connection is still alive."
                " Current connection will be kept and new connection will be closed.")
            instant_disconnecting_socket, _ = sock.accept()
            if sys_platform != "win32": # I know this would be a uh, rather unlikely race condition, but still.
                instant_disconnecting_socket.shutdown(SHUT_RDWR)
            instant_disconnecting_socket.close()
            return
        self.disconnect_scheduled = False
        self.client_sock, _address = sock.accept()
        logger.info("Accepting connection from EBF5.")
        self.client_sock.setblocking(False)
        self.selector.register(self.client_sock, selectors.EVENT_READ | selectors.EVENT_WRITE,
                                data=self.client_readwrite_callback)

    async def client_readwrite_callback(self, client: socket, mask):
        if mask & selectors.EVENT_READ and self.does_client_exist():
            logger.debug("reading...")

            new_bytes = client.recv((2 ** 16) - 1)
            self.received_message_bytes += new_bytes
            done_reading = False

            if len(new_bytes) == 0:
                logger.info("EBF5 disconnected from the client.")
                self._disconnect_client()

            #log(f"start: {self.received_message_bytes}")
            #log(f"len(new_bytes): {len(new_bytes)}")
            while not done_reading:
                if self.is_waiting_for_new_message:
                    if len(self.received_message_bytes) >= 4:
                        self.incoming_message_final_length = int.from_bytes(self.received_message_bytes[:4], "big",
                                                                                signed=False)
                        self.is_waiting_for_new_message = False
                    #else:
                    #    print("setting done reading")
                    #    done_reading = True

                if not self.is_waiting_for_new_message:
                    if len(self.received_message_bytes) >= self.incoming_message_final_length:
                        message_text = self.received_message_bytes[4:4 + self.incoming_message_final_length].decode("utf-8")
                        self.on_message_received(message_text)

                        self.received_message_bytes = self.received_message_bytes[4 + self.incoming_message_final_length:]
                        self.incoming_message_final_length = 0
                        self.is_waiting_for_new_message = True

                await asyncio.sleep(0)

                # doing it here saves an extra loop.
                if self.is_waiting_for_new_message and len(self.received_message_bytes) < 4:
                    done_reading = True

        elif not self.does_client_exist():
            logger.debug("skipping reading because the client socket apparently doesn't exist.")

        if mask & selectors.EVENT_WRITE and self.does_client_exist():
            if len(self.message_bytes_to_send) > 0:
                logger.debug("writing...")
                logger.debug(f"len(self.message_bytes_to_send): {len(self.message_bytes_to_send)}")
                bytes_sent = client.send(self.message_bytes_to_send)
                self.message_bytes_to_send = self.message_bytes_to_send[bytes_sent:]
                logger.debug(f"bytes_sent: {bytes_sent}, len(self.message_bytes_to_send): {len(self.message_bytes_to_send)}")

        elif not self.does_client_exist():
            logger.debug("skipping writing because the client socket apparently doesn't exist.")

    def on_message_received(self, message: str):
        logger.debug(f"received message: \"{message}\"")
        reply = "message received successfully in a callback called from an asyncio `Task` polling the socket with `select()`!"
        self.add_utf8_message_to_send_queue(json.dumps({"type":"client_to_game_debug_message", "text":reply}))
        self.add_utf8_message_to_send_queue(json.dumps({"type":"client_to_game_debug_message",
                "text":"also unicode test: here's an emdash — mid message, emdash at the end of the message—"}))
        self.add_utf8_message_to_send_queue(json.dumps({"type":"client_to_game_debug_message",
                "text":"more random unicode characters: pi: π, smiley: 😀, pirate flag: 🏴‍☠️, all of them next to each other: π😀🏴‍☠️—"}))
        #self.schedule_client_disconnect()

    def schedule_client_disconnect(self):
        logger.debug("Client disconnect is being scheduled.")
        # Special raw UTF-8 non-JSON message.
        self.add_utf8_message_to_send_queue("client_disconnect_soon")
        self.disconnect_scheduled = True

        self.wait_for_empty_buffers_to_close_client_socket_task = asyncio.create_task(
                self.wait_for_empty_buffers_to_close_client_socket(),
                name="EBF5AP waiting for client socket buffers to empty before closing"
        )

    async def wait_for_empty_buffers_to_close_client_socket(self):
        max_wait_seconds = self.timeouts_seconds
        wait_seconds_per_wait = 1/30 # 1 EBF5 frame
        waited_seconds = 0

        while self.does_client_exist() and (len(self.message_bytes_to_send) > 0 or len(self.received_message_bytes) > 0):
            await asyncio.sleep(wait_seconds_per_wait)
            waited_seconds += wait_seconds_per_wait
            if waited_seconds > max_wait_seconds:
                logger.debug("WARNING: A client socket disconnect was scheduled but the buffers didn't clear after"
                   f" waiting a timeout of {max_wait_seconds}, so we're force closing the socket right now anyway.")
                #log(f"self.message_bytes_to_send: {self.message_bytes_to_send} |"
                #    " self.received_message_bytes: {self.received_message_bytes}")
                logger.debug(f"len(self.message_bytes_to_send): {len(self.message_bytes_to_send)} |"
                    f" len(self.received_message_bytes): {len(self.received_message_bytes)}")
                logger.debug("(there should be nothing to send but there probably is something to read if the game is"
                    "sending too many messages to us)")
                break

        self._disconnect_client()

    def _clear_buffers(self):
        logger.debug("clearing buffers.")
        self.message_bytes_to_send.clear()
        self.received_message_bytes.clear()
        self.incoming_message_final_length = 0
        self.is_waiting_for_new_message = True

    def _disconnect_client(self):
        """Clears the read/write buffers and closes the client socket if it currently exists.

        Use `schedule_client_disconnect()` instead of directly calling `_disconnect_client()` when sending messages.
        """
        self.client_disconnect_event.set()
        self._clear_buffers()
        if self.does_client_exist():
            logger.debug("closing client.")
            self.selector.unregister(self.client_sock)
            if sys_platform != "win32":
                self.client_sock.shutdown(SHUT_RDWR)
            self.client_sock.close()
        else:
            logger.debug("client was already closed.")

    def disconnect_server(self):
        if self.does_server_exist():
            logger.debug("disconnecting server.")
            self.selector.unregister(self.server_sock)
            # oh boy, platform specific socket differences! ughhh...
            # apparently windows is stricter than linux about using shutdown on a socket when it isn't actually connected.
            # so to be safe I'm just gonna not `shutdown()` here at all on windows.
            if sys_platform != "win32":
                self.server_sock.shutdown(SHUT_RDWR)
            self.server_sock.close()
        else:
            logger.debug("_disconnect_server() when server was already closed.")

    def __full_close_immediately(self):
        logger.debug("closing everything...")
        #self.exit_event.set()

        # _disconnect_client() clears the buffers anyway
        # self._clear_buffers()
        self._disconnect_client()
        self.disconnect_server()
        # if self.does_socket_exist(self.server_sock):
        #     self.selector.unregister(self.server_sock)
        #     self.server_sock.shutdown(SHUT_RDWR)
        #     self.server_sock.close()

        if self.select_task is not None:
            self.select_task.cancel()

        if self.wait_for_empty_buffers_to_close_client_socket_task is not None:
            self.wait_for_empty_buffers_to_close_client_socket_task.cancel()

    async def select_loop(self):
        try:
            while True:
                # For some reason on windows this is causing the underlying select.select() call to get OS errored
                # with "[WinError 10022] An invalid argument was supplied", but like, I'd imagine that has to be a bug
                # with the selectors library?
                # The error doesn't seem to break or stop anything.
                # It's only happening when we're closing the sockets and cleaning everything up anyway so I think it's fine.
                # TO REPRODUCE: connect the game and client, use /disconnect_ebf5, then use /connect_ebf5
                events = self.selector.select(timeout=0)
                for selector_key, mask in events:
                    # It doesn't look very clear from this code but this callback comes from the data parameter of
                    # self.selector.register(<whatever>, <whatever>, data=callback_function_in_our_case).
                    # This is a kinda clever design but it's also confusing until you know that's what it is doing.
                    # I don't know why the library was made like this but whatever sure fine I guess.
                    # I'll just do it like this with this comment explaining it because it is admittedly convenient.
                    callback = selector_key.data
                    if callable(callback):
                        if iscoroutinefunction(callback):
                            await callback(selector_key.fileobj, mask)
                        else:
                            callback(selector_key.fileobj, mask)

                await asyncio.sleep(1/30) # 1 EBF5 frame (maybe sleep less than that?)
        except (Exception, asyncio.CancelledError) as e: # Exception does not include asyncio.CancelledError apparently.
            if isinstance(e, asyncio.CancelledError):
                logger.debug("select_loop() received `asyncio.CancelledError`, closing everything...")
            else:
                logger.debug("select_loop() threw an error, closing everything...")

            self.__full_close_immediately()

            logger.debug("re-raising original error.")
            raise e
        finally:
            logger.debug("select_loop() exiting, socket will no longer send/receive if still alive.")

# server_test = EBF5AsyncSocket("localhost", 4999)
# asyncio.run(server_test.start())
