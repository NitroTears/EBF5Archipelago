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

    # Secret World (Undertale)
    location_names.CHEST_AFTER_SNOWFLAKE_LEFT: LocationData(0, "139-0-0", [EBF5LocationCategory.CHEST]),                            # H01
    location_names.CHEST_AFTER_SNOWFLAKE_RIGHT: LocationData(0, "139-1-0", [EBF5LocationCategory.CHEST]),                           # H01
    # HOPE HARBOR / WILD TROPICS    
    location_names.CHEST_OUTSIDE_JERRYS_HOUSE: LocationData(0, "21-2-0", [EBF5LocationCategory.CHEST]),                             # A5 - B06
    location_names.CHEST_MATTS_HOUSE_OTHER_ROOM: LocationData(0, "152-0-0", [EBF5LocationCategory.CHEST]),                          # B5(H05) - R05
    location_names.CHEST_MATTS_HOUSE_LEFT_SOCK_DRAWER: LocationData(0, "152-2-0", [EBF5LocationCategory.SECRET]),                   # B5(H05) - D03
    location_names.CHEST_MATTS_HOUSE_RIGHT_SOCK_DRAWER: LocationData(0, "152-2-0", [EBF5LocationCategory.SECRET]),                  # B5(H05) - F03
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
    location_names.CHEST_WILD_TROPICS_MARKET_BEHIND_HIGHER_PATH: LocationData(0, "33-4-0", [EBF5LocationCategory.CHEST]),           # A2 - O06
    location_names.CHEST_DRAGON_ARMOR_CAVE_BEHIND_ENEMY_LEFT: LocationData(0, "166-0-0", [EBF5LocationCategory.CHEST]),             # C3(G04) - D07
    location_names.CHEST_DRAGON_ARMOR_CAVE_BEHIND_ENEMY_RIGHT: LocationData(0, "166-1-0", [EBF5LocationCategory.CHEST]),            # C3(G04) - R05
    location_names.CHEST_DRAGON_ARMOR_CAVE_CENTER: LocationData(0, "166-3-0", [EBF5LocationCategory.CHEST]),                        # C3(G04) - L06
    location_names.CHEST_INDYS_CAVE_BLOCK_PUZZLE_TOP: LocationData(0, "167-0-0", [EBF5LocationCategory.CHEST]),                     # C3(R07) - R05
    location_names.CHEST_INDYS_CAVE_BLOCK_PUZZLE_BOTTOM: LocationData(0, "167-1-0", [EBF5LocationCategory.CHEST]),                  # C3(R07) - R06
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_1_ENEMY: LocationData(0, "36-1-1", [EBF5LocationCategory.CHEST]),                   # D2 - B02
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_TOP_ENEMY: LocationData(0, "32-4-3", [EBF5LocationCategory.CHEST]),               # D3 - S01
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_BOTTOM_ENEMY: LocationData(0, "32-2-1", [EBF5LocationCategory.CHEST]),            # D3 - S10
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_BEHIND_TENT: LocationData(0, "32-3-2", [EBF5LocationCategory.CHEST]),             # D3 - P04
    location_names.CHEST_HOPE_HARBOR_EAST_COAST_3_BEHIND_ENEMY: LocationData(0, "28-3-3", [EBF5LocationCategory.CHEST]),            # D4 - M10
    location_names.CHEST_HOPE_HARBOR_OUTSIDE_ICE_CAVE_LEFT: LocationData(0, "24-2-3", [EBF5LocationCategory.CHEST]),                # D5 - M07
    location_names.CHEST_HOPE_HARBOR_OUTSIDE_ICE_CAVE_MIDDLE: LocationData(0, "24-3-4", [EBF5LocationCategory.CHEST]),              # D5 - N08
    location_names.CHEST_HOPE_HARBOR_BEHIND_ICE_CAVE: LocationData(0, "24-0-1", [EBF5LocationCategory.CHEST]),                      # D5 - R02
    #   ICE CAVE
    location_names.CHEST_ICE_CAVE_ROOM_2_BEHIND_ENEMY: LocationData(0, "19-1-2", [EBF5LocationCategory.CHEST]),                     # D5(P06) | D4 - K09
    location_names.CHEST_ICE_CAVE_ROOM_3_BEHIND_ENEMY: LocationData(0, "20-1-2", [EBF5LocationCategory.CHEST]),                     # D5(P06) | E3 - S03
    #       FREEZEFLAME DUNGEON
    location_names.CHEST_FREEZEFLAME_DUNGEON_BEHIND_ENEMY_LEFT: LocationData(0, "201-1-0", [EBF5LocationCategory.CHEST]),           # D5(P06) | E2 - D03
    location_names.CHEST_FREEZEFLAME_DUNGEON_BEHIND_ENEMY_RIGHT: LocationData(0, "201-3-2", [EBF5LocationCategory.CHEST]),          # D5(P06) | E2 - M08
    location_names.CHEST_FREEZEFLAME_DUNGEON_ICE_BLOCK_PUZZLE_ROOM: LocationData(0, "200-2-2", [EBF5LocationCategory.CHEST]),       # D5(P06) | D2 - B04
    location_names.CHEST_FREEZEFLAME_DUNGEON_ICE_SLIDE_PUZZLE_ROOM: LocationData(0, "203-1-1", [EBF5LocationCategory.CHEST]),       # D5(P06) | D1 - B06
    location_names.CHEST_FREEZEFLAME_DUNGEON_FIRE_BLOCK_PUZZLE_ROOM: LocationData(0, "202-2-2", [EBF5LocationCategory.CHEST]),      # D5(P06) | F2 - Q06
    location_names.CHEST_FREEZEFLAME_DUNGEON_FIRE_COMBAT_ROOM_LAST: LocationData(0, "205-1-1", [EBF5LocationCategory.CHEST]),       # D5(P06) | F1 - R06
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_ICE_TOP: LocationData(0, "206-0-0", [EBF5LocationCategory.CHEST]),           # D5(P06) | E0 - D02
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_TOP: LocationData(0, "206-1-1", [EBF5LocationCategory.CHEST]),          # D5(P06) | E0 - P02
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_MIDDLE: LocationData(0, "206-3-3", [EBF5LocationCategory.CHEST]),       # D5(P06) | E0 - R03
    location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_BOTTOM: LocationData(0, "206-4-4", [EBF5LocationCategory.CHEST]),       # D5(P06) | E0 - Q05
    #   GRAND GALLERY
    location_names.CHEST_GRAND_GALLERY_ENTRANCE: LocationData (0, "38-2-3", [EBF5LocationCategory.CHEST]),                          # B1 - Q08
    location_names.CHEST_GRAND_GALLERY_LEFT_HALL: LocationData(0, "40-0-0", [EBF5LocationCategory.CHEST]),                          # A0 - L05
    location_names.CHEST_GRAND_GALLERY_LEFT_TOP_KEY: LocationData(0, "40-1-1", [EBF5LocationCategory.CHEST]),                       # A0 - B05
    location_names.CHEST_GRAND_GALLERY_LEFT_MIDDLE_KEY: LocationData(0, "40-2-2", [EBF5LocationCategory.CHEST]),                    # A0 - B06
    location_names.CHEST_GRAND_GALLERY_LEFT_BOTTOM_KEY: LocationData(0, "40-3-3", [EBF5LocationCategory.CHEST]),                    # A0 - B07
    location_names.CHEST_GRAND_GALLERY_LEFT_MAZE_RIGHT: LocationData(0, "37-2-1", [EBF5LocationCategory.CHEST]),                    # A1 - P10 
    location_names.CHEST_GRAND_GALLERY_LEFT_MAZE_LEFT: LocationData(0, "37-4-4", [EBF5LocationCategory.CHEST]),                     # A1 - C08
    location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_BEHIND_ENEMY_LEFT: LocationData(0, "39-1-2", [EBF5LocationCategory.CHEST]),       # C1 - G10
    location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_ANGEL_STATUE_LEFT: LocationData(0, "39-4-4", [EBF5LocationCategory.CHEST]),       # C1 - K08
    location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_ANGEL_STATUE_RIGHT: LocationData(0, "39-5-5", [EBF5LocationCategory.CHEST]),      # C1 - M08
    location_names.CHEST_GRAND_GALLERY_RIGHT_TOP_KEY: LocationData(0, "42-1-1", [EBF5LocationCategory.CHEST]),                      # C0 - S05
    location_names.CHEST_GRAND_GALLERY_RIGHT_MIDDLE_KEY: LocationData(0, "42-2-2", [EBF5LocationCategory.CHEST]),                   # C0 - S06
    location_names.CHEST_GRAND_GALLERY_RIGHT_BOTTOM_KEY: LocationData(0, "42-3-3", [EBF5LocationCategory.CHEST]),                   # C0 - S07
    location_names.CHEST_GRAND_GALLERY_80_MEDALS_ROOM: LocationData(0, "336-0-0", [EBF5LocationCategory.CHEST]),                    # C0(R03) - G06
    location_names.CHEST_GRAND_GALLERY_50_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "162-2-2", [EBF5LocationCategory.CHEST]),  # C0(N03) - F04
    location_names.CHEST_GRAND_GALLERY_50_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "162-5-5", [EBF5LocationCategory.CHEST]), # C0(N03) - R04
    location_names.CHEST_GRAND_GALLERY_40_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "160-2-2", [EBF5LocationCategory.CHEST]),  # C0(D04) - B03
    location_names.CHEST_GRAND_GALLERY_40_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "160-5-5", [EBF5LocationCategory.CHEST]), # C0(D04) - R03
    location_names.CHEST_GRAND_GALLERY_20_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "159-5-5", [EBF5LocationCategory.CHEST]),  # A0(G03) - D07
    location_names.CHEST_GRAND_GALLERY_20_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "159-2-2", [EBF5LocationCategory.CHEST]), # A0(G03) - R07
    location_names.CHEST_GRAND_GALLERY_90_MEDALS_ROOM_LEFT: LocationData(0, "335-0-0", [EBF5LocationCategory.CHEST]),               # A0(K03) - O03
    location_names.CHEST_GRAND_GALLERY_90_MEDALS_ROOM_RIGHT: LocationData(0, "335-1-1", [EBF5LocationCategory.CHEST]),              # A0(K03) - S03
    location_names.CHEST_GRAND_GALLERY_30_MEDALS_ROOM_BEHIND_LEFT_ENEMY: LocationData(0, "161-3-3", [EBF5LocationCategory.CHEST]),  # A0(Q04) - E08
    location_names.CHEST_GRAND_GALLERY_30_MEDALS_ROOM_BEHIND_RIGHT_ENEMY: LocationData(0, "161-5-5", [EBF5LocationCategory.CHEST]), # A0(Q04) - Q08
    location_names.CHEST_GRAND_GALLERY_70_MEDALS_ROOM_TOP: LocationData(0, "164-4-4", [EBF5LocationCategory.CHEST]),                # B0(D04) - B07
    location_names.CHEST_GRAND_GALLERY_70_MEDALS_ROOM_BOTTOM: LocationData(0, "164-3-3", [EBF5LocationCategory.CHEST]),             # B0(D04) - B08
    location_names.CHEST_GRAND_GALLERY_60_MEDALS_ROOM_PUZZLE: LocationData(0, "165-4-4", [EBF5LocationCategory.CHEST]),             # B0(O04) - S07
    location_names.CHEST_GRAND_GALLERY_60_MEDALS_ROOM_BEHIND_ENEMY: LocationData(0, "165-1-3", [EBF5LocationCategory.CHEST]),       # B0(O04) - T04
    
    
}

secrets = {

}

pickups = {

}
