from __future__ import annotations

import asyncio

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, server_loop

from .AsyncSocket import EBF5AsyncSocket


# We're gonna need at least a custom command or two to connect to the game.
class EBF5CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: EBF5Context):
        super().__init__(ctx)

    def _cmd_ebf5launchercomponenttest(self):
        """Test command."""
        self.output("_cmd_ebf5launchercomponenttest() was called successfully!")

    def _cmd_debug_unlock_item_test(self, item_AP_name: str = ""):
        """
        Unlock an item in game, only for testing/debugging the client. This does not interface with AP at all.
        """
        if item_AP_name == "":
            self.output("specify an item name")
            return False

        self.output("unimplemented")
        return False

class EBF5Context(CommonContext):
    command_processor = EBF5CommandProcessor
    ebf5_socket: EBF5AsyncSocket | None = None

    # TODO: implement ebf5_address here after i get the command for it working.
    def __init__(self, server_address: str | None = None, password: str | None = None) -> None:
        super().__init__(server_address, password)

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