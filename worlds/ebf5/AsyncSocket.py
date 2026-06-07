import asyncio
import json
import selectors
from datetime import datetime
from inspect import iscoroutinefunction
from socket import AF_INET, SHUT_RDWR, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket


def log(message: str):
    now = datetime.now()
    print(f"[{now.isoformat(' ')}] {message}")


class EBF5AsyncSocket:
    def __init__(self, host: str, port: int, timeouts_seconds: float = 30):
        # Supporting IPV6 would probably be nice.
        # But it'll probably just be running on localhost or a local network with IPV4 LAN addresses anyway.
        self.server_sock: socket = socket(AF_INET, SOCK_STREAM)

        # maybe FIXME: this should probably(?) be removed when we aren't just debug testing stuff.
        # Maybe I'll remove it for release or if the address isn't localhost or something.
        self.server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.server_sock.bind((host, port))
        self.server_sock.listen(1) # CHECK THIS
        self.server_sock.setblocking(False)

        self.select_task: asyncio.Task | None = None
        self.other_work_task: asyncio.Task | None = None
        self.wait_for_empty_buffers_to_close_client_socket_task: asyncio.Task | None = None
        self.exit_event: asyncio.Event = asyncio.Event()

        self.selector = selectors.DefaultSelector()
        self.selector.register(self.server_sock, selectors.EVENT_READ, data=self.accept_connection_callback)

        self.client_sock: None | socket = None

        self.message_bytes_to_send = bytearray()
        self.received_message_bytes = bytearray()
        self.incoming_message_final_length: int = 0
        self.is_waiting_for_new_message: bool = True

        self.disconnect_scheduled = False

        self.timeouts_seconds = timeouts_seconds

        if timeouts_seconds >= 0:
            self.server_sock.settimeout(self.timeouts_seconds)

    def does_client_socket_exist(self) -> bool:
        return isinstance(self.client_sock, socket) and self.client_sock.fileno() != -1

    def add_UTF8_message_to_send_queue(self, UTF8_message: str) -> bool:
        """Add a message to the internal message send queue, to be sent later by the select loop.\n
        ## Note: messages will not be added to the queue if `self.disconnect_scheduled` is `True`!\n
        Messages also will not be added to the queue if the client socket doesn't exist.

        :return: Whether the message was added to the internal message send queue or not.
        """
        if self.disconnect_scheduled or not self.does_client_socket_exist():
            log(f"**NOT** adding to send queue: {UTF8_message}, socket is closing or doesn't exist")
            return False

        log(f"adding to send queue: {UTF8_message}")
        message_bytes = UTF8_message.encode("utf-8")
        length_bytes = len(message_bytes).to_bytes(4, "big", signed=False)
        self.message_bytes_to_send += length_bytes
        self.message_bytes_to_send += message_bytes
        return True

    def accept_connection_callback(self, sock: socket, mask):
        if self.does_client_socket_exist():
            log("something attempted to connect while the previous client socket connection is still alive, "
                "(effectively) rejecting...")
            instant_disconnecting_socket, _ = sock.accept()
            instant_disconnecting_socket.shutdown(SHUT_RDWR)
            instant_disconnecting_socket.close()
            return
        self.disconnect_scheduled = False
        self.client_sock, address = sock.accept()
        log(f"accepting connection from {address}")
        self.client_sock.setblocking(False)
        self.selector.register(self.client_sock, selectors.EVENT_READ | selectors.EVENT_WRITE,
                                data=self.client_readwrite_callback)

    async def client_readwrite_callback(self, client: socket, mask):
        if mask & selectors.EVENT_READ and self.does_client_socket_exist():
            log("reading...")

            new_bytes = client.recv((2 ** 16)-1)
            self.received_message_bytes += new_bytes
            done_reading = False

            if len(new_bytes) == 0:
                log("DISCONNECT RECEIVED!")
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

        elif not self.does_client_socket_exist():
            log("skipping reading because the client socket apparently doesn't exist.")

        if mask & selectors.EVENT_WRITE and self.does_client_socket_exist():
            if len(self.message_bytes_to_send) > 0:
                log("writing...")
                log(f"len(self.message_bytes_to_send): {len(self.message_bytes_to_send)}")
                bytes_sent = client.send(self.message_bytes_to_send)
                self.message_bytes_to_send = self.message_bytes_to_send[bytes_sent:]
                log(f"bytes_sent: {bytes_sent}, len(self.message_bytes_to_send): {len(self.message_bytes_to_send)}")

        elif not self.does_client_socket_exist():
            log("skipping writing because the client socket apparently doesn't exist.")

    def on_message_received(self, message: str):
        log(f"received message: \"{message}\"")
        reply = "message received successfully in a callback called from an asyncio `Task` polling the socket with `select()`!"
        self.add_UTF8_message_to_send_queue(json.dumps({"type":"client_to_game_debug_message", "text":reply}))
        self.add_UTF8_message_to_send_queue(json.dumps({"type":"client_to_game_debug_message",
                "text":"also unicode test: here's an emdash — mid message, emdash at the end of the message—"}))
        self.add_UTF8_message_to_send_queue(json.dumps({"type":"client_to_game_debug_message",
                "text":"more random unicode characters: pi: π, smiley: 😀, pirate flag: 🏴‍☠️, all of them next to each other: π😀🏴‍☠️—"}))
        self.schedule_client_disconnect()

    def schedule_client_disconnect(self):
        log("Client disconnect is being scheduled.")
        # Special raw UTF-8 non-JSON message.
        self.add_UTF8_message_to_send_queue("client_disconnect_soon")
        self.disconnect_scheduled = True

        self.wait_for_empty_buffers_to_close_client_socket_task = asyncio.create_task(
                self.wait_for_empty_buffers_to_close_client_socket(),
                name="EBF5AP waiting for client socket buffers to empty before closing"
        )

    async def wait_for_empty_buffers_to_close_client_socket(self):
        max_wait_seconds = self.timeouts_seconds
        wait_seconds_per_wait = 1/30 # 1 EBF5 frame
        waited_seconds = 0

        while self.does_client_socket_exist() and (len(self.message_bytes_to_send) > 0 or len(self.received_message_bytes) > 0):
            await asyncio.sleep(wait_seconds_per_wait)
            waited_seconds += wait_seconds_per_wait
            if waited_seconds > max_wait_seconds:
                log("WARNING: A client socket disconnect was scheduled but the buffers didn't clear after waiting"
                   f"a timeout of {max_wait_seconds}, so we're force closing the socket right now anyway.")
                #log(f"self.message_bytes_to_send: {self.message_bytes_to_send} |"
                #    " self.received_message_bytes: {self.received_message_bytes}")
                log(f"len(self.message_bytes_to_send): {len(self.message_bytes_to_send)} |"
                    " len(self.received_message_bytes): {len(self.received_message_bytes)}")
                log("(there should be nothing to send but there probably is something to read if the game is sending"
                    "too many messages to us)")
                break

        self._disconnect_client()

    def _clear_buffers(self):
        log("clearing buffers.")
        self.message_bytes_to_send.clear()
        self.received_message_bytes.clear()
        self.incoming_message_final_length = 0

    def _disconnect_client(self):
        """Clears the read/write buffers and closes the client socket if it currently exists.

        Use `schedule_client_disconnect()` instead of directly calling `_disconnect_client()` when sending messages.
        """
        self._clear_buffers()
        if self.does_client_socket_exist():
            log("closing client.")
            self.selector.unregister(self.client_sock)
            self.client_sock.shutdown(SHUT_RDWR)
            self.client_sock.close()
        else:
            log("client was already closed.")

    def __close(self):
        log("closing everything...")
        self.exit_event.set()

        # _disconnect_client() clears the buffers anyway
        # self._clear_buffers()
        self._disconnect_client()

        self.selector.unregister(self.server_sock)
        self.server_sock.shutdown(SHUT_RDWR)
        self.server_sock.close()

        if self.select_task is not None:
            self.select_task.cancel()
        if self.other_work_task is not None:
            self.other_work_task.cancel()

        if self.wait_for_empty_buffers_to_close_client_socket_task is not None:
            self.wait_for_empty_buffers_to_close_client_socket_task.cancel()

    async def select_loop(self):
        try:
            while True:
                events = self.selector.select(timeout=0)
                for selector_key, mask in events:
                    # It doesn't look very clear from this code but this callback comes from the data parameter of
                    # self.selector.register(<whatever>, <whatever>, data=callback_function_in_our_case).
                    # This is a kinda clever design but it's also confusing until you know that's what it is doing.
                    # I don't know why the library was made like this but whatever sure fine I guess.
                    # I'll just do it like this with this comment explaining it because it is admittedly convenient.

                    # maybe this callback should be wrapped in a try except?
                    callback = selector_key.data
                    if callable(callback):
                        if iscoroutinefunction(callback):
                            await callback(selector_key.fileobj, mask)
                        else:
                            callback(selector_key.fileobj, mask)

                await asyncio.sleep(1/30) # 1 EBF5 frame (maybe sleep less than that?)
        except (Exception, asyncio.CancelledError) as e: # Exception does not include asyncio.CancelledError apparently.
            if isinstance(e, asyncio.CancelledError):
                log("select_loop() received `asyncio.CancelledError`, closing everything...")
            else:
                log("select_loop() threw an error, closing everything...")

            self.__close()

            log("re-raising original error.")
            raise e
        finally:
            log("select_loop() exiting, socket will no longer send/receive if still alive.")

    async def other_work(self):
        while True:
            log("print from a task that'd be doing something else (+ sleep)... ")
            await asyncio.sleep(0.1)

    async def start(self):
        log("starting server and other work task.")
        self.select_task = asyncio.create_task(self.select_loop(), name="EBF5AP socket select loop")
        self.other_work_task = asyncio.create_task(self.other_work(), name="EBF5AP asyncio test other work")

        await self.exit_event.wait()

# server_test = EBF5AsyncSocket("localhost", 4999)
# asyncio.run(server_test.start())
