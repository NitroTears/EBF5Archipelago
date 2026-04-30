from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.ebf5.Options import EpicBattleFantasy5Options
from worlds.LauncherComponents import Component, components, Type, launch as launch_component
from .Items import *
from .Locations import *

def launch_client(*args: str):
    from .Client import launch
    launch_component(launch, name="EBF5 client", args=args)

components.append(Component("Epic Battle Fantasy 5 Client", func=launch_client, component_type=Type.CLIENT))

class EpicBattleFantasy5Web(WebWorld):
    theme = "jungle"
    # TODO: Make this more accurate
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the the EBF5 Randomiser on your computer.",
        "English",
        "setup_en",
        "setup/en",
        ["NitroTears"]
    )]


class EpicBattleFantasy5World(World):
    """
    A turn-based RPG adventure, full of video game references, juvenile dialogue, and anime fanservice... 
    and also strategic combat, monster catching, and tons of treasure hunting!
    """
    game = "Epic Battle Fantasy 5"
    web = EpicBattleFantasy5Web()
    options_dataclass = EpicBattleFantasy5Options
    options: EpicBattleFantasy5Options
    
    
    # wait im not even putting this into a constructor
    # i feel like i should be doing that.
    # i should double check
    # hmmm ok yeah it should be fine because im just setting class varaibles, though yeah it's pretty messy.
    # again this should be moved elsewhere if possible, i just want to get the bare minimum world stuff done,
    # so i can start creating the client and communicating with the game.


    # I feel like this probably isn't the best way to do this.
    # I'm just trying to get it to launch from the launcher right now, this should be cleaned up at some point.
    # if anything it should probably be moved to `Items`.
    # it also doesn't include `Items.progression`.
    item_datas = list(equipment.values()) + list(cards.values()) + skills + crafting_items + food + boosters + key_items
    item_name_to_id = {}
    location_name_to_id = {}
    for i in range(len(item_datas)):
        item_name_to_id[item_datas[i].game_id] = item_datas[i].id
    # again this will need to be manually updated if more locationDatas are created.
    location_datas = list(shop_items.values()) + list(chests.values()) # we don't have any secrets or pickups yet so im not sure how they'll be structured. 
    for i in range(len(location_datas)):
        location_name_to_id[location_datas[i].game_id] = location_datas[i].id

    #item_name_to_id = {name : id for }
    