from __future__ import annotations

import asyncio

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop

from .AsyncSocket import EBF5AsyncSocket


class EBF5CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: EBF5Context):
        self.ctx = ctx

    # def _cmd_debug_unlock_item_test(self, client_item_name: str = ""):
    #     """
    #     Unlock an item in game, only for testing/debugging the client. This *does not* interface with AP at all.
    #     """
    #     if client_item_name == "":
    #         self.output("specify an item name")
    #         return False

    #     self.output("unimplemented")
    #     return False

    async def _cmd_connect_ebf5(self, address: str = ""):
        """
        Start listening on `address` for incoming connections from EBF5. EBF5 will be disconnected if it is connected
        when this command is used.

        :param address: IPv4 address to start listening on. Defaults to `localhost:4999` if unspecified.
        """
        if address == "":
            address = "localhost:4999"
        split_address = address.split(":")
        # This won't cover every edge case with the IPv4 address but it'll cover some of them.
        # If the address is can't be bound, the AsyncSocket will print a message to the user.
        if len(split_address) != 2:
            self.output("Please provide an IPv4 address in the form of `host:port`.")
            return False

        host, port = split_address

        try:
            port = int(port)
        except ValueError:
            self.output("Please use an integer port number.")
            return False

        if port < 0 or port > 65535:
            logger.info("port numbers must be positive integers below 65535.")
            return False
        if port < 1024:
            logger.warning("Warning: Flash Player places restrictions on connecting to ports below 1024."
                            " EBF5 might not be able to connect to this port.")

        await self.ctx.ebf5_socket.start(host, port)
        return True

    async def _cmd_disconnect_ebf5(self):
        """
        Disconnect EBF5 from the client if connected and stop listening for connections from EBF5.
        """
        if self.ctx.ebf5_socket.does_client_exist():
            logger.info("disconnecting EBF5...")
            self.ctx.ebf5_socket.schedule_client_disconnect()
        else:
            logger.info("EBF5 already wasn't connected to the client.")

        if self.ctx.ebf5_socket.does_server_exist():
            self.ctx.ebf5_socket.disconnect_server()
            logger.info("stopped listening for connections from EBF5.")
        else:
            logger.info("Client already wasn't listening for connections from EBF5.")

        return True

class EBF5Context(CommonContext):
    command_processor = EBF5CommandProcessor

    # TODO: implement ebf5_address here after i get the command for it working.
    def __init__(self, server_address: str | None = None, password: str | None = None, ebf5_address: str | None = None) -> None:
        super().__init__(server_address, password)
        #self.ebf5_address: str | None = ebf5_address
        self.ebf5_socket: EBF5AsyncSocket = EBF5AsyncSocket()

# General plan:
# 1. Add a launcher integration and make code run when you press launch.
# 2. Get talking with the game (launch this program first, it starts hosting a TCP server, then launch the game and
#    have them send a basic exchange back and forth).
# 3. Polish the connection process (allow the game to be launched first, add an "attempt to reconnect to client"
#    button in game, smooth out any annoyances on the AP client side of the communication process).

# We'll probably save figuring out patching for later?
# Presumably we want to start implementing the AP stuff once we can connect to the game.

def launch(*args: str):
    async def main(args):
        ctx = EBF5Context(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="EBF5 client, for text interfacing.")
    parsed_args = parser.parse_args(args)

    colorama.just_fix_windows_console()
    asyncio.run(main(parsed_args))
    colorama.deinit()