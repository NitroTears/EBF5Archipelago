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

chests = {
    # Glitch Zone / Undertale Area has no randomisable items (map 138/139)
    # HOPE HARBOR / WILD TROPICS
    location_names.CHEST_OUTSIDE_JERRYS_HOUSE: LocationData(0, "21-2-0", [EBF5LocationCategory.CHEST]),
    location_names.CHEST_WILD_TROPICS_ENTERANCE: LocationData(0, "26-1-1", [EBF5LocationCategory.CHEST]),
}

secrets = {

}

pickups = {

}
