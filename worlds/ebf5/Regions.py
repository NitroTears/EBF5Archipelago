from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld

class EBF5RegionData(NamedTuple):
    locations: List[str]
    region_exits: Optional[List[str]]