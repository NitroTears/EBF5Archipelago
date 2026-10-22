from typing import Dict, List, NamedTuple, Optional, Tuple

from BaseClasses import Region
from rule_builder.rules import CanReachRegion, Has, Rule
from worlds.ebf5.Locations import EBF5Location
from worlds.ebf5.static_names import location_names
from worlds.ebf5 import Locations


class EBF5RegionData(NamedTuple):
    locations: List[str]
    region_exits: Optional[List[str]]


MENU_REGION = 'Menu'
START_REGION = "B5 Matt's House"


region_data: Dict[str, EBF5RegionData] = {
    'A0 20 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_20_MEDALS_ROOM_BEHIND_LEFT_ENEMY,
            location_names.CHEST_GRAND_GALLERY_20_MEDALS_ROOM_BEHIND_RIGHT_ENEMY,
        ],
        None,
    ),
    'A0 30 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_30_MEDALS_ROOM_BEHIND_LEFT_ENEMY,
            location_names.CHEST_GRAND_GALLERY_30_MEDALS_ROOM_BEHIND_RIGHT_ENEMY,
        ],
        None,
    ),
    'A0 90 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_90_MEDALS_ROOM_LEFT,
            location_names.CHEST_GRAND_GALLERY_90_MEDALS_ROOM_RIGHT,
        ],
        None,
    ),
    'A0 Grand Gallery': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_LEFT_BOTTOM_KEY,
            location_names.CHEST_GRAND_GALLERY_LEFT_HALL,
            location_names.CHEST_GRAND_GALLERY_LEFT_MIDDLE_KEY,
            location_names.CHEST_GRAND_GALLERY_LEFT_TOP_KEY,
        ],
        [
            'A0 20 Medals Room',
            'A0 30 Medals Room',
            'A0 90 Medals Room',
            'A1 Grand Gallery',
            'A1 Grand Gallery E',
            'B0 Grand Gallery',
        ],
    ),
    'A1 Grand Gallery': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_LEFT_MAZE_LEFT,
        ],
        [
            'A1 Grand Gallery E',
        ],
    ),
    'A1 Grand Gallery E': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_LEFT_MAZE_RIGHT,
        ],
        None,
    ),
    'A2 Hope Harbor': EBF5RegionData(
        [],
        [
            'A3 Wild Tropics',
            'B2 Hope Harbor',
        ],
    ),
    'A3 Wild Tropics': EBF5RegionData(
        [],
        [
            'A2 Hope Harbor',
            'A4 Wild Tropics',
            'B3 Wild Tropics',
        ],
    ),
    'A4 Wild Tropics': EBF5RegionData(
        [],
        [
            'A3 Wild Tropics',
            'A5 Hope Harbor',
            'B4 Wild Tropics',
        ],
    ),
    'A5 Hope Harbor': EBF5RegionData(
        [],
        [
            'A4 Wild Tropics',
            "A5 Jerry's House",
            'B5 Hope Harbor',
        ],
    ),
    "A5 Jerry's Cellar": EBF5RegionData(
        [],
        [
            "A5 Jerry's House",
        ],
    ),
    "A5 Jerry's House": EBF5RegionData(
        [],
        [
            "A5 Jerry's Cellar",
        ],
    ),
    'A6 Frozen Valley': EBF5RegionData(
        [],
        [
            'A7 Frozen Valley E',
        ],
    ),
    'A7 Frozen Valley E': EBF5RegionData(
        [],
        [
            'A6 Frozen Valley',
            'A7 Frozen Valley Water',
            'B7 Frozen Valley',
        ],
    ),
    'A7 Frozen Valley SW': EBF5RegionData(
        [],
        [
            'A7 Frozen Valley Water',
            'A8 Frozen Valley',
        ],
    ),
    'A7 Frozen Valley Water': EBF5RegionData(
        [],
        [
            'A7 Frozen Valley E',
            'A7 Frozen Valley SW',
        ],
    ),
    'A8 Arcade Room': EBF5RegionData(
        [],
        [
            'A8 Hidden Passage',
        ],
    ),
    'A8 Frozen Valley': EBF5RegionData(
        [],
        [
            'A7 Frozen Valley SW',
            'A8 Hidden Passage',
            'A9 Frozen Valley',
            'B8 Frozen Valley',
        ],
    ),
    'A8 Hidden Passage': EBF5RegionData(
        [],
        [
            'A8 Arcade Room',
        ],
    ),
    'A9 Frozen Valley': EBF5RegionData(
        [],
        [
            'A8 Frozen Valley',
            'B9 Frozen Valley',
        ],
    ),
    'B0 60 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_60_MEDALS_ROOM_BEHIND_ENEMY,
            location_names.CHEST_GRAND_GALLERY_60_MEDALS_ROOM_PUZZLE,
        ],
        None,
    ),
    'B0 70 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_70_MEDALS_ROOM_BOTTOM,
            location_names.CHEST_GRAND_GALLERY_70_MEDALS_ROOM_TOP,
        ],
        None,
    ),
    'B0 All Medals Room': EBF5RegionData(
        [],
        [
            'B0 Grand Gallery',
        ],
    ),
    'B0 Grand Gallery': EBF5RegionData(
        [],
        [
            'A0 Grand Gallery',
            'B0 60 Medals Room',
            'B0 70 Medals Room',
            'B0 All Medals Room',
            'B1 Grand Gallery',
            'C0 Grand Gallery',
        ],
    ),
    'B1 Grand Gallery': EBF5RegionData(
        [],
        [
            'B0 Grand Gallery',
            'B2 Hope Harbor',
        ],
    ),
    'B2 Glitch Area': EBF5RegionData(
        [],
        None,
    ),
    'B2 Hope Harbor': EBF5RegionData(
        [],
        [
            'A2 Hope Harbor',
            'B1 Grand Gallery',
            'B2 Glitch Area',
            'B3 Wild Tropics',
            'C2 Hope Harbor',
        ],
    ),
    'B3 Arcade Room': EBF5RegionData(
        [],
        [
            'C3 Wild Tropics',
        ],
    ),
    'B3 Deathly Hollows': EBF5RegionData(
        [],
        [
            'C3 Deathly Hollows',
        ],
    ),
    'B3 Wild Tropics': EBF5RegionData(
        [],
        [
            'A3 Wild Tropics',
            'B2 Hope Harbor',
            'B4 Wild Tropics',
            'C3 Wild Tropics',
        ],
    ),
    'B4 Deathly Hollows': EBF5RegionData(
        [],
        [
            'C3 Deathly Hollows',
        ],
    ),
    'B4 Wild Tropics': EBF5RegionData(
        [
            location_names.CHEST_WILD_TROPICS_ENTERANCE,
        ],
        [
            'A4 Wild Tropics',
            'B3 Wild Tropics',
            'B5 Hope Harbor',
            'C4 Hope Harbor',
        ],
    ),
    'B5 Hope Harbor': EBF5RegionData(
        [],
        [
            'A5 Hope Harbor',
            'B4 Wild Tropics',
            'B5 Hope Harbor Water',
            "B5 Matt's House",
            'C5 Hope Harbor',
        ],
    ),
    'B5 Hope Harbor Water': EBF5RegionData(
        [],
        [
            'B5 Hope Harbor',
            'C5 Hope Harbor Water',
        ],
    ),
    "B5 Matt's House": EBF5RegionData(
        [
            location_names.CHEST_MATTS_HOUSE_LEFT_SOCK_DRAWER,
            location_names.CHEST_MATTS_HOUSE_OLD_BOOTS,
            location_names.CHEST_MATTS_HOUSE_OTHER_ROOM,
            location_names.CHEST_MATTS_HOUSE_RIGHT_SOCK_DRAWER,
            location_names.CHEST_MATTS_HOUSE_SCOUTER,
        ],
        [
            'B5 Hope Harbor',
        ],
    ),
    'B6 Rainbow River': EBF5RegionData(
        [],
        [
            'B5 Hope Harbor Water',
            'B6 Rainbow River Land',
            'C6 Rainbow River',
        ],
    ),
    'B6 Rainbow River Land': EBF5RegionData(
        [],
        [
            'B6 Rainbow River',
            'C6 Rainbow River Land',
        ],
    ),
    'B7 Frozen Valley': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_STREAM_1_FROM_VALLEY,
        ],
        [
            'A7 Frozen Valley E',
            'B8 Frozen Valley',
        ],
    ),
    'B8 Frozen Valley': EBF5RegionData(
        [],
        [
            'A8 Frozen Valley',
            'B7 Frozen Valley',
            'B9 Frozen Valley',
            'C8 Frozen Valley',
        ],
    ),
    'B9 Frozen Valley': EBF5RegionData(
        [],
        [
            'A9 Frozen Valley',
            'B8 Frozen Valley',
            'B9 Glitch Area',
            'C9 Frozen Valley',
        ],
    ),
    'B9 Glitch Area': EBF5RegionData(
        [],
        None,
    ),
    'C0 40 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_40_MEDALS_ROOM_BEHIND_LEFT_ENEMY,
            location_names.CHEST_GRAND_GALLERY_40_MEDALS_ROOM_BEHIND_RIGHT_ENEMY,
        ],
        None,
    ),
    'C0 50 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_50_MEDALS_ROOM_BEHIND_LEFT_ENEMY,
            location_names.CHEST_GRAND_GALLERY_50_MEDALS_ROOM_BEHIND_RIGHT_ENEMY,
        ],
        None,
    ),
    'C0 80 Medals Room': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_80_MEDALS_ROOM,
        ],
        None,
    ),
    'C0 Grand Gallery': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_RIGHT_BOTTOM_KEY,
            location_names.CHEST_GRAND_GALLERY_RIGHT_MIDDLE_KEY,
            location_names.CHEST_GRAND_GALLERY_RIGHT_TOP_KEY,
        ],
        [
            'B0 Grand Gallery',
            'C0 40 Medals Room',
            'C0 50 Medals Room',
            'C0 80 Medals Room',
            'C1 Grand Gallery E',
            'C1 Grand Gallery W',
        ],
    ),
    'C1 Grand Gallery E': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_ANGEL_STATUE_LEFT,
            location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_ANGEL_STATUE_RIGHT,
        ],
        None,
    ),
    'C1 Grand Gallery W': EBF5RegionData(
        [
            location_names.CHEST_GRAND_GALLERY_ENTRANCE,
            location_names.CHEST_GRAND_GALLERY_RIGHT_MAZE_BEHIND_ENEMY_LEFT,
        ],
        [
            'C2 Hope Harbor',
        ],
    ),
    'C11 The Great Sea': EBF5RegionData(
        [],
        [
            'C12 The Great Sea',
            'D11 The Great Sea',
        ],
    ),
    'C12 The Great Sea': EBF5RegionData(
        [],
        [
            'C11 The Great Sea',
            'D12 The Great Sea',
        ],
    ),
    'C13 Data Bunker': EBF5RegionData(
        [],
        [
            'C14 Data Bunker',
        ],
    ),
    'C14 Data Bunker': EBF5RegionData(
        [],
        [
            'C13 Data Bunker',
            'C15 Data Bunker',
        ],
    ),
    'C15 Data Bunker': EBF5RegionData(
        [],
        [
            'C14 Data Bunker',
        ],
    ),
    'C15 The Great Sea': EBF5RegionData(
        [],
        [
            'C15 Data Bunker',
            'D15 The Great Sea',
        ],
    ),
    'C2 Arcade Room': EBF5RegionData(
        [],
        [
            'C2 Hope Harbor',
        ],
    ),
    'C2 Basement': EBF5RegionData(
        [],
        [
            'C2 Equipment Shop Back',
        ],
    ),
    'C2 Deathly Hollows': EBF5RegionData(
        [],
        [
            'C3 Deathly Hollows',
        ],
    ),
    'C2 Equipment Shop': EBF5RegionData(
        [],
        [
            'C2 Hope Harbor',
            'C2 Kitchen',
        ],
    ),
    'C2 Equipment Shop Back': EBF5RegionData(
        [],
        [
            'C2 Basement',
            'C2 Hope Harbor',
        ],
    ),
    'C2 Hope Harbor': EBF5RegionData(
        [],
        [
            'B2 Hope Harbor',
            'C1 Grand Gallery W',
            'C2 Arcade Room',
            'C2 Equipment Shop',
            'C2 Equipment Shop Back',
            'C2 Kitchen',
            'C3 Wild Tropics',
            'D2 Hope Harbor W',
        ],
    ),
    'C2 Kitchen': EBF5RegionData(
        [],
        [
            'C2 Equipment Shop',
        ],
    ),
    'C3 Deathly Hollows': EBF5RegionData(
        [],
        [
            'B3 Deathly Hollows',
            'B4 Deathly Hollows',
            'C2 Deathly Hollows',
            'C4 Deathly Hollows',
            'D2 Deathly Hollows',
            'D3 Deathly Hollows',
        ],
    ),
    'C3 Dragon Armor Cave': EBF5RegionData(
        [
            location_names.CHEST_DRAGON_ARMOR_CAVE_BEHIND_ENEMY_LEFT,
        ],
        [
            'C3 Wild Tropics',
        ],
    ),
    "C3 Indy's Cave": EBF5RegionData(
        [],
        None,
    ),
    'C3 Wild Tropics': EBF5RegionData(
        [],
        [
            'B3 Arcade Room',
            'B3 Wild Tropics',
            'C2 Hope Harbor',
            'C3 Dragon Armor Cave',
            "C3 Indy's Cave",
            'D3 Hope Harbor',
        ],
    ),
    'C4 Deathly Hollows': EBF5RegionData(
        [],
        [
            'C3 Deathly Hollows',
        ],
    ),
    'C4 Food Shop': EBF5RegionData(
        [],
        [
            'C4 Food Shop 1st Floor',
        ],
    ),
    'C4 Food Shop 1st Floor': EBF5RegionData(
        [],
        None,
    ),
    'C4 Hope Harbor': EBF5RegionData(
        [],
        [
            'B4 Wild Tropics',
            'C4 Food Shop',
            'C4 Material Shop',
            'C5 Hope Harbor',
        ],
    ),
    'C4 Material Shop': EBF5RegionData(
        [],
        [
            'C4 Hope Harbor',
        ],
    ),
    'C5 Hope Harbor': EBF5RegionData(
        [],
        [
            'B5 Hope Harbor',
            'C4 Hope Harbor',
            'C5 Hope Harbor Water',
        ],
    ),
    'C5 Hope Harbor Water': EBF5RegionData(
        [],
        [
            'B5 Hope Harbor Water',
            'C5 Hope Harbor',
            'D5 Hope Harbor Water',
        ],
    ),
    'C6 Rainbow River': EBF5RegionData(
        [],
        [
            'B6 Rainbow River',
            'C6 Rainbow River Land',
            'D6 Rainbow River',
        ],
    ),
    'C6 Rainbow River Land': EBF5RegionData(
        [],
        [
            'B6 Rainbow River Land',
            'C6 Rainbow River',
            'C7 Frozen Valley',
            'C7 Frozen Valley Ice',
        ],
    ),
    'C7 Frozen Valley': EBF5RegionData(
        [],
        [
            'C7 Frozen Valley Ice',
            'C8 Frozen Valley',
        ],
    ),
    'C7 Frozen Valley Ice': EBF5RegionData(
        [],
        [
            'C6 Rainbow River Land',
            'C7 Frozen Valley',
        ],
    ),
    'C8 Frozen Valley': EBF5RegionData(
        [],
        [
            'B8 Frozen Valley',
            'C7 Frozen Valley',
            'C9 Frozen Valley',
        ],
    ),
    'C9 Frozen Valley': EBF5RegionData(
        [],
        [
            'B9 Frozen Valley',
            'C8 Frozen Valley',
            'C9 Frozen Valley Water',
        ],
    ),
    'C9 Frozen Valley Water': EBF5RegionData(
        [],
        [
            'C9 Frozen Valley',
            'D9 Redpine Town Water',
        ],
    ),
    'D0 Crystal Caverns': EBF5RegionData(
        [],
        [
            'D1 Crystal Caverns',
            'E0 Crystal Caverns',
        ],
    ),
    'D0 Forgotten Ruins': EBF5RegionData(
        [],
        [
            'D1 Forgotten Ruins NW',
            'E0 Forgotten Ruins W',
        ],
    ),
    'D1 Crystal Caverns': EBF5RegionData(
        [],
        [
            'D0 Crystal Caverns',
        ],
    ),
    'D1 Forgotten Ruins': EBF5RegionData(
        [],
        [
            'D1 Forgotten Ruins NW',
            'D2 Hope Harbor E',
            'E1 Forgotten Ruins S',
        ],
    ),
    'D1 Forgotten Ruins NW': EBF5RegionData(
        [],
        [
            'D0 Forgotten Ruins',
            'D1 Forgotten Ruins',
        ],
    ),
    'D1 Freezeflame Dungeon': EBF5RegionData(
        [
            location_names.CHEST_FREEZEFLAME_DUNGEON_ICE_SLIDE_PUZZLE_ROOM,
        ],
        [
            'D2 Freezeflame Dungeon',
            'E1 Freezeflame Dungeon W',
        ],
    ),
    'D10 The Great Sea': EBF5RegionData(
        [],
        [
            'D11 The Great Sea',
            'D9 Redpine Town Water',
        ],
    ),
    'D11 The Great Sea': EBF5RegionData(
        [],
        [
            'C11 The Great Sea',
            'D10 The Great Sea',
        ],
    ),
    'D12 The Great Sea': EBF5RegionData(
        [],
        [
            'C12 The Great Sea',
            'E12 The Great Sea',
        ],
    ),
    'D13 The Great Sea': EBF5RegionData(
        [],
        [
            'D14 The Great Sea',
            'E13 The Great Sea',
        ],
    ),
    'D14 Arcade Room': EBF5RegionData(
        [],
        [
            'D14 The Great Sea Island',
        ],
    ),
    'D14 The Great Sea': EBF5RegionData(
        [],
        [
            'D13 The Great Sea',
            'D14 The Great Sea Island',
            'D15 The Great Sea',
        ],
    ),
    'D14 The Great Sea Island': EBF5RegionData(
        [],
        [
            'D14 Arcade Room',
            'D14 The Great Sea',
        ],
    ),
    'D15 The Great Sea': EBF5RegionData(
        [],
        [
            'C15 The Great Sea',
            'D14 The Great Sea',
            'D15 The Great Sea Island',
            'E15 The Great Sea',
        ],
    ),
    'D15 The Great Sea Island': EBF5RegionData(
        [],
        [
            'D15 The Great Sea',
        ],
    ),
    'D2 Deathly Hollows': EBF5RegionData(
        [],
        [
            'C3 Deathly Hollows',
        ],
    ),
    'D2 Deathly Hollows Start': EBF5RegionData(
        [],
        [
            'D2 Deathly Hollows',
            'D2 Hope Harbor E',
        ],
    ),
    'D2 Freezeflame Dungeon': EBF5RegionData(
        [
            location_names.CHEST_FREEZEFLAME_DUNGEON_ICE_BLOCK_PUZZLE_ROOM,
        ],
        [
            'D1 Freezeflame Dungeon',
            'E2 Freezeflame Dungeon',
        ],
    ),
    'D2 Hope Harbor E': EBF5RegionData(
        [],
        [
            'D1 Forgotten Ruins',
            'D2 Deathly Hollows Start',
            'D2 Hope Harbor Water',
            'E2 Mystic Woods W',
        ],
    ),
    'D2 Hope Harbor W': EBF5RegionData(
        [
            location_names.CHEST_HOPE_HARBOR_EAST_COAST_1_ENEMY,
        ],
        [
            'C2 Hope Harbor',
            'D2 Hope Harbor Water',
            'D3 Hope Harbor',
        ],
    ),
    'D2 Hope Harbor Water': EBF5RegionData(
        [],
        [
            'D2 Hope Harbor E',
            'D2 Hope Harbor W',
        ],
    ),
    'D3 Deathly Hollows': EBF5RegionData(
        [],
        [
            'C3 Deathly Hollows',
        ],
    ),
    'D3 Hope Harbor': EBF5RegionData(
        [
            location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_BEHIND_TENT,
            location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_BOTTOM_ENEMY,
            location_names.CHEST_HOPE_HARBOR_EAST_COAST_2_TOP_ENEMY,
        ],
        [
            'C3 Wild Tropics',
            'D2 Hope Harbor W',
            'D4 Hope Harbor',
        ],
    ),
    'D4 Hope Harbor': EBF5RegionData(
        [],
        [
            'C4 Hope Harbor',
            'D3 Hope Harbor',
            'D4 Hope Harbor Water',
            'D5 Hope Harbor',
            "E4 No Man's Land NW",
        ],
    ),
    'D4 Hope Harbor Cave Chest': EBF5RegionData(
        [
            location_names.CHEST_HOPE_HARBOR_EAST_COAST_3_BEHIND_ENEMY,
        ],
        [
            'D4 Ice Cave',
        ],
    ),
    'D4 Hope Harbor Water': EBF5RegionData(
        [],
        [
            'D4 Hope Harbor',
            "E4 No Man's Land Water",
        ],
    ),
    'D4 Ice Cave': EBF5RegionData(
        [
            location_names.CHEST_ICE_CAVE_ROOM_2_BEHIND_ENEMY,
        ],
        [
            'D4 Hope Harbor Cave Chest',
            'D5 Ice Cave',
            'E3 Ice Cave',
        ],
    ),
    'D5 Hope Harbor': EBF5RegionData(
        [
            location_names.CHEST_HOPE_HARBOR_BEHIND_ICE_CAVE,
        ],
        [
            'D4 Hope Harbor',
            'D5 Hope Harbor Cave Entrance',
            'D5 Hope Harbor Water',
        ],
    ),
    'D5 Hope Harbor Cave Entrance': EBF5RegionData(
        [
            location_names.CHEST_HOPE_HARBOR_OUTSIDE_ICE_CAVE_LEFT,
            location_names.CHEST_HOPE_HARBOR_OUTSIDE_ICE_CAVE_MIDDLE,
        ],
        [
            'D5 Hope Harbor',
            'D5 Ice Cave',
        ],
    ),
    'D5 Hope Harbor Water': EBF5RegionData(
        [],
        [
            'C5 Hope Harbor Water',
            'D5 Hope Harbor',
            'D6 Rainbow River',
            "E5 No Man's Land Water",
        ],
    ),
    'D5 Ice Cave': EBF5RegionData(
        [],
        [
            'D4 Ice Cave',
            'D5 Hope Harbor Cave Entrance',
        ],
    ),
    'D6 Rainbow River': EBF5RegionData(
        [],
        [
            'C6 Rainbow River',
            'D5 Hope Harbor Water',
            'D6 Rainbow River S',
            'E6 Rainbow River',
        ],
    ),
    'D6 Rainbow River S': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_STREAM_3,
        ],
        [
            'D6 Rainbow River',
            'D7 Redpine Town',
        ],
    ),
    'D7 Food Shop': EBF5RegionData(
        [],
        None,
    ),
    'D7 Redpine Town': EBF5RegionData(
        [],
        [
            'C7 Frozen Valley Ice',
            'D6 Rainbow River S',
            'D7 Food Shop',
            'D7 Steroid Shop',
            'D8 Redpine Town',
            'E7 Redpine Town',
        ],
    ),
    'D7 Steroid Shop': EBF5RegionData(
        [],
        [
            'D7 Redpine Town',
        ],
    ),
    'D7 The Void': EBF5RegionData(
        [],
        [
            'D8 The Void',
        ],
    ),
    'D8 Equipment Shop': EBF5RegionData(
        [],
        [
            'D8 Redpine Town',
        ],
    ),
    'D8 Redpine Town': EBF5RegionData(
        [],
        [
            'D7 Redpine Town',
            'D8 Equipment Shop',
            'D8 The Void',
            'D9 Redpine Town',
            'E8 Redpine Town',
        ],
    ),
    'D8 The Void': EBF5RegionData(
        [],
        [
            'D7 The Void',
        ],
    ),
    'D9 Redpine Town': EBF5RegionData(
        [],
        [
            'D8 Redpine Town',
            'D9 Redpine Town Water',
            'E9 Redpine Town',
        ],
    ),
    'D9 Redpine Town Water': EBF5RegionData(
        [],
        [
            'C9 Frozen Valley Water',
            'D10 The Great Sea',
            'D9 Redpine Town',
        ],
    ),
    'E0 Crystal Caverns': EBF5RegionData(
        [],
        [
            'D0 Crystal Caverns',
            'E9 Crystal Caverns',
        ],
    ),
    'E0 Forgotten Ruins E': EBF5RegionData(
        [],
        [
            'E0 Forgotten Temple',
            'E1 Forgotten Ruins NE',
        ],
    ),
    'E0 Forgotten Ruins W': EBF5RegionData(
        [],
        [
            'D0 Forgotten Ruins',
            'E1 Forgotten Ruins NW',
        ],
    ),
    'E0 Forgotten Temple': EBF5RegionData(
        [],
        [
            'E0 Forgotten Ruins E',
            'E1 Secret World',
        ],
    ),
    'E0 Freezeflame Dungeon': EBF5RegionData(
        [
            location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_BOTTOM,
            location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_MIDDLE,
            location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_FIRE_TOP,
            location_names.CHEST_FREEZEFLAME_DUNGEON_BOSS_ROOM_ICE_TOP,
        ],
        [
            'E1 Freezeflame Dungeon',
        ],
    ),
    'E0 Secret World': EBF5RegionData(
        [
            location_names.CHEST_AFTER_SNOWFLAKE_LEFT,
        ],
        [
            'E1 Secret World',
        ],
    ),
    'E1 Forgotten Ruins NE': EBF5RegionData(
        [],
        [
            'E0 Forgotten Ruins E',
            'E1 Forgotten Ruins NW',
        ],
    ),
    'E1 Forgotten Ruins NW': EBF5RegionData(
        [],
        [
            'D1 Forgotten Ruins',
            'E0 Forgotten Ruins W',
            'E1 Forgotten Ruins NE',
        ],
    ),
    'E1 Forgotten Ruins S': EBF5RegionData(
        [],
        [
            'D1 Forgotten Ruins',
        ],
    ),
    'E1 Freezeflame Dungeon': EBF5RegionData(
        [],
        [
            'E0 Freezeflame Dungeon',
            'E2 Freezeflame Dungeon',
        ],
    ),
    'E1 Freezeflame Dungeon E': EBF5RegionData(
        [],
        [
            'F1 Freezeflame Dungeon',
        ],
    ),
    'E1 Freezeflame Dungeon W': EBF5RegionData(
        [],
        [
            'D1 Freezeflame Dungeon',
        ],
    ),
    'E1 Secret World': EBF5RegionData(
        [],
        [
            'E0 Forgotten Temple',
            'E0 Secret World',
        ],
    ),
    'E11 The Great Sea': EBF5RegionData(
        [],
        [
            'E12 The Great Sea',
        ],
    ),
    'E12 The Great Sea': EBF5RegionData(
        [],
        [
            'D12 The Great Sea',
            'E11 The Great Sea',
            'E13 The Great Sea',
        ],
    ),
    'E13 The Great Sea': EBF5RegionData(
        [],
        [
            'D13 The Great Sea',
            'E12 The Great Sea',
        ],
    ),
    'E14 Battle Arena': EBF5RegionData(
        [],
        [
            'E15 Battle Arena',
        ],
    ),
    'E15 Battle Arena': EBF5RegionData(
        [],
        [
            'E14 Battle Arena',
        ],
    ),
    'E15 The Great Sea': EBF5RegionData(
        [],
        [
            'D15 The Great Sea',
            'E15 Battle Arena',
        ],
    ),
    'E2 Freezeflame Dungeon': EBF5RegionData(
        [
            location_names.CHEST_FREEZEFLAME_DUNGEON_BEHIND_ENEMY_LEFT,
            location_names.CHEST_FREEZEFLAME_DUNGEON_BEHIND_ENEMY_RIGHT,
        ],
        [
            'D2 Freezeflame Dungeon',
            'E1 Freezeflame Dungeon',
            'E3 Ice Cave',
            'F2 Freezeflame Dungeon',
        ],
    ),
    'E2 Mystic Woods E': EBF5RegionData(
        [],
        [
            'E2 Mystic Woods W',
            'F2 Mystic Woods',
        ],
    ),
    'E2 Mystic Woods W': EBF5RegionData(
        [],
        [
            'D2 Hope Harbor E',
            'E2 Mystic Woods E',
        ],
    ),
    'E3 Ice Cave': EBF5RegionData(
        [
            location_names.CHEST_ICE_CAVE_ROOM_3_BEHIND_ENEMY,
        ],
        [
            'D4 Ice Cave',
            'E2 Freezeflame Dungeon',
            "E3 No Man's Land",
        ],
    ),
    'E3 Iron Fortress': EBF5RegionData(
        [
            location_names.CHEST_IRON_FORTRESS_SUB_ENTRANCE,
            location_names.CHEST_IRON_FORTRESS_SUB_ENTRANCE_MAGNET,
        ],
        [
            "E3 No Man's Land",
        ],
    ),
    'E3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'E4 Mineshaft Maze',
            'F3 Mineshaft Maze',
            'M3 Mineshaft Maze',
        ],
    ),
    "E3 No Man's Land": EBF5RegionData(
        [],
        [
            'E3 Ice Cave',
            "E4 No Man's Land",
        ],
    ),
    "E3 No Man's Land SW": EBF5RegionData(
        [
            location_names.CHEST_NO_MANS_LAND_HARBOR_SECRET,
        ],
        [
            "E4 No Man's Land NW",
        ],
    ),
    'E4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'E3 Mineshaft Maze',
        ],
    ),
    "E4 No Man's Land": EBF5RegionData(
        [
            location_names.CHEST_NO_MANS_LAND_HARBOR_BEHIND_ENEMY,
        ],
        [
            "E3 No Man's Land",
            "E4 No Man's Land NW",
            "E4 No Man's Land Water",
            "E5 No Man's Land",
        ],
    ),
    "E4 No Man's Land NW": EBF5RegionData(
        [],
        [
            'D4 Hope Harbor',
            "E3 No Man's Land SW",
        ],
    ),
    "E4 No Man's Land Water": EBF5RegionData(
        [],
        [
            'D4 Hope Harbor Water',
            "E4 No Man's Land",
            "E5 No Man's Land Water",
        ],
    ),
    'E5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F5 Mineshaft Maze',
        ],
    ),
    "E5 No Man's Land": EBF5RegionData(
        [
            location_names.CHEST_NO_MANS_LAND_SOUTH_WEST_BEHIND_ENEMY,
        ],
        [
            "E4 No Man's Land",
            "E5 No Man's Land Water",
            "F5 No Man's Land",
        ],
    ),
    "E5 No Man's Land Water": EBF5RegionData(
        [],
        [
            'D5 Hope Harbor Water',
            "E4 No Man's Land Water",
            "E5 No Man's Land",
            'E6 Rainbow River',
        ],
    ),
    'E6 Rainbow River': EBF5RegionData(
        [],
        [
            'D6 Rainbow River',
            "E5 No Man's Land Water",
            'F6 Rainbow River',
        ],
    ),
    'E6 Rainbow River S': EBF5RegionData(
        [],
        [
            'E6 Rainbow River',
            'E7 Redpine Town',
        ],
    ),
    'E7 Basement': EBF5RegionData(
        [],
        [
            'E7 Mausoleum',
        ],
    ),
    'E7 Mausoleum': EBF5RegionData(
        [],
        [
            'E7 Basement',
            'E7 Redpine Town',
        ],
    ),
    'E7 Redpine Town': EBF5RegionData(
        [],
        [
            'D7 Redpine Town',
            'E6 Rainbow River S',
            'E7 Mausoleum',
            'E8 Redpine Town',
            'F7 Redpine Town',
        ],
    ),
    'E8 Redpine Town': EBF5RegionData(
        [],
        [
            'D8 Redpine Town',
            'E7 Redpine Town',
            'E9 Redpine Town',
            'F8 Redpine Town',
        ],
    ),
    'E9 Crystal Caverns': EBF5RegionData(
        [],
        [
            'E0 Crystal Caverns',
            'F9 Crystal Caverns',
        ],
    ),
    'E9 Redpine Town': EBF5RegionData(
        [],
        [
            'D9 Redpine Town',
            'E8 Redpine Town',
            'F9 Redpine Town',
        ],
    ),
    'F0 Inside The Tree': EBF5RegionData(
        [],
        [
            'F0 Mystic Woods W',
            'F1 Inside The Tree',
        ],
    ),
    'F0 Mystic Woods': EBF5RegionData(
        [],
        [
            'F0 Mystic Woods W',
            'G0 Mystic Woods',
        ],
    ),
    'F0 Mystic Woods W': EBF5RegionData(
        [],
        [
            'F0 Inside The Tree',
            'F0 Mystic Woods',
        ],
    ),
    'F1 Arcade Room': EBF5RegionData(
        [],
        [
            'F1 Mystic Woods',
        ],
    ),
    'F1 Freezeflame Dungeon': EBF5RegionData(
        [
            location_names.CHEST_FREEZEFLAME_DUNGEON_FIRE_COMBAT_ROOM_LAST,
        ],
        [
            'E1 Freezeflame Dungeon E',
            'F2 Freezeflame Dungeon',
        ],
    ),
    'F1 Hidden Passage': EBF5RegionData(
        [],
        None,
    ),
    'F1 Inside The Tree': EBF5RegionData(
        [],
        [
            'F0 Inside The Tree',
            'F1 Mystic Woods',
        ],
    ),
    'F1 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F2 Mineshaft Maze',
        ],
    ),
    'F1 Mystic Woods': EBF5RegionData(
        [],
        [
            'F1 Arcade Room',
            'F1 Hidden Passage',
            'F1 Inside The Tree',
            'F2 Mystic Woods',
            'G1 Mystic Woods',
        ],
    ),
    'F2 Freezeflame Dungeon': EBF5RegionData(
        [
            location_names.CHEST_FREEZEFLAME_DUNGEON_FIRE_BLOCK_PUZZLE_ROOM,
        ],
        [
            'E2 Freezeflame Dungeon',
            'F1 Freezeflame Dungeon',
        ],
    ),
    'F2 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F1 Mineshaft Maze',
            'F3 Mineshaft Maze',
        ],
    ),
    'F2 Mystic Woods': EBF5RegionData(
        [],
        [
            'E2 Mystic Woods E',
            'F1 Mystic Woods',
            'G2 Mystic Woods',
        ],
    ),
    'F3 Iron Fortress': EBF5RegionData(
        [
            location_names.CHEST_IRON_FORTRESS_SUB_EXIT_BEHIND_ENEMY,
            location_names.CHEST_IRON_FORTRESS_SUB_EXIT_LADDER,
            location_names.CHEST_IRON_FORTRESS_SUB_EXIT_LEO_TOILET,
        ],
        [
            'E3 Iron Fortress',
            'F4 Iron Fortress',
            'G3 Iron Fortress',
        ],
    ),
    'F3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'E3 Mineshaft Maze',
            'F2 Mineshaft Maze',
            'F4 Mineshaft Maze',
            'G3 Mineshaft Maze',
        ],
    ),
    'F4 Iron Fortress': EBF5RegionData(
        [
            location_names.CHEST_IRON_FORTRESS_STORAGE_ROOM_BOTTOM_LEFT,
            location_names.CHEST_IRON_FORTRESS_STORAGE_ROOM_PAINTING,
            location_names.CHEST_IRON_FORTRESS_STORAGE_ROOM_PUZZLE,
        ],
        [
            'F3 Iron Fortress',
            'G4 Iron Fortress',
        ],
    ),
    'F4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F3 Mineshaft Maze',
            'F5 Mineshaft Maze',
            'G4 Mineshaft Maze',
        ],
    ),
    'F5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'E5 Mineshaft Maze',
            'F4 Mineshaft Maze',
            'F6 Mineshaft Maze',
        ],
    ),
    "F5 No Man's Land": EBF5RegionData(
        [],
        [
            "E5 No Man's Land",
            'F6 Rainbow River NE',
            "G5 No Man's Land",
        ],
    ),
    'F6 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F5 Mineshaft Maze',
            'G6 Mineshaft Maze',
        ],
    ),
    'F6 Rainbow River': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_STREAM_5_BOTTOM,
            location_names.CHEST_RAINBOW_RIVER_STREAM_5_RIGHT,
        ],
        [
            'E6 Rainbow River',
            'G6 Rainbow River',
        ],
    ),
    'F6 Rainbow River NE': EBF5RegionData(
        [],
        [
            "F5 No Man's Land",
            'G6 Rainbow River NW',
        ],
    ),
    'F7 Material Shop': EBF5RegionData(
        [],
        [
            'F7 Redpine Town',
        ],
    ),
    'F7 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F8 Mineshaft Maze',
        ],
    ),
    'F7 Redpine Town': EBF5RegionData(
        [],
        [
            'E7 Redpine Town',
            'F7 Material Shop',
            'F7 Stable',
            'F8 Redpine Town',
        ],
    ),
    'F7 Stable': EBF5RegionData(
        [],
        None,
    ),
    'F8 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F7 Mineshaft Maze',
            'G8 Mineshaft Maze',
        ],
    ),
    'F8 Redpine Town': EBF5RegionData(
        [],
        [
            'E8 Redpine Town',
            'F7 Redpine Town',
            'F9 Redpine Town',
            'G8 The Rapture',
        ],
    ),
    'F9 Arcade Room': EBF5RegionData(
        [],
        [
            'F9 Redpine Town',
        ],
    ),
    'F9 Crystal Caverns': EBF5RegionData(
        [],
        [
            'E9 Crystal Caverns',
            'F9 Redpine Town',
            'G9 Crystal Caverns',
        ],
    ),
    'F9 Redpine Town': EBF5RegionData(
        [],
        [
            'E9 Redpine Town',
            'F8 Redpine Town',
            'F9 Arcade Room',
            'F9 Crystal Caverns',
        ],
    ),
    'F9 Redpine Town E': EBF5RegionData(
        [],
        [
            'F9 Redpine Town',
            'G9 The Rapture',
        ],
    ),
    'G0 Mystic Woods': EBF5RegionData(
        [],
        [
            'F0 Mystic Woods',
            'H0 Mystic Woods',
        ],
    ),
    'G1 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G2 Mineshaft Maze',
        ],
    ),
    'G1 Mystic Woods': EBF5RegionData(
        [],
        [
            'F1 Mystic Woods',
            'G2 Mystic Woods',
            'H1 Mystic Woods',
        ],
    ),
    'G2 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G1 Mineshaft Maze',
            'G3 Mineshaft Maze',
            'H2 Mineshaft Maze',
        ],
    ),
    'G2 Mystic Woods': EBF5RegionData(
        [],
        [
            'F2 Mystic Woods',
            'G1 Mystic Woods',
            'H2 Mystic Woods',
        ],
    ),
    'G3 Iron Fortress': EBF5RegionData(
        [
            location_names.CHEST_IRON_FORTRESS_MIDBOSS_ROOM_BEHIND_ENEMY,
            location_names.CHEST_IRON_FORTRESS_MIDBOSS_ROOM_BEHIND_LANCE,
            location_names.CHEST_IRON_FORTRESS_UPPER_ARROW_ROOM,
        ],
        [
            'F3 Iron Fortress',
            'G4 Iron Fortress',
            'H3 Iron Fortress',
        ],
    ),
    'G3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F3 Mineshaft Maze',
            'G2 Mineshaft Maze',
            'G4 Mineshaft Maze',
            'H3 Mineshaft Maze',
        ],
    ),
    'G4 Iron Fortress': EBF5RegionData(
        [
            location_names.CHEST_IRON_FORTRESS_MONOLITH,
            location_names.CHEST_IRON_FORTRESS_MONOLITH_ROOM_BEHIND_BOTTOM_ENEMY,
            location_names.CHEST_IRON_FORTRESS_MONOLITH_ROOM_BEHIND_TOP_ENEMY,
        ],
        [
            'F4 Iron Fortress',
            'G3 Iron Fortress',
            'H4 Iron Fortress',
        ],
    ),
    'G4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F4 Mineshaft Maze',
            'G3 Mineshaft Maze',
            'G5 Mineshaft Maze',
        ],
    ),
    'G5 Glitch Area': EBF5RegionData(
        [],
        None,
    ),
    'G5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G4 Mineshaft Maze',
            'H5 Mineshaft Maze',
        ],
    ),
    "G5 No Man's Land": EBF5RegionData(
        [
            location_names.CHEST_NO_MANS_LAND_SOUTH_ROOM_2_BEHIND_ENEMY,
        ],
        [
            "F5 No Man's Land",
            'G5 Glitch Area',
            'G6 Rainbow River NE',
            'G6 Rainbow River NW',
            "H5 No Man's Land",
        ],
    ),
    'G6 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F6 Mineshaft Maze',
            'G7 Mineshaft Maze',
            'H6 Mineshaft Maze',
        ],
    ),
    'G6 Rainbow River': EBF5RegionData(
        [],
        [
            'F6 Rainbow River',
            'H6 Rainbow River Water',
        ],
    ),
    'G6 Rainbow River NE': EBF5RegionData(
        [],
        [
            "G5 No Man's Land",
            'G6 Rainbow River',
            'G6 Rainbow River NW',
            'H6 Rainbow River N',
        ],
    ),
    'G6 Rainbow River NW': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_STREAM_6,
        ],
        [
            'F6 Rainbow River NE',
            "G5 No Man's Land",
        ],
    ),
    'G6 Rainbow River S': EBF5RegionData(
        [],
        [
            'G7 The Rapture',
            'H6 Rainbow River S',
        ],
    ),
    'G7 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G6 Mineshaft Maze',
            'G8 Mineshaft Maze',
        ],
    ),
    'G7 The Rapture': EBF5RegionData(
        [],
        [
            'F7 Redpine Town',
            'G6 Rainbow River S',
            'G8 The Rapture',
            'H7 The Rapture',
        ],
    ),
    'G8 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'F8 Mineshaft Maze',
            'G7 Mineshaft Maze',
            'G9 Mineshaft Maze',
            'H8 Mineshaft Maze',
        ],
    ),
    'G8 The Rapture': EBF5RegionData(
        [],
        [
            'F8 Redpine Town',
            'G7 The Rapture',
            'G9 The Rapture',
            'H8 The Rapture',
        ],
    ),
    'G8 The Rapture E Crystal': EBF5RegionData(
        [],
        [
            'G8 The Rapture SE Crystal',
        ],
    ),
    'G8 The Rapture SE': EBF5RegionData(
        [],
        [
            'G8 The Rapture E Crystal',
            'G9 The Rapture',
        ],
    ),
    'G8 The Rapture SE Crystal': EBF5RegionData(
        [],
        [
            'G9 The Rapture',
        ],
    ),
    'G9 Crystal Caverns': EBF5RegionData(
        [],
        [
            'F9 Crystal Caverns',
            'H9 Crystal Caverns',
        ],
    ),
    'G9 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G8 Mineshaft Maze',
        ],
    ),
    'G9 The Rapture': EBF5RegionData(
        [],
        [
            'F9 Redpine Town E',
            'G8 The Rapture',
            'G8 The Rapture SE',
            'G8 The Rapture SE Crystal',
            'H9 The Rapture',
        ],
    ),
    'H0 Material Shop': EBF5RegionData(
        [],
        [
            'H0 Mystic Woods',
            'H1 Inside The Tree',
        ],
    ),
    'H0 Mystic Woods': EBF5RegionData(
        [],
        [
            'G0 Mystic Woods',
            'H0 Material Shop',
            'I0 Mystic Woods',
        ],
    ),
    'H1 Inside The Tree': EBF5RegionData(
        [],
        [
            'H0 Material Shop',
            'H1 Mystic Woods',
        ],
    ),
    'H1 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'H2 Mineshaft Maze',
        ],
    ),
    'H1 Mystic Woods': EBF5RegionData(
        [],
        [
            'H1 Inside The Tree',
            'H2 Mystic Woods',
            'I1 Mystic Woods',
        ],
    ),
    'H2 Glitch Area': EBF5RegionData(
        [],
        None,
    ),
    'H2 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G2 Mineshaft Maze',
            'H1 Mineshaft Maze',
            'H3 Mineshaft Maze',
            'I2 Mineshaft Maze',
        ],
    ),
    'H2 Mystic Woods': EBF5RegionData(
        [],
        [
            'G2 Mystic Woods',
            'H1 Mystic Woods',
            'H2 Glitch Area',
            'I2 Mystic Woods',
        ],
    ),
    'H3 Iron Fortress': EBF5RegionData(
        [
            location_names.CHEST_IRON_FORTRESS_NATALIE_ROOM,
        ],
        [
            'G3 Iron Fortress',
        ],
    ),
    'H3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G3 Mineshaft Maze',
            'H2 Mineshaft Maze',
            'H4 Mineshaft Maze',
        ],
    ),
    'H4 Iron Fortress': EBF5RegionData(
        [],
        [
            'H3 Iron Fortress',
            "H5 No Man's Land",
            'I4 Iron Fortress',
        ],
    ),
    'H4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'H3 Mineshaft Maze',
            'H5 Mineshaft Maze',
        ],
    ),
    'H5 Arcade Room': EBF5RegionData(
        [
            location_names.CHEST_NO_MANS_LAND_ARCADE_ROOM,
        ],
        [
            "H5 No Man's Land",
        ],
    ),
    'H5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G5 Mineshaft Maze',
            'H4 Mineshaft Maze',
            'I5 Mineshaft Maze',
        ],
    ),
    "H5 No Man's Land": EBF5RegionData(
        [],
        [
            "G5 No Man's Land",
            'H4 Iron Fortress',
            'H5 Arcade Room',
            'H6 Rainbow River N',
            "I5 No Man's Land",
        ],
    ),
    'H6 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G6 Mineshaft Maze',
            'H7 Mineshaft Maze',
        ],
    ),
    'H6 Rainbow River N': EBF5RegionData(
        [],
        [
            'G6 Rainbow River NE',
            "H5 No Man's Land",
            'H6 Rainbow River Water',
        ],
    ),
    'H6 Rainbow River S': EBF5RegionData(
        [],
        [
            'I6 Rainbow River Teleporter',
        ],
    ),
    'H6 Rainbow River Water': EBF5RegionData(
        [],
        [
            'G6 Rainbow River',
            'H6 Rainbow River N',
            'I6 Rainbow River',
        ],
    ),
    'H7 Mineshaft Maze': EBF5RegionData(
        [
            location_names.CHEST_MINESHAFT_MAZE_EARTHS_WHISPER,
        ],
        [
            'H6 Mineshaft Maze',
        ],
    ),
    'H7 The Rapture': EBF5RegionData(
        [],
        [
            'G7 The Rapture',
            'H9 The Rapture',
        ],
    ),
    'H8 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'G8 Mineshaft Maze',
            'H9 Mineshaft Maze',
        ],
    ),
    'H8 The Rapture': EBF5RegionData(
        [],
        [
            'G8 The Rapture',
            'I8 The Rapture',
        ],
    ),
    'H9 Crystal Caverns': EBF5RegionData(
        [],
        [
            'G9 Crystal Caverns',
            'I9 Crystal Caverns',
        ],
    ),
    'H9 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'H8 Mineshaft Maze',
            'I9 Mineshaft Maze',
        ],
    ),
    'H9 The Rapture': EBF5RegionData(
        [],
        [
            'G9 The Rapture',
        ],
    ),
    'I0 Mystic Woods': EBF5RegionData(
        [],
        [
            'H0 Mystic Woods',
            'I1 Inside The Tree',
            'J0 Mystic Woods',
        ],
    ),
    'I1 Inside The Tree': EBF5RegionData(
        [],
        [
            'I0 Mystic Woods',
            'I1 Mystic Woods',
        ],
    ),
    'I1 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I2 Mineshaft Maze',
        ],
    ),
    'I1 Mystic Woods': EBF5RegionData(
        [],
        [
            'I1 Inside The Tree',
            'I2 Mystic Woods',
            'J1 Greenwood Village',
        ],
    ),
    'I2 Library': EBF5RegionData(
        [
            location_names.CHEST_LIBRARY_LEFT_ROOM_BEHIND_WISE_MIRROR,
            location_names.CHEST_LIBRARY_LEFT_ROOM_PAPER_STACK,
        ],
        [
            'J2 Library',
        ],
    ),
    'I2 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'H2 Mineshaft Maze',
            'I1 Mineshaft Maze',
            'I3 Mineshaft Maze',
            'J2 Mineshaft Maze',
        ],
    ),
    'I2 Mystic Woods': EBF5RegionData(
        [],
        [
            'H2 Mystic Woods',
            'I1 Mystic Woods',
            'J2 Greenwood Village',
        ],
    ),
    'I3 Iron Fortress': EBF5RegionData(
        [],
        [
            'I4 Iron Fortress',
        ],
    ),
    'I3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I2 Mineshaft Maze',
            'I4 Mineshaft Maze',
            'J3 Mineshaft Maze',
        ],
    ),
    'I4 Iron Fortress': EBF5RegionData(
        [
            location_names.CHEST_IRON_FORTRESS_LOWER_ARROW_ROOM_ABDUL_CELL,
            location_names.CHEST_IRON_FORTRESS_LOWER_ARROW_ROOM_SECRET_STORAGE_LEFT,
            location_names.CHEST_IRON_FORTRESS_LOWER_ARROW_ROOM_SECRET_STORAGE_RIGHT,
        ],
        [
            'H4 Iron Fortress',
            'I3 Iron Fortress',
        ],
    ),
    'I4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I3 Mineshaft Maze',
            'I5 Mineshaft Maze',
        ],
    ),
    'I5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'H5 Mineshaft Maze',
            'I4 Mineshaft Maze',
            "I5 No Man's Land",
            'I6 Mineshaft Maze',
            'J5 Mineshaft Maze',
        ],
    ),
    "I5 No Man's Land": EBF5RegionData(
        [
            location_names.CHEST_NO_MANS_LAND_EXIT_FORTRESS_LEFT,
            location_names.CHEST_NO_MANS_LAND_EXIT_FORTRESS_MIDDLE,
            location_names.CHEST_NO_MANS_LAND_EXIT_FORTRESS_RIGHT,
        ],
        [
            "H5 No Man's Land",
            'I5 Mineshaft Maze',
            'J5 Rainbow River',
        ],
    ),
    'I6 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I5 Mineshaft Maze',
            'I7 Mineshaft Maze',
            'J6 Mineshaft Maze',
        ],
    ),
    'I6 Rainbow River': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_STREAM_8,
        ],
        [
            'H6 Rainbow River Water',
            'J6 Rainbow River Water',
        ],
    ),
    'I6 Rainbow River Teleporter': EBF5RegionData(
        [],
        [
            'H6 Rainbow River S',
        ],
    ),
    'I7 Arcade Room': EBF5RegionData(
        [],
        [
            "I7 Zombie Hydra's Cave",
        ],
    ),
    'I7 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I6 Mineshaft Maze',
            'J7 Mineshaft Maze',
        ],
    ),
    'I7 The Rapture': EBF5RegionData(
        [],
        [
            "I7 Zombie Hydra's Cave",
            'I8 The Rapture',
            'J7 Lava Lake',
        ],
    ),
    "I7 Zombie Hydra's Cave": EBF5RegionData(
        [],
        [
            'I7 Arcade Room',
            'I7 The Rapture',
        ],
    ),
    'I8 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J8 Mineshaft Maze',
        ],
    ),
    'I8 The Beyond': EBF5RegionData(
        [],
        [
            'I8 The Rapture',
            'J8 The Beyond',
        ],
    ),
    'I8 The Rapture': EBF5RegionData(
        [],
        [
            'H8 The Rapture',
            'I7 The Rapture',
            'I8 The Beyond',
            'I9 The Rapture',
            'J8 Lava Lake',
        ],
    ),
    'I9 Crystal Caverns': EBF5RegionData(
        [],
        [
            'H9 Crystal Caverns',
        ],
    ),
    'I9 Mineshaft Maze': EBF5RegionData(
        [
            location_names.CHEST_MINESHAFT_MAZE_BOSS_ROOM_BOTTOM,
            location_names.CHEST_MINESHAFT_MAZE_BOSS_ROOM_LEFT,
            location_names.CHEST_MINESHAFT_MAZE_BOSS_ROOM_RIGHT,
        ],
        [
            'H9 Mineshaft Maze',
        ],
    ),
    'I9 The Rapture': EBF5RegionData(
        [],
        [
            'H9 The Rapture',
            'I8 The Rapture',
            'J9 Lava Lake',
        ],
    ),
    "J0 Anna's House": EBF5RegionData(
        [],
        [
            'J0 Mystic Woods House',
            "J1 Anna's House",
        ],
    ),
    'J0 Mystic Woods': EBF5RegionData(
        [],
        [
            'I0 Mystic Woods',
            'J0 Mystic Woods E',
            'J0 Mystic Woods House',
        ],
    ),
    'J0 Mystic Woods E': EBF5RegionData(
        [],
        [
            'J0 Mystic Woods',
        ],
    ),
    'J0 Mystic Woods House': EBF5RegionData(
        [],
        [
            "J0 Anna's House",
            'J0 Mystic Woods',
        ],
    ),
    "J1 Anna's House": EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_BRONZE_BOTTOM_LEFT,
            location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_BRONZE_BOTTOM_RIGHT,
            location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_BRONZE_TOP_LEFT,
            location_names.CHEST_GREENWOOD_VILLAGE_ANNAS_HOUSE_DRAWER,
        ],
        [
            "J0 Anna's House",
        ],
    ),
    'J1 Greenwood Village': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_OUTSIDE_ANNAS_HOUSE_TARGET,
        ],
        [
            "J1 Anna's House",
            'J2 Greenwood Village',
            'K1 Greenwood Village',
        ],
    ),
    'J1 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J2 Mineshaft Maze',
            'J9 Mineshaft Maze',
        ],
    ),
    'J2 Greenwood Village': EBF5RegionData(
        [],
        [
            'I2 Mystic Woods',
            'J1 Greenwood Village',
            'J3 Greenwood Village',
            'K2 Greenwood Village',
        ],
    ),
    'J2 Library': EBF5RegionData(
        [
            location_names.CHEST_LIBRARY_MIDDLE_ROOM_BEHIND_CAT_WIZARD,
            location_names.CHEST_LIBRARY_MIDDLE_ROOM_BEHIND_PAPER_BOSS_LEFT,
            location_names.CHEST_LIBRARY_MIDDLE_ROOM_BEHIND_PAPER_BOSS_RIGHT,
        ],
        [
            'I2 Library',
            'J3 Library',
            'K2 Library',
        ],
    ),
    'J2 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I2 Mineshaft Maze',
            'J1 Mineshaft Maze',
            'J3 Mineshaft Maze',
            'K2 Mineshaft Maze',
        ],
    ),
    'J3 Greenwood Village': EBF5RegionData(
        [],
        [
            'J2 Greenwood Village',
            'J3 Library',
            'J4 Greenwood Village',
            'K3 Greenwood Village',
        ],
    ),
    'J3 Library': EBF5RegionData(
        [],
        [
            'J2 Library',
            'J3 Greenwood Village',
        ],
    ),
    'J3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I3 Mineshaft Maze',
            'J2 Mineshaft Maze',
            'J4 Mineshaft Maze',
        ],
    ),
    'J4 Greenwood Village': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_FARM,
        ],
        [
            'J3 Greenwood Village',
            'J4 Stable',
            'J5 Rainbow River',
            'K4 Greenwood Village',
        ],
    ),
    'J4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J3 Mineshaft Maze',
            'J5 Mineshaft Maze',
            'K4 Mineshaft Maze',
        ],
    ),
    'J4 Stable': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_BARN_LEFT,
            location_names.CHEST_GREENWOOD_VILLAGE_BARN_RIGHT,
        ],
        None,
    ),
    'J5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I5 Mineshaft Maze',
            'J4 Mineshaft Maze',
        ],
    ),
    'J5 Rainbow River': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_FORTRESS_SECRET,
        ],
        [
            "I5 No Man's Land",
            'J4 Greenwood Village',
            'J5 Rainbow River SW Water',
            'J5/K5 Rainbow River',
        ],
    ),
    'J5 Rainbow River SW Water': EBF5RegionData(
        [],
        [
            'J5 Rainbow River',
        ],
    ),
    'J5/K5 Rainbow River': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_MIDDLE_ISLAND,
        ],
        [
            'J5 Rainbow River',
            'J6 Rainbow River Land',
            'K5 Rainbow River Water',
        ],
    ),
    'J6 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I6 Mineshaft Maze',
            'J7 Mineshaft Maze',
            'K6 Mineshaft Maze',
        ],
    ),
    'J6 Rainbow River Land': EBF5RegionData(
        [],
        [
            'J5/K5 Rainbow River',
            'J6 Rainbow River Water',
        ],
    ),
    'J6 Rainbow River S': EBF5RegionData(
        [],
        [
            'J6 Rainbow River Water',
            'J7 Lava Lake',
        ],
    ),
    'J6 Rainbow River Water': EBF5RegionData(
        [],
        [
            'I6 Rainbow River',
            'J6 Rainbow River Land',
            'K6 Rainbow River Water',
        ],
    ),
    'J7 Lava Lake': EBF5RegionData(
        [],
        [
            'I7 The Rapture',
            'J6 Rainbow River S',
        ],
    ),
    'J7 Lava Lake S': EBF5RegionData(
        [],
        [
            'J8 Lava Lake',
            'K7 Lava Lake',
        ],
    ),
    'J7 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I7 Mineshaft Maze',
            'J6 Mineshaft Maze',
            'J8 Mineshaft Maze',
        ],
    ),
    'J8 Lava Lake': EBF5RegionData(
        [
            location_names.EQUIPMENT_SHOP_ITEM_1,
        ],
        [
            'I8 The Rapture',
            'J7 Lava Lake',
            'J9 Lava Lake',
        ],
    ),
    'J8 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'I8 Mineshaft Maze',
            'J7 Mineshaft Maze',
            'J9 Mineshaft Maze',
            'K8 Mineshaft Maze',
        ],
    ),
    'J8 The Beyond': EBF5RegionData(
        [],
        [
            'I8 The Beyond',
            'K8 The Beyond',
        ],
    ),
    'J9 Lava Lake': EBF5RegionData(
        [],
        [
            'I9 The Rapture',
            'J8 Lava Lake',
            'K9 Lava Lake',
        ],
    ),
    'J9 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J1 Mineshaft Maze',
            'J8 Mineshaft Maze',
        ],
    ),
    'K0 Arcade Room': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_TOTOM_ARCADE_LEFT_SECRET,
            location_names.CHEST_GREENWOOD_VILLAGE_TOTOM_ARCADE_REWARD,
        ],
        [
            'K0 Greenwood Village',
        ],
    ),
    'K0 Greenwood Village': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_ORB_SHRINE_BEHIND_ENEMY,
            location_names.CHEST_GREENWOOD_VILLAGE_ORB_SHRINE_ORB_SECRET,
        ],
        [
            'K0 Arcade Room',
            'K1 Greenwood Village',
        ],
    ),
    'K1 Greenwood Village': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_BLOCK_PUZZLE,
            location_names.CHEST_GREENWOOD_VILLAGE_EGG_SHRINE,
        ],
        [
            'J1 Greenwood Village',
            'K0 Greenwood Village',
            'K2 Greenwood Village',
        ],
    ),
    'K1 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K2 Mineshaft Maze',
            'L1 Mineshaft Maze',
        ],
    ),
    'K2 Arcade Room': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_BOSH_ARCADE_LEFT,
            location_names.CHEST_GREENWOOD_VILLAGE_BOSH_ARCADE_RIGHT,
        ],
        [
            'K2 Greenwood Village',
        ],
    ),
    'K2 Greenwood Village': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_STATUES,
            location_names.CHEST_GREENWOOD_VILLAGE_STATUE_ROOM_SECRET_PATH,
        ],
        [
            'J2 Greenwood Village',
            'K1 Greenwood Village',
            'K2 Arcade Room',
            'K2 Material Food Shops',
            'K3 Greenwood Village',
        ],
    ),
    'K2 Library': EBF5RegionData(
        [
            location_names.CHEST_LIBRARY_RIGHT_ROOM_BOOKSHELF,
        ],
        [
            'J2 Library',
        ],
    ),
    'K2 Material Food Shops': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_MATERIALS_SHOP,
        ],
        [
            'K2 Greenwood Village',
        ],
    ),
    'K2 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J2 Mineshaft Maze',
            'K1 Mineshaft Maze',
            'L2 Mineshaft Maze',
        ],
    ),
    'K3 Equipment Shop': EBF5RegionData(
        [],
        [
            'K3 Greenwood Village',
        ],
    ),
    'K3 Greenwood Village': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_BEHIND_RANDYS_HOUSE,
        ],
        [
            'J3 Greenwood Village',
            'K2 Greenwood Village',
            'K3 Equipment Shop',
            "K3 Randy's House",
            'K4 Greenwood Village',
        ],
    ),
    'K3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K4 Mineshaft Maze',
            'M2 Mineshaft Maze',
        ],
    ),
    "K3 Randy's House": EBF5RegionData(
        [],
        [
            'K3 Greenwood Village',
        ],
    ),
    'K4 Basement': EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_BASEMENT_BOTTOM,
            location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_BASEMENT_LEFT,
            location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_BASEMENT_TOP,
        ],
        [
            "K4 Jamie's House",
        ],
    ),
    'K4 Greenwood Village': EBF5RegionData(
        [],
        [
            'J4 Greenwood Village',
            'K3 Greenwood Village',
            "K4 Jamie's House",
            'K5 Rainbow River N',
        ],
    ),
    "K4 Jamie's House": EBF5RegionData(
        [
            location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_HOUSE_LEFT,
            location_names.CHEST_GREENWOOD_VILLAGE_JAMIES_HOUSE_RIGHT,
        ],
        [
            'K4 Basement',
        ],
    ),
    'K4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J4 Mineshaft Maze',
            'K3 Mineshaft Maze',
            'K5 Mineshaft Maze',
            'L4 Mineshaft Maze',
        ],
    ),
    'K5 Arcade Room': EBF5RegionData(
        [],
        [
            'K5 Rainbow River',
        ],
    ),
    'K5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K4 Mineshaft Maze',
            'L5 Mineshaft Maze',
        ],
    ),
    'K5 Rainbow River': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_RIGHT_ISLAND_TOP,
        ],
        [
            'K5 Arcade Room',
            'K5 Rainbow River N',
            'K5 Rainbow River SE',
        ],
    ),
    'K5 Rainbow River N': EBF5RegionData(
        [],
        [
            'K4 Greenwood Village',
            'K5 Rainbow River',
        ],
    ),
    'K5 Rainbow River SE': EBF5RegionData(
        [],
        [
            'K5 Rainbow River',
            'K5 Rainbow River SE Port',
            'K6 Rainbow River',
        ],
    ),
    'K5 Rainbow River SE Port': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_RIGHT_ISLAND_BOTTOM,
        ],
        [
            'K5 Rainbow River SE',
            'K5 Rainbow River Water',
        ],
    ),
    'K5 Rainbow River Water': EBF5RegionData(
        [],
        [
            'J5/K5 Rainbow River',
            'K5 Rainbow River N',
            'K5 Rainbow River SE Port',
            'K6 Rainbow River Water',
        ],
    ),
    'K5 Temple of Trials': EBF5RegionData(
        [],
        [
            'K6 Temple of Trials',
        ],
    ),
    'K6 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J6 Mineshaft Maze',
            'K7 Mineshaft Maze',
            'L6 Mineshaft Maze',
        ],
    ),
    'K6 Rainbow River': EBF5RegionData(
        [
            location_names.CHEST_RAINBOW_RIVER_STREAM_10,
        ],
        [
            'K6 Rainbow River Water',
        ],
    ),
    'K6 Rainbow River Water': EBF5RegionData(
        [],
        [
            'J6 Rainbow River Water',
            'K5 Rainbow River Water',
            'K6 Rainbow River',
        ],
    ),
    'K6 Temple of Trials': EBF5RegionData(
        [],
        [
            'K5 Temple of Trials',
            'K7 Temple of Trials',
        ],
    ),
    'K7 Lava Lake': EBF5RegionData(
        [],
        [
            'J7 Lava Lake S',
            'K7 Temple of Trials',
        ],
    ),
    'K7 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K6 Mineshaft Maze',
            'K8 Mineshaft Maze',
            'L7 Mineshaft Maze',
        ],
    ),
    'K7 Temple of Trials': EBF5RegionData(
        [],
        [
            'K6 Temple of Trials',
            'K7 Lava Lake',
        ],
    ),
    'K8 Lava Lake': EBF5RegionData(
        [],
        [
            'J8 Lava Lake',
            'K7 Lava Lake',
            'K9 Lava Lake',
        ],
    ),
    'K8 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'J8 Mineshaft Maze',
            'K7 Mineshaft Maze',
            'L8 Mineshaft Maze',
        ],
    ),
    'K8 The Beyond': EBF5RegionData(
        [],
        [
            'J8 The Beyond',
        ],
    ),
    'K9 Lava Lake': EBF5RegionData(
        [],
        [
            'J9 Lava Lake',
            'K8 Lava Lake',
        ],
    ),
    'L1 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K1 Mineshaft Maze',
        ],
    ),
    'L2 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K2 Mineshaft Maze',
            'L3 Mineshaft Maze',
        ],
    ),
    'L3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'L2 Mineshaft Maze',
            'L4 Mineshaft Maze',
            'M3 Mineshaft Maze',
        ],
    ),
    'L4 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K4 Mineshaft Maze',
            'L3 Mineshaft Maze',
            'L5 Mineshaft Maze',
        ],
    ),
    'L5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K5 Mineshaft Maze',
            'L4 Mineshaft Maze',
            'L6 Mineshaft Maze',
            'M5 Mineshaft Maze',
        ],
    ),
    'L6 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K6 Mineshaft Maze',
            'L5 Mineshaft Maze',
            'L7 Mineshaft Maze',
        ],
    ),
    'L7 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K7 Mineshaft Maze',
            'L6 Mineshaft Maze',
            'L8 Mineshaft Maze',
            'M7 Mineshaft Maze',
        ],
    ),
    'L8 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'K8 Mineshaft Maze',
            'L7 Mineshaft Maze',
        ],
    ),
    'M2 Mineshaft Maze': EBF5RegionData(
        [
            location_names.CHEST_MINESHAFT_MAZE_UPPER_LIGHT_PUZZLE_ROOM,
        ],
        [
            'K3 Mineshaft Maze',
        ],
    ),
    'M3 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'E3 Mineshaft Maze',
            'L3 Mineshaft Maze',
        ],
    ),
    'M4 Mineshaft Maze': EBF5RegionData(
        [
            location_names.CHEST_MINESHAFT_MAZE_SHOOTING_STAR,
        ],
        [
            'M5 Mineshaft Maze',
        ],
    ),
    'M5 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'L5 Mineshaft Maze',
            'M4 Mineshaft Maze',
        ],
    ),
    'M7 Mineshaft Maze': EBF5RegionData(
        [],
        [
            'L7 Mineshaft Maze',
            'M8 Mineshaft Maze',
        ],
    ),
    'M8 Mineshaft Maze': EBF5RegionData(
        [
            location_names.CHEST_MINESHAFT_MAZE_LOWER_LIGHT_PUZZLE_ROOM_LEFT,
            location_names.CHEST_MINESHAFT_MAZE_LOWER_LIGHT_PUZZLE_ROOM_RIGHT,
        ],
        [
            'M7 Mineshaft Maze',
        ],
    ),
}


# One entry per authored connection. Two-way connections get both directions.
connection_rules: Dict[Tuple[str, str], Rule] = {
    ('A2 Hope Harbor', 'A3 Wild Tropics'):
        Has('The Shovel'),
    ('A3 Wild Tropics', 'A2 Hope Harbor'):
        Has('The Shovel'),
    ('A4 Wild Tropics', 'A5 Hope Harbor'):
        Has('The Shovel'),
    ('A5 Hope Harbor', 'A4 Wild Tropics'):
        Has('The Shovel'),
    ('A7 Frozen Valley Water', 'A7 Frozen Valley E'):
        Has('The Raft'),
    ('A7 Frozen Valley E', 'A7 Frozen Valley Water'):
        Has('The Raft'),
    ('A7 Frozen Valley Water', 'A7 Frozen Valley SW'):
        Has('The Raft'),
    ('A7 Frozen Valley SW', 'A7 Frozen Valley Water'):
        Has('The Raft'),
    ('A8 Frozen Valley', 'B8 Frozen Valley'):
        Has('Spiked Boots'),
    ('B8 Frozen Valley', 'A8 Frozen Valley'):
        Has('Spiked Boots'),
    ('B2 Hope Harbor', 'B3 Wild Tropics'):
        Has('The Shovel'),
    ('B3 Wild Tropics', 'B2 Hope Harbor'):
        Has('The Shovel'),
    ('B3 Arcade Room', 'C3 Wild Tropics'):
        Has('The Hammer'),
    ('C3 Wild Tropics', 'B3 Arcade Room'):
        Has('The Hammer'),
    ('B3 Wild Tropics', 'B4 Wild Tropics'):
        Has('The Shovel'),
    ('B4 Wild Tropics', 'B3 Wild Tropics'):
        Has('The Shovel'),
    ('B5 Hope Harbor', 'B5 Hope Harbor Water'):
        Has('The Raft'),
    ('B5 Hope Harbor Water', 'B5 Hope Harbor'):
        Has('The Raft'),
    ('B6 Rainbow River', 'B6 Rainbow River Land'):
        Has('The Raft'),
    ('B6 Rainbow River Land', 'B6 Rainbow River'):
        Has('The Raft'),
    ('B8 Frozen Valley', 'B9 Frozen Valley'):
        Has('Spiked Boots'),
    ('B9 Frozen Valley', 'B8 Frozen Valley'):
        Has('Spiked Boots'),
    ('B9 Frozen Valley', 'C9 Frozen Valley'):
        Has('Spiked Boots'),
    ('C9 Frozen Valley', 'B9 Frozen Valley'):
        Has('Spiked Boots'),
    ('C2 Arcade Room', 'C2 Hope Harbor'):
        Has('The Shovel'),
    ('C2 Hope Harbor', 'C2 Arcade Room'):
        Has('The Shovel'),
    ('C2 Hope Harbor', 'D2 Hope Harbor W'):
        Has('The Shovel'),
    ('D2 Hope Harbor W', 'C2 Hope Harbor'):
        Has('The Shovel'),
    ('C3 Wild Tropics', 'C3 Dragon Armor Cave'):
        Has('The Hammer'),
    ('C3 Dragon Armor Cave', 'C3 Wild Tropics'):
        Has('The Hammer'),
    # Unlock once you get out of sphere 0
    ('C3 Wild Tropics', "C3 Indy's Cave"):
        CanReachRegion('D3 Hope Harbor'),
    ('C3 Wild Tropics', 'D3 Hope Harbor'):
        Has('The Shovel'),
    ('D3 Hope Harbor', 'C3 Wild Tropics'):
        Has('The Shovel'),
    ('C5 Hope Harbor', 'C5 Hope Harbor Water'):
        Has('The Raft'),
    ('C5 Hope Harbor Water', 'C5 Hope Harbor'):
        Has('The Raft'),
    ('C6 Rainbow River Land', 'C7 Frozen Valley'):
        Has('Stone Head', 6),
    ('C7 Frozen Valley', 'C7 Frozen Valley Ice'):
        Has('Spiked Boots'),
    ('C7 Frozen Valley Ice', 'C7 Frozen Valley'):
        Has('Spiked Boots'),
    ('C8 Frozen Valley', 'C9 Frozen Valley'):
        Has('Spiked Boots'),
    ('C9 Frozen Valley', 'C8 Frozen Valley'):
        Has('Spiked Boots'),
    ('C9 Frozen Valley', 'C9 Frozen Valley Water'):
        Has('The Raft'),
    ('C9 Frozen Valley Water', 'C9 Frozen Valley'):
        Has('The Raft'),
    ('D1 Forgotten Ruins', 'D1 Forgotten Ruins NW'):
        Has('The Shovel'),
    ('D1 Forgotten Ruins NW', 'D1 Forgotten Ruins'):
        Has('The Shovel'),
    ('D14 The Great Sea', 'D14 The Great Sea Island'):
        Has('The Stepladder'),
    ('D14 The Great Sea Island', 'D14 The Great Sea'):
        Has('The Stepladder'),
    ('D15 The Great Sea', 'D15 The Great Sea Island'):
        Has('The Raft'),
    ('D15 The Great Sea Island', 'D15 The Great Sea'):
        Has('The Raft'),
    ('D2 Deathly Hollows Start', 'D2 Deathly Hollows'):
        Has('The Hammer'),
    ('D2 Hope Harbor E', 'E2 Mystic Woods W'):
        Has('The Raft'),
    ('E2 Mystic Woods W', 'D2 Hope Harbor E'):
        Has('The Raft'),
    ('D2 Hope Harbor W', 'D2 Hope Harbor Water'):
        Has('The Raft'),
    ('D2 Hope Harbor Water', 'D2 Hope Harbor W'):
        Has('The Raft'),
    ('D2 Hope Harbor Water', 'D2 Hope Harbor E'):
        Has('The Raft'),
    ('D2 Hope Harbor E', 'D2 Hope Harbor Water'):
        Has('The Raft'),
    ('D4 Hope Harbor', 'D4 Hope Harbor Water'):
        Has('The Raft'),
    ('D4 Hope Harbor Water', 'D4 Hope Harbor'):
        Has('The Raft'),
    ('D4 Hope Harbor', "E4 No Man's Land NW"):
        Has('The Hammer'),
    ("E4 No Man's Land NW", 'D4 Hope Harbor'):
        Has('The Hammer'),
    ('D4 Hope Harbor Cave Chest', 'D4 Ice Cave'):
        Has('Spiked Boots'),
    ('D4 Ice Cave', 'D4 Hope Harbor Cave Chest'):
        Has('Spiked Boots'),
    ('D5 Hope Harbor', 'D5 Hope Harbor Water'):
        Has('The Raft'),
    ('D5 Hope Harbor Water', 'D5 Hope Harbor'):
        Has('The Raft'),
    ('D9 Redpine Town', 'D9 Redpine Town Water'):
        Has('The Raft'),
    ('D9 Redpine Town Water', 'D9 Redpine Town'):
        Has('The Raft'),
    ('D9 Redpine Town Water', 'D10 The Great Sea'):
        Has('The Raft'),
    ('D10 The Great Sea', 'D9 Redpine Town Water'):
        Has('The Raft'),
    ('E0 Crystal Caverns', 'D0 Crystal Caverns'):
        Has('The Shovel'),
    ('D0 Crystal Caverns', 'E0 Crystal Caverns'):
        Has('The Shovel'),
    ('E0 Freezeflame Dungeon', 'E1 Freezeflame Dungeon'):
        CanReachRegion('E1 Freezeflame Dungeon E') & CanReachRegion('E1 Freezeflame Dungeon W'),
    ('E1 Freezeflame Dungeon', 'E0 Freezeflame Dungeon'):
        CanReachRegion('E1 Freezeflame Dungeon E') & CanReachRegion('E1 Freezeflame Dungeon W'),
    ('E1 Forgotten Ruins NE', 'E1 Forgotten Ruins NW'):
        Has('The Shovel'),
    ('E1 Forgotten Ruins NW', 'E1 Forgotten Ruins NE'):
        Has('The Shovel'),
    ('E1 Forgotten Ruins S', 'D1 Forgotten Ruins'):
        Has('The Shovel'),
    ('D1 Forgotten Ruins', 'E1 Forgotten Ruins S'):
        Has('The Shovel'),
    ('E2 Mystic Woods E', 'E2 Mystic Woods W'):
        Has('The Raft'),
    ('E2 Mystic Woods W', 'E2 Mystic Woods E'):
        Has('The Raft'),
    ('E2 Mystic Woods E', 'F2 Mystic Woods'):
        Has('Leafy Boots'),
    ('F2 Mystic Woods', 'E2 Mystic Woods E'):
        Has('Leafy Boots'),
    ("E4 No Man's Land", "E4 No Man's Land Water"):
        Has('The Raft'),
    ("E4 No Man's Land Water", "E4 No Man's Land"):
        Has('The Raft'),
    ("E5 No Man's Land", "E5 No Man's Land Water"):
        Has('The Raft'),
    ("E5 No Man's Land Water", "E5 No Man's Land"):
        Has('The Raft'),
    ('F0 Mystic Woods', 'F0 Mystic Woods W'):
        Has('The Stepladder'),
    ('F0 Mystic Woods W', 'F0 Mystic Woods'):
        Has('The Stepladder'),
    ('F0 Mystic Woods', 'G0 Mystic Woods'):
        Has('The Stepladder'),
    ('G0 Mystic Woods', 'F0 Mystic Woods'):
        Has('The Stepladder'),
    ('F2 Mystic Woods', 'G2 Mystic Woods'):
        Has('Leafy Boots'),
    ('G2 Mystic Woods', 'F2 Mystic Woods'):
        Has('Leafy Boots'),
    ("F5 No Man's Land", 'F6 Rainbow River NE'):
        Has('The Hammer'),
    ('F6 Rainbow River NE', "F5 No Man's Land"):
        Has('The Hammer'),
    ('F9 Crystal Caverns', 'G9 Crystal Caverns'):
        Has('The Big Hammer'),
    ('G9 Crystal Caverns', 'F9 Crystal Caverns'):
        Has('The Big Hammer'),
    ('F9 Redpine Town', 'F9 Crystal Caverns'):
        Has('Spiked Boots'),
    ('F9 Crystal Caverns', 'F9 Redpine Town'):
        Has('Spiked Boots'),
    ('G0 Mystic Woods', 'H0 Mystic Woods'):
        Has('The Stepladder'),
    ('H0 Mystic Woods', 'G0 Mystic Woods'):
        Has('The Stepladder'),
    ('G3 Iron Fortress', 'G4 Iron Fortress'):
        Has('The Hammer'),
    ('G4 Iron Fortress', 'G3 Iron Fortress'):
        Has('The Hammer'),
    ('G6 Rainbow River NE', 'G6 Rainbow River'):
        Has('The Raft'),
    ('G8 The Rapture', 'G7 The Rapture'):
        Has('The Big Hammer'),
    ('G7 The Rapture', 'G8 The Rapture'):
        Has('The Big Hammer'),
    ('G8 The Rapture SE', 'G8 The Rapture E Crystal'):
        Has('The Big Hammer'),
    ('G8 The Rapture SE Crystal', 'G9 The Rapture'):
        Has('The Big Hammer'),
    ('G9 The Rapture', 'G8 The Rapture SE Crystal'):
        Has('The Big Hammer'),
    ('G9 Crystal Caverns', 'H9 Crystal Caverns'):
        Has('The Big Hammer'),
    ('H9 Crystal Caverns', 'G9 Crystal Caverns'):
        Has('The Big Hammer'),
    ('G9 The Rapture', 'G8 The Rapture'):
        Has('The Big Hammer'),
    ('G8 The Rapture', 'G9 The Rapture'):
        Has('The Big Hammer'),
    ('H2 Mystic Woods', 'I2 Mystic Woods'):
        Has('Leafy Boots'),
    ('I2 Mystic Woods', 'H2 Mystic Woods'):
        Has('Leafy Boots'),
    ("H5 No Man's Land", "I5 No Man's Land"):
        Has('The Hammer'),
    ("I5 No Man's Land", "H5 No Man's Land"):
        Has('The Hammer'),
    ('H6 Rainbow River Water', 'H6 Rainbow River N'):
        Has('The Raft'),
    ('H6 Rainbow River N', 'H6 Rainbow River Water'):
        Has('The Raft'),
    ('I2 Mystic Woods', 'J2 Greenwood Village'):
        Has('The Axe'),
    ('J2 Greenwood Village', 'I2 Mystic Woods'):
        Has('The Axe'),
    ("I7 Zombie Hydra's Cave", 'I7 The Rapture'):
        Has('The Candle'),
    ('I7 The Rapture', "I7 Zombie Hydra's Cave"):
        Has('The Candle'),
    ('I8 The Beyond', 'I8 The Rapture'):
        Has('Water Orb') & Has('Earth Orb') & Has('Fire Orb') & Has('Wind Orb'),
    ('I8 The Rapture', 'I8 The Beyond'):
        Has('Water Orb') & Has('Earth Orb') & Has('Fire Orb') & Has('Wind Orb'),
    ('J0 Mystic Woods', 'J0 Mystic Woods E'):
        Has('The Stepladder'),
    ('J0 Mystic Woods E', 'J0 Mystic Woods'):
        Has('The Stepladder'),
    ('J0 Mystic Woods', 'J0 Mystic Woods House'):
        Has('The Stepladder'),
    ('J0 Mystic Woods House', 'J0 Mystic Woods'):
        Has('The Stepladder'),
    ('J5 Rainbow River', 'J5 Rainbow River SW Water'):
        Has('The Raft'),
    ('J5 Rainbow River SW Water', 'J5 Rainbow River'):
        Has('The Raft'),
    ('J5 Rainbow River', 'J5/K5 Rainbow River'):
        Has('The Axe'),
    ('J5/K5 Rainbow River', 'J5 Rainbow River'):
        Has('The Axe'),
    ('J5/K5 Rainbow River', 'K5 Rainbow River Water'):
        Has('The Raft'),
    ('K5 Rainbow River Water', 'J5/K5 Rainbow River'):
        Has('The Raft'),
    ('J6 Rainbow River Land', 'J5/K5 Rainbow River'):
        Has('The Axe'),
    ('J5/K5 Rainbow River', 'J6 Rainbow River Land'):
        Has('The Axe'),
    ('J6 Rainbow River S', 'J6 Rainbow River Water'):
        Has('The Raft'),
    ('J6 Rainbow River Water', 'J6 Rainbow River Land'):
        Has('The Raft'),
    ('J6 Rainbow River Land', 'J6 Rainbow River Water'):
        Has('The Raft'),
    ('K2 Arcade Room', 'K2 Greenwood Village'):
        Has('The Hammer'),
    ('K2 Greenwood Village', 'K2 Arcade Room'):
        Has('The Hammer'),
    ('K5 Rainbow River', 'K5 Rainbow River N'):
        Has('The Stepladder'),
    ('K5 Rainbow River N', 'K5 Rainbow River'):
        Has('The Stepladder'),
    ('K5 Rainbow River', 'K5 Rainbow River SE'):
        Has('The Big Hammer'),
    ('K5 Rainbow River SE', 'K5 Rainbow River'):
        Has('The Big Hammer'),
    ('K5 Rainbow River SE', 'K5 Rainbow River SE Port'):
        Has('The Big Hammer'),
    ('K5 Rainbow River SE Port', 'K5 Rainbow River SE'):
        Has('The Big Hammer'),
    ('K5 Rainbow River Water', 'K5 Rainbow River N'):
        Has('The Raft'),
    ('K5 Rainbow River Water', 'K5 Rainbow River SE Port'):
        Has('The Raft'),
    ('K5 Rainbow River SE Port', 'K5 Rainbow River Water'):
        Has('The Raft'),
    ('K6 Rainbow River', 'K6 Rainbow River Water'):
        Has('The Raft') & Has('The Big Hammer'),
    ('K6 Rainbow River Water', 'K6 Rainbow River'):
        Has('The Raft') & Has('The Big Hammer'),
}


location_rules: Dict[str, Rule] = {
    # Add other rules here like quest NPCs
}


def location_table() -> Dict[str, object]:
    table: Dict[str, object] = {}
    for group in ("shop_items", "chests", "secrets", "pickups"):
        table.update(getattr(Locations, group, None) or {})
    return table


def create_regions(world) -> None:
    table = location_table()

    regions: Dict[str, Region] = {}
    for name in [MENU_REGION, *region_data]:
        regions[name] = Region(name, world.player, world.multiworld)
        world.multiworld.regions.append(regions[name])

    regions[MENU_REGION].connect(regions[START_REGION])

    for name, data in region_data.items():
        region = regions[name]
        for location_name in data.locations:
            entry = table.get(location_name)
            region.locations.append(
                EBF5Location(world.player, location_name,
                             getattr(entry, "id", None), region))
        for target in data.region_exits or []:
            world.create_entrance(region, regions[target],
                                  connection_rules.get((name, target)))


def set_rules(world) -> None:
    for location_name, rule in location_rules.items():
        world.set_rule(world.multiworld.get_location(location_name, world.player),
                       rule)
