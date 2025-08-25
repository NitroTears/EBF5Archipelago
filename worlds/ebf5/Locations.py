from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Location
from worlds.ebf5.static_names import location_names


class EBF5Location(Location):
    game: str = "Epic Battle Fantasy 5"

class EBF5LocationCategory(IntEnum):
    CHEST       = 0
    SHOP        = 1
    PICKUP      = 2
    SECRET      = 3
    SEASONAL    = 4

class LocationData(NamedTuple):
    id: Optional[int]
    game_id: str
    category: list[EBF5LocationCategory]


# Item code will either be "{mapNo}-{chestNo}-{itemIndex}" or something epecific like "eqsh-1" for equipment shop item 1.

shop_items = {
    location_names.EQUIPMENT_SHOP_ITEM_1: LocationData(5000, "eqsh-1", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_2: LocationData(5001, "eqsh-2", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_3: LocationData(5002, "eqsh-3", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_4: LocationData(5003, "eqsh-4", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_5: LocationData(5004, "eqsh-5", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_6: LocationData(5005, "eqsh-6", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_7: LocationData(5006, "eqsh-7", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_8: LocationData(5007, "eqsh-8", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_9: LocationData(5008, "eqsh-9", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_10: LocationData(5009, "eqsh-10", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_11: LocationData(5010, "eqsh-11", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_12: LocationData(5011, "eqsh-12", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_13: LocationData(5012, "eqsh-13", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_14: LocationData(5013, "eqsh-14", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_15: LocationData(5014, "eqsh-15", [EBF5LocationCategory.SHOP]),
    location_names.EQUIPMENT_SHOP_ITEM_16: LocationData(5015, "eqsh-16", [EBF5LocationCategory.SHOP, EBF5LocationCategory.SEASONAL]),
    location_names.EQUIPMENT_SHOP_ITEM_17: LocationData(5016, "eqsh-17", [EBF5LocationCategory.SHOP, EBF5LocationCategory.SEASONAL]),
    location_names.EQUIPMENT_SHOP_ITEM_18: LocationData(5017, "eqsh-18", [EBF5LocationCategory.SHOP, EBF5LocationCategory.SEASONAL]),
    location_names.EQUIPMENT_SHOP_ITEM_19: LocationData(5018, "eqsh-19", [EBF5LocationCategory.SHOP, EBF5LocationCategory.SEASONAL]),
    location_names.EQUIPMENT_SHOP_ITEM_20: LocationData(5019, "eqsh-20", [EBF5LocationCategory.SHOP, EBF5LocationCategory.SEASONAL]),
    location_names.EQUIPMENT_SHOP_ITEM_21: LocationData(5020, "eqsh-21", [EBF5LocationCategory.SHOP, EBF5LocationCategory.SEASONAL]),
    location_names.EQUIPMENT_SHOP_ITEM_22: LocationData(5021, "eqsh-22", [EBF5LocationCategory.SHOP, EBF5LocationCategory.SEASONAL]),
}

chests = { # Chest locations are marked by ebf wiki co-ordinates, world map co-ords, then map co-ords.
    # Secret World (Undertale)
    location_names.CHEST_AFTER_SNOWFLAKE_LEFT: LocationData(0, "139-0-0", [EBF5LocationCategory.CHEST]),                            # H01
    location_names.CHEST_AFTER_SNOWFLAKE_RIGHT: LocationData(0, "139-1-0", [EBF5LocationCategory.CHEST]),                           # H01
    # HOPE HARBOR / WILD TROPICS    
    location_names.CHEST_OUTSIDE_JERRYS_HOUSE: LocationData(0, "21-2-0", [EBF5LocationCategory.CHEST]),                             # A5 - B06
    location_names.CHEST_WILD_TROPICS_ENTERANCE: LocationData(0, "26-1-1", [EBF5LocationCategory.CHEST]),                           # B4 - P01
    location_names.CHEST_WILD_TROPICS_FARM_BLOCK_PUZZLE: LocationData(0, "29-3-0", [EBF5LocationCategory.CHEST]),                   # A3 - B02
    location_names.CHEST_WILD_TROPICS_FARM_BLOCK_ENEMY: LocationData(0, "29-2-0", [EBF5LocationCategory.CHEST]),                    # A3 - C06
    location_names.CHEST_WILD_TROPICS_MIDDLE_AREA_SECRET_BUSH: LocationData(0, "30-3-0", [EBF5LocationCategory.CHEST]),             # B3 - B01
    location_names.CHEST_WILD_TROPICS_MIDDLE_AREA_RIGHT_ENTRANCE_CHEST: LocationData(0, "30-5-0", [EBF5LocationCategory.SECRET]),   # B3 - S04
    location_names.CHEST_WILD_TROPICS_OUTSIDE_KITCHEN: LocationData(0, "35-1-0", [EBF5LocationCategory.SECRET]),                    # C2 - G10       
    location_names.PICKUP_SHOVEL: LocationData(0, "33-??-??", [EBF5LocationCategory.PICKUP]), # TODO: INVESTIGATE ACQUIRING SHOVEL  # A2 - K06
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_ENEMY: LocationData(0, "33-1-0", [EBF5LocationCategory.CHEST]),                 # A2 - P02
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_DIRT: LocationData(0, "33-2-0", [EBF5LocationCategory.CHEST]),                  # A2 - C01
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_FOOD_SHOP: LocationData(0, "33-3-0", [EBF5LocationCategory.CHEST]),             # A2 - L02
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_HIGHER_PATH: LocationData(0, "33-4-0", [EBF5LocationCategory.CHEST]),           # A2 - O02
    location_names.CHEST_MATTS_HOUSE_OTHER_ROOM: LocationData(0, "152-0-0", [EBF5LocationCategory.CHEST]),                          # R05
    location_names.CHEST_MATTS_HOUSE_LEFT_SOCK_DRAWER: LocationData(0, "152-2-0", [EBF5LocationCategory.SECRET]),                   # D03
    location_names.CHEST_MATTS_HOUSE_RIGHT_SOCK_DRAWER: LocationData(0, "152-2-0", [EBF5LocationCategory.SECRET]),                  # F03
    location_names.CHEST_DRAGON_ARMOR_CAVE_BEHIND_ENEMY_LEFT: LocationData(0, "166-0-0", [EBF5LocationCategory.CHEST]),             # D07
    location_names.CHEST_DRAGON_ARMOR_CAVE_BEHIND_ENEMY_RIGHT: LocationData(0, "166-1-0", [EBF5LocationCategory.CHEST]),            # R05
    location_names.CHEST_DRAGON_ARMOR_CAVE_CENTER: LocationData(0, "166-3-0", [EBF5LocationCategory.CHEST]),                        # L06
    location_names.CHEST_INDYS_CAVE_BLOCK_PUZZLE_TOP: LocationData(0, "167-0-0", [EBF5LocationCategory.CHEST]),                     # R05
    location_names.CHEST_INDYS_CAVE_BLOCK_PUZZLE_BOTTOM: LocationData(0, "167-1-0", [EBF5LocationCategory.CHEST]),                  # R06
}

secrets = {

}

pickups = {

}
