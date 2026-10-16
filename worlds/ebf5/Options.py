from Options import Toggle, PerGameCommonOptions
from dataclasses import dataclass

class IncludeSeasonalContent(Toggle):
    """Includes seasonal Weapons and Skills in the item pool."""
    display_name = "Include Seasonal Content"
    default = 1

@dataclass
class EpicBattleFantasy5Options(PerGameCommonOptions):
    include_seasonal:   IncludeSeasonalContent