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
'''
# For all items, the array item will look like the below
{
  location_name: LocationData(
     arbitrary item id for AP,
     game_id: chess access code, explained below
     array of item types
  )
}

# OUTDATED, see below
# To explain the item code, look at this example
if (mapNo == 139)
{
    setArea(GLITCH_ZONE);
    ...
    maps.objectData = [ {
             "mc": "chest0",
             "type": CHEST,
             "data": [Equips.powerpaw, 1, Items.turnip, 1, Items.poptart, 1]
          }, {
             "mc": "chest1",
             "type": CHEST,
             "data": [Equips.popedress, 1, Items.bread, 1, Items.riceball, 1]
          }];
    ...
}
the location CHEST_AFTER_SNOWFLAKE_LEFT can be found here with 139-0-0,
139 for the mapNo in the if statement
0 for the index in the maps.objectData
0 for chestX, in this case chest0

It will either be chest access code will either be "{mapNo}-{chestNo}-{itemIndex}" or something epecific like "eqsh-1" for equipment shop item 1.
'''

'''
# New LocationData game_id formatting:
    <item type>-<map id>-<chest id>-<item index>
    where
        item type -> chest, shop, quest
        map id -> the number of the room in the mapData file, found in "if(mapNo == X)" at the start of each block
        chest id -> the number at the end of the name of the chest. Chests in mapData are named "chestX" and you want the X
        item index -> the index of the item in the chest's array.
    so, for the example above,
    "chest-139-0-0"
    would describe the Equips.powerpaw location. This only refers to ONE stack of items in the chest now.

    To convert from the old format to the new, add "chest-" to the front, double check the second number is correct, and change the third to the index of the item in the chest.
    Also: make sure your numbers are zero-indexed.
'''

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

chests = { # Chest locations aren't visibly obvious, so I've written comments with a location that is first then world map co-ords (if on world map), then map co-ords (co-ords from EBF Wiki)
    # (From UniverseGlory) Parenthesis in the location is the entrance for a room that doesn't appear on the main map. If this includes multiple connected rooms, the entrance is treated as a header before a "|" sign.
    # (From Solanum) Locations marked with a * on their position are "minor" items (not cards/equips/skills/key items/etc). I put (one per chest of) these in for HH/WT but we're not using them yet.

    # Secret World (Undertale)
    # location_names.CHEST_SECRET_WORLD_2: LocationData(0, "138-0-0", [EBF5LocationCategory.CHEST]),                                          # E0(M04) | J04 - C02*
    # location_names.CHEST_SECRET_WORLD_1: LocationData(0, "138-1-1", [EBF5LocationCategory.CHEST]),                                          # E0(M04) | J04 - N06*
    location_names.CHEST_AFTER_SNOWFLAKE_LEFT: LocationData(0, "map139-chest0-item0", [EBF5LocationCategory.CHEST]),                                    # E0(M04) | J04 | I00 - H01
    location_names.CHEST_AFTER_SNOWFLAKE_RIGHT: LocationData(0, "map139-chest1-item0", [EBF5LocationCategory.CHEST]),                                   # E0(M04) | J04 | I00 - P01
    # HOPE HARBOR / WILD TROPICS    
    # location_names.CHEST_OUTSIDE_JERRYS_HOUSE_LEFT: LocationData(0, "21-1-1", [EBF5LocationCategory.CHEST]),                                # A5 - B02*
    location_names.CHEST_OUTSIDE_JERRYS_HOUSE_PUZZLE: LocationData(0, "map21-chest2-item0", [EBF5LocationCategory.CHEST]),                              # A5 - B06
    # location_names.CHEST_OUTSIDE_JERRYS_HOUSE_SHOVEL: LocationData(0, "21-3-3", [EBF5LocationCategory.CHEST]),                              # A5 - G01*
    # location_names.CHEST_OUTSIDE_JERRYS_HOUSE_LADDER: LocationData(0, "21-4-4", [EBF5LocationCategory.CHEST]),                              # A5 - M09*
    # location_names.CHEST_OUTSIDE_MATTS_HOUSE_CACTUS: LocationData(0, "22-0-5", [EBF5LocationCategory.SECRET]),                              # B5 - O03*
    # location_names.CHEST_NOLEGS_ROOM_BOTTOM_LEFT: LocationData(0, "21-0-1", [EBF5LocationCategory.CHEST]),                                  # C5 - D08*
    # location_names.CHEST_NOLEGS_ROOM_CRACKED_POT: LocationData(0, "21-1-2", [EBF5LocationCategory.SECRET]),                                 # C5 - J04*
    # location_names.CHEST_NOLEGS_ROOM_AFTER_NOLEGS: LocationData(0, "21-2-6", [EBF5LocationCategory.CHEST]),                                 # C5 - N02*
    # location_names.CHEST_HOPE_HARBOR_SHOPS_BEHIND_LOGS: LocationData(0, "27-0-1", [EBF5LocationCategory.CHEST]),                            # C4 - R02*
    # location_names.CHEST_HOPE_HARBOR_SHOPS_BEHIND_TREE: LocationData(0, "27-1-2", [EBF5LocationCategory.CHEST]),                            # C4 - S07*
    # location_names.CHEST_HOPE_HARBOR_SHOPS_CHILI: LocationData(0, "27-2-5", [EBF5LocationCategory.SECRET]),                                 # C4 - F07*
    # location_names.CHEST_HOPE_HARBOR_SHOPS_LOGS: LocationData(0, "27-3-6", [EBF5LocationCategory.SECRET]),                                  # C4 - O01*
    location_names.CHEST_WILD_TROPICS_ENTRANCE_TOP_RIGHT: LocationData(0, "map26-chest1-item1", [EBF5LocationCategory.CHEST]),                          # B4 - P01
    # location_names.CHEST_WILD_TROPICS_ENTRANCE_CENTER: LocationData(0, "26-1-2", [EBF5LocationCategory.CHEST]),                             # B4 - H07*
    # location_names.CHEST_WILD_TROPICS_ENTRANCE_BOTTOM_LEFT: LocationData(0, "26-2-3", [EBF5LocationCategory.CHEST]),                        # B4 - E10*
    # location_names.CHEST_WILD_TROPICS_ENTRANCE_TOP_LEFT: LocationData(0, "26-3-4", [EBF5LocationCategory.CHEST]),                           # B4 - C01*
    # location_names.CHEST_WILD_TROPICS_WELL_ROOM_TOP_RIGHT: LocationData(0, "26-4-5", [EBF5LocationCategory.CHEST]),                         # B4 - R05*
    # location_names.CHEST_WILD_TROPICS_ENTRANCE_GRASS: LocationData(0, "25-0-1", [EBF5LocationCategory.CHEST]),                              # A4 - S01*
    # location_names.CHEST_WILD_TROPICS_WELL_ROOM_PUZZLE: LocationData(0, "25-1-2", [EBF5LocationCategory.CHEST]),                            # A4 - C01*
    # location_names.CHEST_WILD_TROPICS_WELL_ROOM_BOTTOM_LEFT: LocationData(0, "25-2-3", [EBF5LocationCategory.CHEST]),                       # A4 - B09*
    # location_names.CHEST_WILD_TROPICS_WELL_ROOM_CACTUS: LocationData(0, "25-3-5", [EBF5LocationCategory.SECRET]),                           # A4 - E05*
    # location_names.CHEST_WILD_TROPICS_WELL_ROOM_ROOT: LocationData(0, "25-4-6", [EBF5LocationCategory.SECRET]),                             # A4 - P01*
    # location_names.CHEST_WILD_TROPICS_FARM_BLOCK_BOTTOM_LEFT: LocationData(0, "29-0-1", [EBF5LocationCategory.CHEST]),                      # A3 - B10*
    location_names.CHEST_WILD_TROPICS_FARM_BLOCK_ENEMY: LocationData(0, "map29-chest2-item0", [EBF5LocationCategory.CHEST]),                            # A3 - C06
    location_names.CHEST_WILD_TROPICS_FARM_BLOCK_PUZZLE: LocationData(0, "map29-chest3-item0", [EBF5LocationCategory.CHEST]),                           # A3 - B02
    # location_names.CHEST_WILD_TROPICS_FARM_BLOCK_BOTTOM_RIGHT: LocationData(0, "29-3-4", [EBF5LocationCategory.CHEST]),                     # A3 - S10*
    # location_names.CHEST_WILD_TROPICS_FARM_BLOCK_KEG: LocationData(0, "29-4-5", [EBF5LocationCategory.SECRET]),                             # A3 - B08*
    # location_names.CHEST_WILD_TROPICS_FARM_BLOCK_PUMPKIN: LocationData(0, "29-5-6", [EBF5LocationCategory.SECRET]),                         # A3 - M06*
    # location_names.CHEST_WILD_TROPICS_FARM_BLOCK_GARLIC: LocationData(0, "29-6-7", [EBF5LocationCategory.SECRET]),                          # A3 - Q06*
    # location_names.CHEST_WILD_TROPICS_MIDDLE_AREA_BAT: LocationData(0, "30-0-1", [EBF5LocationCategory.CHEST]),                             # B3 - N10*
    # location_names.CHEST_WILD_TROPICS_MIDDLE_AREA_BOTTOM_LEFT: LocationData(0, "30-1-2", [EBF5LocationCategory.CHEST]),                     # B3 - B10*
    location_names.CHEST_WILD_TROPICS_MIDDLE_AREA_RIGHT_ENTRANCE_CHEST_RIGHT: LocationData(0, "map30-chest3-item0", [EBF5LocationCategory.CHEST]),      # B3 - S04
    # location_names.CHEST_WILD_TROPICS_MIDDLE_AREA_RIGHT_ENTRANCE_CHEST_LEFT: LocationData(0, "30-3-4", [EBF5LocationCategory.CHEST]),       # B3 - Q05*
    location_names.CHEST_WILD_TROPICS_MIDDLE_AREA_SECRET_BUSH: LocationData(0, "map30-chest5-item0", [EBF5LocationCategory.SECRET]),                    # B3 - B01
    # location_names.CHEST_WILD_TROPICS_MONOLITH_LEFT: LocationData(0, "31-0-1", [EBF5LocationCategory.CHEST]),                               # C3 - J10*
    # location_names.CHEST_WILD_TROPICS_MONOLITH_RIGHT: LocationData(0, "31-1-2", [EBF5LocationCategory.CHEST]),                              # C3 - R10*
    location_names.CHEST_WILD_TROPICS_OUTSIDE_KITCHEN_HIDDEN: LocationData(0, "map35-chest1-item0", [EBF5LocationCategory.CHEST]),                      # C2 - G10 note: there is technically a visible chest here.
    # location_names.CHEST_WILD_TROPICS_OUTSIDE_KITCHEN_LOGS: LocationData(0, "35-2-6", [EBF5LocationCategory.SECRET]),                       # C2 - K04*
    location_names.PICKUP_SHOVEL: LocationData(0, "33-??-??", [EBF5LocationCategory.PICKUP]), # TODO: INVESTIGATE ACQUIRING SHOVEL          # A2 - K06
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_ENEMY: LocationData(0, "map33-chest1-item0", [EBF5LocationCategory.CHEST]),                         # A2 - P02
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_DIRT: LocationData(0, "map33-chest2-item0", [EBF5LocationCategory.CHEST]),                          # A2 - C01
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_FOOD_SHOP: LocationData(0, "map33-chest3-item0", [EBF5LocationCategory.CHEST]),                     # A2 - L02
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_HIGHER_PATH: LocationData(0, "map33-chest4-item0", [EBF5LocationCategory.CHEST]),                   # A2 - O06
    # location_names.CHEST_WILD_TROPICS_MARKET_LEFT: LocationData(0, "33-6-5", [EBF5LocationCategory.CHEST]),                                 # A2 - B07*
    # location_names.CHEST_WILD_TROPICS_MARKET_MEAT: LocationData(0, "33-7-6", [EBF5LocationCategory.CHEST]),                                 # A2 - L07*
    # location_names.CHEST_WILD_TROPICS_NATALIE_RIGHT: LocationData(0, "34-0-1", [EBF5LocationCategory.CHEST]),                               # B2 - N03*
    # location_names.CHEST_WILD_TROPICS_NATALIE_LEFT: LocationData(0, "34-1-2", [EBF5LocationCategory.CHEST]),                                # B2 - F03*
    location_names.CHEST_MATTS_HOUSE_OTHER_ROOM: LocationData(0, "map152-chest0-item1", [EBF5LocationCategory.CHEST]),                                  # B5(H05) - R05
    # location_names.CHEST_MATTS_HOUSE_FRIDGE: LocationData(0, "152-4-1", [EBF5LocationCategory.SECRET]),                                     # B5(H05) -JF03*
    location_names.CHEST_MATTS_HOUSE_LEFT_SOCK_DRAWER: LocationData(0, "map152-chest2-item0", [EBF5LocationCategory.SECRET]),                           # B5(H05) - D03
    location_names.CHEST_MATTS_HOUSE_RIGHT_SOCK_DRAWER: LocationData(0, "map152-chest3-item0", [EBF5LocationCategory.SECRET]),                          # B5(H05) - F03
    # location_names.CHEST_MATTS_HOUSE_ARCADE_REWARD: LocationData(0, "152-7-4", [EBF5LocationCategory.CHEST]),                               # B5(H05) - G07*
    location_names.CHEST_DRAGON_ARMOR_CAVE_BEHIND_ENEMY_LEFT: LocationData(0, "map166-chest0-item1", [EBF5LocationCategory.CHEST]),                     # C3(G04) - D07
    location_names.CHEST_DRAGON_ARMOR_CAVE_BEHIND_ENEMY_RIGHT: LocationData(0, "map166-chest1-item0", [EBF5LocationCategory.CHEST]),                    # C3(G04) - R05
    # location_names.CHEST_DRAGON_ARMOR_CAVE_BOTTOM: LocationData(0, "166-2-2", [EBF5LocationCategory.CHEST]),                                # C3(G04) - J10*
    location_names.CHEST_DRAGON_ARMOR_CAVE_CENTER: LocationData(0, "map166-chest2-item0", [EBF5LocationCategory.CHEST]),                                # C3(G04) - L06
    location_names.CHEST_INDYS_CAVE_BLOCK_PUZZLE_TOP: LocationData(0, "map167-chest0-item0", [EBF5LocationCategory.CHEST]),                             # C3(R07) - R05
    location_names.CHEST_INDYS_CAVE_BLOCK_PUZZLE_BOTTOM: LocationData(0, "map167-chest1-item0", [EBF5LocationCategory.CHEST]),                          # C3(R07) - R06
    # location_names.CHEST_INDYS_CAVE_ENEMY: LocationData(0, "167-3-2", [EBF5LocationCategory.CHEST]),                                        # C3(R07) - G03*
    # location_names.CHEST_JERRYS_HOUSE_DRESSER: LocationData(0, "150-1-0", [EBF5LocationCategory.SECRET]),                                   # A5(N03) - G03*
    # location_names.CHEST_JERRYS_HOUSE_CHEST: LocationData(0, "150-2-1", [EBF5LocationCategory.CHEST]),                                      # A5(N03) - M04*
    # location_names.CHEST_JERRYS_BASEMENT_LEFT: LocationData(0, "151-0-1", [EBF5LocationCategory.CHEST]),                                    # A5(N03) | I04 - E09*
    # location_names.CHEST_JERRYS_BASEMENT_RIGHT: LocationData(0, "151-1-2", [EBF5LocationCategory.CHEST]),                                   # A5(N03) | I04 - Q08*
    # location_names.CHEST_WILD_TROPICS_MATERIAL_SHOP_CHEST: LocationData(0, "153-3-0", [EBF5LocationCategory.CHEST]),                        # C4(K03) - N05*
    # location_names.CHEST_WILD_TROPICS_FOOD_SHOP_CHEST: LocationData(0, "154-3-0", [EBF5LocationCategory.CHEST]),                            # C4(D06) - F08*
    # location_names.CHEST_WILD_TROPICS_FOOD_SHOP_SECOND_FLOOR: LocationData(0, "155-1-0", [EBF5LocationCategory.CHEST]),                     # C4(D06) | M04 - J09*
    # location_names.CHEST_WILD_TROPICS_KITCHEN_HIDDEN: LocationData(0, "156-1-0", [EBF5LocationCategory.CHEST]),                             # C2(F05) - P04*
    # location_names.CHEST_WILD_TROPICS_KITCHEN_FRIDGE: LocationData(0, "156-2-1", [EBF5LocationCategory.SECRET]),                            # C2(F05) - H04*
    # location_names.CHEST_WILD_TROPICS_KITCHEN_OVEN: LocationData(0, "156-3-2", [EBF5LocationCategory.SECRET]),                              # C2(F05) - J04*
    # location_names.CHEST_WILD_TROPICS_EQUIP_SHOP_CHEST: LocationData(0, "157-2-0", [EBF5LocationCategory.CHEST]),                           # C2(Q02) - E04*
    # location_names.CHEST_WILD_TROPICS_EQUIP_SHOP_BASEMENT_RIGHT: LocationData(0, "158-0-0", [EBF5LocationCategory.CHEST]),                  # C2(Q02) | C2 - P03*
    # location_names.CHEST_WILD_TROPICS_EQUIP_SHOP_BASEMENT_LEFT: LocationData(0, "158-1-1", [EBF5LocationCategory.CHEST]),                   # C2(Q02) | C2 - E04*
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_1_ENEMY: LocationData(0, "map36-chest1-item0", [EBF5LocationCategory.CHEST]),                           # D2 - B02
    # location_names.CHEST_AFTER_LAURELIN_LEFT: LocationData(0, "36-2-2", [EBF5LocationCategory.CHEST]),                                      # D2 - Q07*
    location_names.CHEST_AFTER_LAURELIN_RIGHT: LocationData(0, "map36-chest3-item0", [EBF5LocationCategory.CHEST]),                                     # D2 - S07
    location_names.CHEST_AFTER_LAURELIN_MIDDLE: LocationData(0, "map36-chest4-item0", [EBF5LocationCategory.CHEST]),                                    # D2 - R07
    # location_names.CHEST_HOPE_HARBOR_EAST_COAST_1_RAFT: LocationData(0, "36-5-5", [EBF5LocationCategory.CHEST]),                            # D2 - B02*
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_BOTTOM_ENEMY: LocationData(0, "map32-chest1-item1", [EBF5LocationCategory.CHEST]),                    # D3 - S10
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_BEHIND_TENT: LocationData(0, "map32-chest2-item0", [EBF5LocationCategory.CHEST]),                     # D3 - P04
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_TOP_ENEMY: LocationData(0, "map32-chest3-item0", [EBF5LocationCategory.CHEST]),                       # D3 - S01
    # location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_FISH: LocationData(0, "32-5-5", [EBF5LocationCategory.SECRET]),                           # D3 - M06*
    # location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_TENT: LocationData(0, "32-6-6", [EBF5LocationCategory.CHEST]),                            # D3 - P07*
    # location_names.CHEST_HOPE_HARBOR_EAST_COAST_3_BOTTOM_RIGHT: LocationData(0, "28-1-1", [EBF5LocationCategory.CHEST]),                    # D4 - Q10*
    # location_names.CHEST_HOPE_HARBOR_EAST_COAST_3_BOTTOM_LEFT: LocationData(0, "28-2-2", [EBF5LocationCategory.CHEST]),                     # D4 - B09*
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_3_BEHIND_ENEMY: LocationData(0, "map28-chest3-item0", [EBF5LocationCategory.CHEST]),                    # D4 - M10
    # location_names.CHEST_HOPE_HARBOR_EAST_COAST_3_CACTUS: LocationData(0, "28-4-5", [EBF5LocationCategory.SECRET]),                         # D4 - B01*
    location_names.CHEST_HOPE_HARBOR_BEHIND_ICE_CAVE: LocationData(0, "map24-chest1-item0", [EBF5LocationCategory.CHEST]),                              # D5 - R02
    # location_names.CHEST_HOPE_HARBOR_JOTUN_ROOM_LEFT: LocationData(0, "24-1-2", [EBF5LocationCategory.CHEST]),                              # D5 - C07*
    location_names.CHEST_HOPE_HARBOR_OUTSIDE_ICE_CAVE_LEFT: LocationData(0, "map24-chest3-item0", [EBF5LocationCategory.CHEST]),                        # D5 - M07
    location_names.CHEST_HOPE_HARBOR_OUTSIDE_ICE_CAVE_MIDDLE: LocationData(0, "map24-chest4-item0", [EBF5LocationCategory.CHEST]),                      # D5 - N08
    # location_names.CHEST_HOPE_HARBOR_OUTSIDE_ICE_CAVE_RIGHT: LocationData(0, "24-4-5", [EBF5LocationCategory.CHEST]),                       # D5 - R08*
    # location_names.CHEST_HOPE_HARBOR_JOTUN_ROOM_BONE: LocationData(0, "24-5-6", [EBF5LocationCategory.SECRET]),                             # D5 - B01*
    #   ICE CAVE
    location_names.CHEST_ICE_CAVE_ROOM_2_BEHIND_ENEMY: LocationData(0, "map19-chest2-item1", [EBF5LocationCategory.CHEST]),                             # D5(P06) | D4 - K09
    location_names.CHEST_ICE_CAVE_ROOM_3_BEHIND_ENEMY: LocationData(0, "map20-chest2-item0", [EBF5LocationCategory.CHEST]),                             # D5(P06) | E3 - S03
    #       FREEZEFLAME DUNGEON
    location_names.CHEST_FREEZEFLAME_DUNGEON_BEHIND_ENEMY_LEFT: LocationData(0, "map201-chest0-item0", [EBF5LocationCategory.CHEST]),                   # D5(P06) | E2 - D03
    location_names.CHEST_FREEZEFLAME_DUNGEON_BEHIND_ENEMY_RIGHT: LocationData(0, "map201-chest2-item0", [EBF5LocationCategory.CHEST]),                  # D5(P06) | E2 - M08
    location_names.CHEST_FREEZEFLAME_DUNGEON_ICE_BLOCK_PUZZLE_ROOM: LocationData(0, "map200-chest2-item0", [EBF5LocationCategory.CHEST]),               # D5(P06) | D2 - B04
    location_names.CHEST_FREEZEFLAME_DUNGEON_ICE_SLIDE_PUZZLE_ROOM: LocationData(0, "map203-chest1-item0", [EBF5LocationCategory.CHEST]),               # D5(P06) | D1 - B06
    location_names.CHEST_FREEZEFLAME_DUNGEON_FIRE_BLOCK_PUZZLE_ROOM: LocationData(0, "map202-chest2-item0", [EBF5LocationCategory.CHEST]),              # D5(P06) | F2 - Q06
    location_names.CHEST_FREEZEFLAME_DUNGEON_FIRE_COMBAT_ROOM_LAST: LocationData(0, "map205-chest1-item0", [EBF5LocationCategory.CHEST]),               # D5(P06) | F1 - R06
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_ICE_TOP: LocationData(0, "map206-chest0-item0", [EBF5LocationCategory.CHEST]),                   # D5(P06) | E0 - D02
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_TOP: LocationData(0, "map206-chest1-item0", [EBF5LocationCategory.CHEST]),                  # D5(P06) | E0 - P02
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_MIDDLE: LocationData(0, "map206-chest3-item0", [EBF5LocationCategory.CHEST]),               # D5(P06) | E0 - R03
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_BOTTOM: LocationData(0, "map206-chest4-item0", [EBF5LocationCategory.CHEST]),               # D5(P06) | E0 - Q05
    #   GRAND GALLERY
    location_names.CHEST_GRAND_GALLERY_ENTRANCE: LocationData (0, "map38-chest3-item0", [EBF5LocationCategory.CHEST]),                                  # B1 - Q08
    location_names.CHEST_GRAND_GALLERY_LEFT_HALL: LocationData(0, "map40-chest0-item1", [EBF5LocationCategory.CHEST]),                                  # A0 - L05
    location_names.CHEST_GRAND_GALLERY_LEFT_TOP_KEY: LocationData(0, "map40-chest1-item1", [EBF5LocationCategory.CHEST]),                               # A0 - B05
    location_names.CHEST_GRAND_GALLERY_LEFT_MIDDLE_KEY: LocationData(0, "map40-chest2-item1", [EBF5LocationCategory.CHEST]),                            # A0 - B06
    location_names.CHEST_GRAND_GALLERY_LEFT_BOTTOM_KEY: LocationData(0, "map40-chest3-item1", [EBF5LocationCategory.CHEST]),                            # A0 - B07
    location_names.CHEST_GRAND_GALLERY_LEFT_MAZE_RIGHT: LocationData(0, "map37-chest1-item0", [EBF5LocationCategory.CHEST]),                            # A1 - P10 
    location_names.CHEST_GRAND_GALLERY_LEFT_MAZE_LEFT: LocationData(0, "map37-chest4-item0", [EBF5LocationCategory.CHEST]),                             # A1 - C08
    location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_BEHIND_ENEMY_LEFT: LocationData(0, "map39-chest2-item0", [EBF5LocationCategory.CHEST]),               # C1 - G10
    location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_ANGEL_STATUE_LEFT: LocationData(0, "map39-chest4-item0", [EBF5LocationCategory.CHEST]),               # C1 - K08
    location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_ANGEL_STATUE_RIGHT: LocationData(0, "map39-chest5-item0", [EBF5LocationCategory.CHEST]),              # C1 - M08
    location_names.CHEST_GRAND_GALLERY_RIGHT_TOP_KEY: LocationData(0, "map42-chest1-item1", [EBF5LocationCategory.CHEST]),                              # C0 - S05
    location_names.CHEST_GRAND_GALLERY_RIGHT_MIDDLE_KEY: LocationData(0, "map42-chest2-item1", [EBF5LocationCategory.CHEST]),                           # C0 - S06
    location_names.CHEST_GRAND_GALLERY_RIGHT_BOTTOM_KEY: LocationData(0, "map42-chest3-item1", [EBF5LocationCategory.CHEST]),                           # C0 - S07
    location_names.CHEST_GRAND_GALLERY_80_MEDALS_ROOM: LocationData(0, "map336-chest0-item1", [EBF5LocationCategory.CHEST]),                            # C0(R03) - G06
    location_names.CHEST_GRAND_GALLERY_50_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "map162-chest2-item0", [EBF5LocationCategory.CHEST]),          # C0(N03) - F04
    location_names.CHEST_GRAND_GALLERY_50_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "map162-chest5-item1", [EBF5LocationCategory.CHEST]),         # C0(N03) - R04
    location_names.CHEST_GRAND_GALLERY_40_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "map160-chest2-item1", [EBF5LocationCategory.CHEST]),          # C0(D04) - B03
    location_names.CHEST_GRAND_GALLERY_40_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "map160-chest5-item1", [EBF5LocationCategory.CHEST]),         # C0(D04) - R03
    location_names.CHEST_GRAND_GALLERY_20_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "map159-chest5-item1", [EBF5LocationCategory.CHEST]),          # A0(G03) - D07
    location_names.CHEST_GRAND_GALLERY_20_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "map159-chest2-item1", [EBF5LocationCategory.CHEST]),         # A0(G03) - R07
    location_names.CHEST_GRAND_GALLERY_90_MEDALS_ROOM_LEFT: LocationData(0, "map335-chest0-item0", [EBF5LocationCategory.CHEST]),                       # A0(K03) - O03
    location_names.CHEST_GRAND_GALLERY_90_MEDALS_ROOM_RIGHT: LocationData(0, "map335-chest1-item0", [EBF5LocationCategory.CHEST]),                      # A0(K03) - S03
    location_names.CHEST_GRAND_GALLERY_30_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "map161-chest3-item1", [EBF5LocationCategory.CHEST]),          # A0(Q04) - E08
    location_names.CHEST_GRAND_GALLERY_30_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "map161-chest5-item1", [EBF5LocationCategory.CHEST]),         # A0(Q04) - Q08
    location_names.CHEST_GRAND_GALLERY_70_MEDALS_ROOM_TOP: LocationData(0, "map164-chest4-item0", [EBF5LocationCategory.CHEST]),                        # B0(D04) - B07
    location_names.CHEST_GRAND_GALLERY_70_MEDALS_ROOM_BOTTOM: LocationData(0, "map164-chest3-item0", [EBF5LocationCategory.CHEST]),                     # B0(D04) - B08
    location_names.CHEST_GRAND_GALLERY_60_MEDALS_ROOM_PUZZLE: LocationData(0, "map165-chest4-item1", [EBF5LocationCategory.CHEST]),                     # B0(O04) - S07
    location_names.CHEST_GRAND_GALLERY_60_MEDALS_ROOM_BEHIND_ENEMY: LocationData(0, "map165-chest3-item0", [EBF5LocationCategory.CHEST]),               # B0(O04) - T04
    # NO MAN'S LAND
    location_names.CHEST_NO_MANS_LAND_HARBOR_SECRET: LocationData(0,"map44-chest1-item0", [EBF5LocationCategory.CHEST]),                                # E3 - B09
    location_names.CHEST_NO_MANS_LAND_HARBOR_BEHIND_ENEMY: LocationData(0,"map45-chest2-item0", [EBF5LocationCategory.CHEST]),                          # E4 - Q07
    location_names.CHEST_NO_MANS_LAND_SOUTH_WEST_BEHIND_ENEMY: LocationData(0, "map46-chest1-item0", [EBF5LocationCategory.CHEST]),                     # E5 - C05
    location_names.CHEST_NO_MANS_LAND_SOUTH_ROOM_2_BEHIND_ENEMY: LocationData(0, "map48-chest2-item0", [EBF5LocationCategory.CHEST]),                   # G5 - P03
    location_names.CHEST_NO_MANS_LAND_ARCADE_ROOM_0: LocationData(0, "map323-chest0-item0", [EBF5LocationCategory.CHEST]),                                # H5(D05) - C03
    location_names.CHEST_NO_MANS_LAND_ARCADE_ROOM_2: LocationData(0, "map323-chest0-item2", [EBF5LocationCategory.CHEST]),                                # H5(D05) - C03
    location_names.CHEST_NO_MANS_LAND_EXIT_FORTRESS_LEFT: LocationData(0, "map50-chest3-item0", [EBF5LocationCategory.CHEST]),                          # I5 - J03
    location_names.CHEST_NO_MANS_LAND_EXIT_FORTRESS_MIDDLE: LocationData(0, "map50-chest2-item0", [EBF5LocationCategory.CHEST]),                        # I5 - K02
    location_names.CHEST_NO_MANS_LAND_EXIT_FORTRESS_RIGHT: LocationData(0, "map50-chest1-item0", [EBF5LocationCategory.CHEST]),                         # I5 - Q02
    #   IRON FORTRESS
    location_names.CHEST_IRON_FORTRESS_SUB_ENTRANCE: LocationData(0,"map59-chest1-item1", [EBF5LocationCategory.CHEST]),                                # E3(Q03) - E08
    location_names.CHEST_IRON_FORTRESS_SUB_ENTRANCE_MAGNET: LocationData(0, "map59-chest2-item0", [EBF5LocationCategory.CHEST]),                        # E3(Q03) - K04
    location_names.CHEST_IRON_FORTRESS_SUB_EXIT_BEHIND_ENEMY: LocationData(0, "map51-chest1-item0", [EBF5LocationCategory.CHEST]),                      # F3 - B10
    location_names.CHEST_IRON_FORTRESS_SUB_EXIT_LADDER: LocationData(0, "map51-chest4-item0", [EBF5LocationCategory.CHEST]),                            # F3 - T08
    location_names.CHEST_IRON_FORTRESS_SUB_EXIT_LEO_TOILET: LocationData(0, "map51-chest6-item0", [EBF5LocationCategory.CHEST]),                        # F3 - J02
    location_names.CHEST_IRON_FORTRESS_STORAGE_ROOM_BOTTOM_LEFT: LocationData(0, "map55-chest3-item0", [EBF5LocationCategory.CHEST]),                   # F4 - B09
    location_names.CHEST_IRON_FORTRESS_STORAGE_ROOM_PAINTING: LocationData(0, "map55-chest1-item0", [EBF5LocationCategory.CHEST]),                      # F4 - C01
    location_names.CHEST_IRON_FORTRESS_STORAGE_ROOM_PUZZLE: LocationData(0, "map55-chest4-item0", [EBF5LocationCategory.CHEST]),                        # F4 - R09
    location_names.CHEST_IRON_FORTRESS_MONOLITH: LocationData(0, "map56-chest6-item0", [EBF5LocationCategory.CHEST]),                                   # G4 - I05
    location_names.CHEST_IRON_FORTRESS_MONOLITH_ROOM_BEHIND_TOP_ENEMY: LocationData(0, "map56-chest1-item0", [EBF5LocationCategory.CHEST]),             # G4 - Q02
    location_names.CHEST_IRON_FORTRESS_MONOLITH_ROOM_BEHIND_BOTTOM_ENEMY: LocationData(0, "map56-chest2-item0", [EBF5LocationCategory.CHEST]),          # G4 - S10
    location_names.CHEST_IRON_FORTRESS_MIDBOSS_ROOM_BEHIND_LANCE: LocationData(0, "map52-chest1-item0", [EBF5LocationCategory.CHEST]),                  # G3 - P02
    location_names.CHEST_IRON_FORTRESS_MIDBOSS_ROOM_BEHIND_ENEMY: LocationData(0,"map52-chest2-item0", [EBF5LocationCategory.CHEST]),                   # G3 - R08
    location_names.CHEST_IRON_FORTRESS_NATALIE_ROOM: LocationData(0, "map53-chest3-item1", [EBF5LocationCategory.CHEST]),                               # H3 - H02
    location_names.CHEST_IRON_FORTRESS_LOWER_ARROW_ROOM_ABDUL_CELL: LocationData(0, "map58-chest2-item0", [EBF5LocationCategory.CHEST]),                # I4 - B10
    location_names.CHEST_IRON_FORTRESS_LOWER_ARROW_ROOM_SECRET_STORAGE_LEFT: LocationData(0, "map58-chest3-item0", [EBF5LocationCategory.CHEST]),       # I4 - O02
    location_names.CHEST_IRON_FORTRESS_LOWER_ARROW_ROOM_SECRET_STORAGE_RIGHT: LocationData(0, "map58-chest4-item0", [EBF5LocationCategory.CHEST]),      # I4 - P02
    location_names.CHEST_IRON_FORTRESS_UPPER_ARROW_ROOM: LocationData(0, "map52-chest1-item0", [EBF5LocationCategory.CHEST]),                           # I3 - E06
    #   MINESHAFT MAZE
    location_names.CHEST_MINESHAFT_MAZE_UPPER_LIGHT_PUZZLE_ROOM: LocationData(0, "map208-chest0-item0", [EBF5LocationCategory.CHEST]),                  # I5(F04) | M2(I04) - O05
    location_names.CHEST_MINESHAFT_MAZE_UPPER_LIGHT_PUZZLE_ROOM: LocationData(0, "map208-chest0-item1", [EBF5LocationCategory.CHEST]),                  # I5(F04) | M2(I04) - O05
    location_names.CHEST_MINESHAFT_MAZE_SHOOTING_STAR: LocationData(0, "map207-chest0-item0", [EBF5LocationCategory.CHEST]),                            # I5(F04) | M4 - J05
    location_names.CHEST_MINESHAFT_MAZE_EARTHS_WHISPER: LocationData(0, "map207-chest3-item1", [EBF5LocationCategory.CHEST]),                           # I5(F04) | H7 - J06
    location_names.CHEST_MINESHAFT_MAZE_LOWER_LIGHT_PUZZLE_ROOM_LEFT: LocationData(0, "map210-chest0-item0", [EBF5LocationCategory.CHEST]),             # I5(F04) | M7(L04) - C07
    location_names.CHEST_MINESHAFT_MAZE_LOWER_LIGHT_PUZZLE_ROOM_RIGHT: LocationData(0, "map210-chest1-item0", [EBF5LocationCategory.CHEST]),            # I5(F04) | M7(L04) - R06
    location_names.CHEST_MINESHAFT_MAZE_BOSS_ROOM_BOTTOM: LocationData(0, "map209-chest4-item0", [EBF5LocationCategory.CHEST]),                         # I5(F04) | H9(K06) - D09
    location_names.CHEST_MINESHAFT_MAZE_BOSS_ROOM_LEFT: LocationData(0, "map209-chest3-item0", [EBF5LocationCategory.CHEST]),                           # I5(F04) | H9(K06) - B06
    location_names.CHEST_MINESHAFT_MAZE_BOSS_ROOM_RIGHT: LocationData(0, "map209-chest1-item0", [EBF5LocationCategory.CHEST]),                          # I5(F04) | H9(K06) - R06
    # RAINBOW RIVER
    location_names.CHEST_RAINBOW_RIVER_FORTRESS_SECRET: LocationData(0, "map60-chest2-item0", [EBF5LocationCategory.CHEST]),                            # J5 - C03
    location_names.CHEST_RAINBOW_RIVER_MIDDLE_ISLAND: LocationData(0, "map61-chest4-item0", [EBF5LocationCategory.CHEST]),                              # K5 - C05
    location_names.CHEST_RAINBOW_RIVER_RIGHT_ISLAND_BOTTOM: LocationData(0, "map61-chest1-item0", [EBF5LocationCategory.CHEST]),                        # K5 - N07
    location_names.CHEST_RAINBOW_RIVER_RIGHT_ISLAND_TOP: LocationData(0, "map61-chest0-item0", [EBF5LocationCategory.CHEST]),                           # K5 - S01
    location_names.CHEST_RAINBOW_RIVER_STREAM_10: LocationData(0, "map99-chest7-item1", [EBF5LocationCategory.CHEST]),                                  # K6 - M07
    location_names.CHEST_RAINBOW_RIVER_STREAM_8: LocationData(0, "map97-chest7-item0", [EBF5LocationCategory.CHEST]),                                   # I6 - C11
    location_names.CHEST_RAINBOW_RIVER_STREAM_6: LocationData(0, "map95-chest0-item0", [EBF5LocationCategory.CHEST]),                                   # G6 - C04
    location_names.CHEST_RAINBOW_RIVER_STREAM_5_RIGHT: LocationData(0, "map94-chest3-item0", [EBF5LocationCategory.CHEST]),                             # F6 - Q09
    location_names.CHEST_RAINBOW_RIVER_STREAM_5_BOTTOM: LocationData(0, "map94-chest2-item0", [EBF5LocationCategory.CHEST]),                            # F6 - N11
    location_names.CHEST_RAINBOW_RIVER_STREAM_3: LocationData(0, "map92-chest7-item0", [EBF5LocationCategory.CHEST]),                                   # D6 - N06
    location_names.CHEST_RAINBOW_RIVER_STREAM_2_SECRET: LocationData(0, "map91-chest4-item1", [EBF5LocationCategory.CHEST]),                            # C6 - G04
    location_names.CHEST_RAINBOW_RIVER_STREAM_2_ENEMY: LocationData(0, "map91-chest3-item0", [EBF5LocationCategory.CHEST]),                             # C6 - Q06
    location_names.CHEST_RAINBOW_RIVER_STREAM_1_FROM_VALLEY: LocationData(0, "map90-chest2-item0", [EBF5LocationCategory.CHEST]),                       # B6 - C10
    # GREENWOOD VILLAGE
    location_names.CHEST_GREENWOOD_VILLAGE_FARM: LocationData(0, "map62-chest1-item1", [EBF5LocationCategory.CHEST]),                                   # J4 - H06
    location_names.CHEST_GREENWOOD_VILLAGE_BARN_LEFT: LocationData(0, "map172-chest0-item0", [EBF5LocationCategory.CHEST]),                             # J4(K03) - F05
    location_names.CHEST_GREENWOOD_VILLAGE_BARN_RIGHT: LocationData(0, "map172-chest1-item0", [EBF5LocationCategory.CHEST]),                            # J4(K03) - H05
    location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_HOUSE_LEFT: LocationData(0, "map175-chest1-item0", [EBF5LocationCategory.CHEST]),                     # K4(P03) - B05
    location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_HOUSE_RIGHT: LocationData(0, "map175-chest3-item0", [EBF5LocationCategory.CHEST]),                    # K4(P03) - S03
    location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_BASEMENT_LEFT: LocationData(0, "map176-chest2-item0", [EBF5LocationCategory.CHEST]),                  # K4(P03)(L02) - A07
    location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_BASEMENT_BOTTOM: LocationData(0, "map176-chest0-item0", [EBF5LocationCategory.CHEST]),                # K4(P03)(L02) - M08
    location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_BASEMENT_TOP: LocationData(0, "map176-chest1-item1", [EBF5LocationCategory.CHEST]),                   # K4(P03)(L02) - K02
    location_names.CHEST_GREENWOOD_VILLAGE_BEHIND_RANDYS_HOUSE: LocationData(0, "map65-chest1-item0", [EBF5LocationCategory.CHEST]),                    # K3 - P02
    location_names.CHEST_GREENWOOD_VILLAGE_EQUIPMENT_SHOP_LEFT_DRAWER: LocationData(0, "map169-chest3-item0", [EBF5LocationCategory.CHEST]),            # K3(J04) - G05
    location_names.CHEST_GREENWOOD_VILLAGE_EQUIPMENT_SHOP_RIGHT_DRAWER: LocationData(0, "map169-chest2-item0", [EBF5LocationCategory.CHEST]),           # K3(J04) - H05
    location_names.CHEST_GREENWOOD_VILLAGE_EQUIPMENT_SHOP_SECRET_ROOM: LocationData(0, "map169-chest1-item0", [EBF5LocationCategory.CHEST]),            # K3(J04) - R03
    location_names.CHEST_GREENWOOD_VILLAGE_RANDYS_HOUSE_DRAWER: LocationData(0, "map171-chest1-item1", [EBF5LocationCategory.CHEST]),                   # K3(P06) - N04
    location_names.CHEST_GREENWOOD_VILLAGE_STATUES: LocationData(0, "map67-chest2-item0", [EBF5LocationCategory.CHEST]),                                # K2 - S02
    location_names.CHEST_GREENWOOD_VILLAGE_STATUE_ROOM_SECRET_PATH: LocationData(0, "map67-chest1-item0", [EBF5LocationCategory.CHEST]),                # K2 - B04    
    location_names.CHEST_GREENWOOD_VILLAGE_MATERIALS_SHOP: LocationData(0, "map177-chest0-item1", [EBF5LocationCategory.CHEST]),                        # K2(F08) - L05
    location_names.CHEST_GREENWOOD_VILLAGE_BOSH_ARCADE_LEFT: LocationData(0, "map332-chest0-item0", [EBF5LocationCategory.CHEST]),                      # K2(D05) - G05 
    location_names.CHEST_GREENWOOD_VILLAGE_BOSH_ARCADE_RIGHT: LocationData(0, "map332-chest1-item0", [EBF5LocationCategory.CHEST]),                     # K2(D05) - N05
    location_names.CHEST_GREENWOOD_VILLAGE_OUTSIDE_ANNAS_HOUSE_TARGET: LocationData(0, "map68-chest4-item0", [EBF5LocationCategory.CHEST]),             # J1 - B08
    location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_BRONZE_TOP_LEFT: LocationData(0, "map173-chest0-item0", [EBF5LocationCategory.CHEST]),           # J1(L06) | J1 - F05
    location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_BRONZE_BOTTOM_LEFT: LocationData(0, "map173-chest3-item0", [EBF5LocationCategory.CHEST]),        # J1(L06) | J1 - F08
    location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_BRONZE_BOTTOM_RIGHT: LocationData(0, "map173-chest4-item0", [EBF5LocationCategory.CHEST]),       # J1(L06) | J1 - O08
    location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_DRAWER: LocationData(0, "map173-chest1-item0", [EBF5LocationCategory.CHEST]),                    # J1(L06) | J1 - L02
    location_names.CHEST_GREENWOOD_VILLAGE_BLOCK_PUZZLE: LocationData(0, "map69-chest1-item0", [EBF5LocationCategory.CHEST]),                           # K1 - B01
    location_names.CHEST_GREENWOOD_VILLAGE_EGG_SHRINE: LocationData(0, "map69-chest4-item0", [EBF5LocationCategory.CHEST]),                             # K1 - L06
    location_names.CHEST_GREENWOOD_VILLAGE_ORB_SHRINE_BEHIND_ENEMY: LocationData(0, "map71-chest2-item0", [EBF5LocationCategory.CHEST]),                # K0 - C09
    location_names.CHEST_GREENWOOD_VILLAGE_ORB_SHRINE_ORB_SECRET: LocationData(0, "map71-chest3-item0", [EBF5LocationCategory.CHEST]),                  # K0 - I03
    location_names.CHEST_GREENWOOD_VILLAGE_TOTOM_ARCADE_REWARD: LocationData(0, "map322-chest0-item0", [EBF5LocationCategory.CHEST]),                   # K0(B01) - K07
    location_names.CHEST_GREENWOOD_VILLAGE_TOTOM_ARCADE_LEFT_SECRET: LocationData(0, "map322-chest1-item1", [EBF5LocationCategory.CHEST]),              # K0(B01) - B08
    #   LIBRARY
    location_names.CHEST_LIBRARY_MIDDLE_ROOM_BEHIND_CAT_WIZARD: LocationData(0, "map338-chest1-item0", [EBF5LocationCategory.CHEST]),                   # J3(G06) | J2 - E02
    location_names.CHEST_LIBRARY_MIDDLE_ROOM_BEHIND_PAPER_BOSS_LEFT: LocationData(0, "map338-chest3-item0", [EBF5LocationCategory.CHEST]),              # J3(G06) | J2 - H03
    location_names.CHEST_LIBRARY_MIDDLE_ROOM_BEHIND_PAPER_BOSS_RIGHT: LocationData(0, "map338-chest4-item0", [EBF5LocationCategory.CHEST]),             # J3(G06) | J2 - L03
    location_names.CHEST_LIBRARY_LEFT_ROOM_BEHIND_WISE_MIRROR: LocationData(0, "map337-chest0-item0", [EBF5LocationCategory.CHEST]),                    # J3(G06) | I2 - D08
    location_names.CHEST_LIBRARY_LEFT_ROOM_PAPER_STACK: LocationData(0, "map337-chest3-item0", [EBF5LocationCategory.CHEST]),                           # J3(G06) | I2 - D04
    location_names.CHEST_LIBRARY_RIGHT_ROOM_BOOKSHELF: LocationData(0, "map339-chest2-item1", [EBF5LocationCategory.CHEST]),                            # J3(G06) | K2 - H06
    # MYSTIC WOODS
    location_names.CHEST_MYSTIC_WOODS_I2_TOP_RIGHT: LocationData(0, "map85-chest1-item0", [EBF5LocationCategory.CHEST]),                                # I2 - S03
    location_names.CHEST_MYSTIC_WOODS_H2_SQUID: LocationData(0, "map84-chest1-item0", [EBF5LocationCategory.CHEST]),                                    # H2 - F06
    location_names.CHEST_MYSTIC_WOODS_G2_SLIME: LocationData(0, "map83-chest2-item0", [EBF5LocationCategory.CHEST]),                                    # G2 - B09
    location_names.CHEST_MYSTIC_WOODS_F2_TOP_RIGHT: LocationData(0, "map82-chest1-item0", [EBF5LocationCategory.CHEST]),                                # F2 - R02
    location_names.CHEST_MYSTIC_WOODS_I1_TOP_LEFT_2: LocationData(0, "map80-chest1-item0", [EBF5LocationCategory.CHEST]),                               # I1 - C02
    location_names.CHEST_MYSTIC_WOODS_I1_TOP_HIDDEN: LocationData(0, "map80-chest4-item0", [EBF5LocationCategory.CHEST]),                               # I1 - E01
    location_names.CHEST_MYSTIC_WOODS_H1_PUZZLE: LocationData(0, "map79-chest2-item0", [EBF5LocationCategory.CHEST]),                                   # H1 - F08
    location_names.CHEST_MYSTIC_WOODS_G1_TOP_HIDDEN: LocationData(0, "map78-chest3-item0", [EBF5LocationCategory.CHEST]),                               # G1 - F08
    location_names.CHEST_MYSTIC_WOODS_F1_PUZZLE_RIGHT: LocationData(0, "map77-chest1-item0", [EBF5LocationCategory.CHEST]),                             # F1 - K03
    location_names.CHEST_MYSTIC_WOODS_F1_SECRET_CODE: LocationData(0, "map77-chest5-item0", [EBF5LocationCategory.CHEST]),                              # F1 - P10
    location_names.CHEST_MYSTIC_WOODS_J0_LEAFY_BOOTS: LocationData(0, "map70-chest3-item1", [EBF5LocationCategory.CHEST]),                                    # J0 - R05
    location_names.CHEST_MYSTIC_WOODS_J0_BOTTOM_LEFT: LocationData(0, "map70-chest4-item0", [EBF5LocationCategory.CHEST]),                              # J0 - C10
    location_names.CHEST_MYSTIC_WOODS_G0_TOP_HIDDEN: LocationData(0, "map73-chest0-item0", [EBF5LocationCategory.CHEST]),                               # G0 - M01
    location_names.CHEST_MYSTIC_WOODS_G0_LEFT: LocationData(0, "map73-chest2-item0", [EBF5LocationCategory.CHEST]),                                     # G0 - E08
    location_names.CHEST_MYSTIC_WOODS_F0_STEPLADDER: LocationData(0, "map72-chest0-item1", [EBF5LocationCategory.CHEST]),                               # F0 - D06
    location_names.CHEST_MYSTIC_WOODS_F0_TOP_RIGHT_HIDDEN: LocationData(0, "map72-chest3-item1", [EBF5LocationCategory.CHEST]),                         # F0 - S02
    location_names.CHEST_MYSTIC_WOODS_E2_ABOVE_LAURELIN: LocationData(0, "map81-chest0-item0", [EBF5LocationCategory.CHEST]),                           # E2 - J01
    location_names.CHEST_MYSTIC_WOODS_LEFT_TREE_LOWER_SPIKES: LocationData(0, "map178-chest0-item0", [EBF5LocationCategory.CHEST]),                     # F1(D04) - H02
    location_names.CHEST_MYSTIC_WOODS_LEFT_TREE_UPPER_HIDDEN_LEFT: LocationData(0, "map179-chest2-item0", [EBF5LocationCategory.CHEST]),                # F0(O05) - Q09
    location_names.CHEST_MYSTIC_WOODS_LEFT_TREE_UPPER_HIDDEN_RIGHT: LocationData(0, "map179-chest3-item0", [EBF5LocationCategory.CHEST]),               # F0(O05) - S09
    location_names.CHEST_MYSTIC_WOODS_SHOP_BED: LocationData(0, "chest181-chest3-item0", [EBF5LocationCategory.SECRET]),                                  # H0(E08) - E08



    
}

secrets = {

}

pickups = {

}

def build_location_name_to_id_table():
    # At time of writing, we don't have any secrets or pickups yet so I don't know how they'll be structured.
    # So they aren't included.
    location_datas = list(shop_items.values()) + list(chests.values())

    location_name_to_id = {}
    for i in range(len(location_datas)):
        location_name_to_id[location_datas[i].game_id] = location_datas[i].id
    
    return location_name_to_id