from __future__ import annotations
from CommonClient import ClientCommandProcessor, CommonContext, server_loop, get_base_parser, gui_enabled
import asyncio

# We're gonna need at least a custom command or two to connect to the game.
class EBF5CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: EBF5Context):
        super().__init__(ctx)
        # ^ self.ctx = ctx

    def _cmd_ebf5launchercomponenttest(self):
        self.output("_cmd_ebf5launchercomponenttest() was called successfully!")
    
class EBF5Context(CommonContext):
    command_processor = EBF5CommandProcessor

# General plan:
# 1. Add a launcher integration and make code run when you press launch.
# 2. Get talking with the game (launch this program first, it starts hosting a TCP server, then launch the game and
#    have them send a basic exchange back and forth).
# 3. Polish the connection process (allow the game to be launched first, add an "attempt to reconnect to client"
#    button in game, smooth out any annoyances on the AP client side of the communication process).

# We'll probably save figuring out patching for later?
# Presumably we want to start implementing the AP stuff once we can connect to the game.

# OK it looks like the class we need to actually get the UI is GameManager, which we make a child class of.
# Or actually i think i can just use run_ui, at least for now. Maybe i'll have to make a custom class later.

def launch(*args: str):
    # This feels relatively undocumented which makes it a bit of a pain to have to manually search through how
    # other implementations do this to see how i need to do it.
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