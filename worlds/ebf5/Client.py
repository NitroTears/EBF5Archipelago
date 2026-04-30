from __future__ import annotations
from CommonClient import ClientCommandProcessor, CommonContext

class EBF5CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)
        # ^ self.ctx = ctx

    def _cmd_ebf5launchercomponenttest(self):
        self.output("_cmd_ebf5launchercomponenttest() was called successfully!")

# general plan:
# 1. add a launcher integration and make code run when you press launch.
# 2. get talking with the game (launch this program first, it starts hosting a TCP server, then launch the game and
#    have them send a basic exchange back and forth).
# 3. polish the connection process (allow the game to be launched first, add an "attempt to reconnect to client"
#    button in game, smooth out any annoyances on the AP client side of the communication process).
#
# we'll probably save figuring out patching for later?
# presumably we want to start implementing the AP stuff once we can connect to the game.

def launch():
    pass