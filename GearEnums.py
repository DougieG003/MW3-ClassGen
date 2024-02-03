"""
Enums to hold names of gear.
"""

from enum import Enum, auto

class Vest(Enum):
    INFANTRY_VEST = auto()
    ENGINEER_VEST = auto()
    GUNNER_VEST = auto()
    DEMOLITION_VEST = auto()
    CCT_COMMS_VEST = auto()
    OVERKILL_VEST = auto()
    ASSASSIN_VEST = auto()


class Tactical(Enum):
    STUN_GRENADE = auto()
    BATTLE_RAGE = auto()
    SMOKE_GRENADE = auto()
    SCATTER_MINE = auto()
    DECOY_GRENADE = auto()
    FLASH_GRENADE = auto()
    SNAPSHOT_GRENADE = auto()
    SHOCK_STICK = auto()
    STIM = auto()
    TEAR_GAS = auto()
    EMD_GRENADE = auto()


class Lethal(Enum):
    FRAG_GRENADE = auto()
    CLAYMORE = auto()
    THROWING_KNIFE = auto()
    THERMITE_GRENADE = auto()
    THERMOBARIC_GRENADE = auto()
    PROXIMITY_MINE = auto()
    DRILL_CHARGE = auto()
    SEMTEX = auto()
    C4 = auto()
    BREACHER_DRONE = auto()
    THROWING_STAR = auto()


class FieldUpgrade(Enum):
    HEARTBEAT_SENSOR = auto()
    TACTICAL_INSERTION = auto()
    TROPHY_SYSTEM = auto()
    COMM_SCRAMBLER = auto()
    MED_BOX = auto()
    INFLATABLE_DECOY = auto()
    ACS = auto()
    TACTICAL_CAMERA = auto()
    MUNITIONS_BOX = auto()
    DEPLOYABLE_COVER = auto()
    DDOS = auto()
    RECON_DRONE = auto()
    DEAD_SILENCE = auto()
    LOADOUT_DROP = auto()
    PORTABLE_RADAR = auto()
    SMOKE_AIRDROP = auto()
    SUPPRESSION_MINE = auto()
    ANTI_ARMOR_ROUNDS = auto()


class Gloves(Enum):
    QUICK_GRIP_GLOVES = auto()
    ORDANANCE_GLOVES = auto()
    COMMANDO_GLOVES = auto()
    SCAVENGER_GLOVES = auto()
    MARKSMAN_GLOVES = auto()
    ASSAULT_GLOVES = auto()


class Boots(Enum):
    LIGHTWEIGHT_BOOTS = auto()
    CLIMBING_BOOTS = auto()
    RUNNING_SNEAKERS = auto()
    TACTICAL_PADS = auto()
    STALKER_BOOTS = auto()
    COVERT_SNEAKERS = auto()


class Gear(Enum):
    MISSION_CONTROL = auto()
    BONE_CONDUCTION = auto()
    MAG_HOLSTER = auto()
    BLACKLIGHT_FLASHLIGHT = auto()
    LR_DETECTOR = auto()
    IDENTIFICATION_SYSTEM = auto()
    DATA_JACKER = auto()
    SIGNAL_JAMMER = auto()
    HIJACKED_IFF_STROBE = auto()
    GHOST_TV_CAMO = auto()
    EOD_PADDING = auto()
