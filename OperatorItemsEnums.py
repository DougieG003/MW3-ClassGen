"""
Enums to hold names of gear.
"""

from enum import Enum

class Vest(Enum):
    INFANTRY_VEST = "INFANTRY VEST"
    ENGINEER_VEST = "ENGINEER VEST"
    GUNNER_VEST = "GUNNER VEST"
    DEMOLITION_VEST = "DEMOLITION VEST"
    CCT_COMMS_VEST = "CCT COMMS VEST"
    OVERKILL_VEST = "OVERKILL VEST"
    ASSASSIN_VEST = "ASSASSIN VEST"


class Tactical(Enum):
    STUN_GRENADE = "STUN GRENADE"
    BATTLE_RAGE = "BATTLE RAGE"
    SMOKE_GRENADE = "SMOKE GRENADE"
    SCATTER_MINE = "SCATTER MINE"
    DECOY_GRENADE = "DECOY GRENADE"
    FLASH_GRENADE = "FLASH GRENADE"
    SNAPSHOT_GRENADE = "SNAPSHOT GRENADE"
    SHOCK_STICK = "SHOCK STICK"
    STIM = "STIM"
    TEAR_GAS = "TEAR GAS"
    EMD_GRENADE = "EMD GRENADE"


class Lethal(Enum):
    FRAG_GRENADE = "FRAG GRENADE"
    CLAYMORE = "CLAYMORE"
    THROWING_KNIFE = "THROWING KNIFE"
    THERMITE_GRENADE = "THERMITE"
    THERMOBARIC_GRENADE = "THERMOBARIC GRENADE"
    PROXIMITY_MINE = "PROXIMITY MINE"
    DRILL_CHARGE = "DRILL CHARGE"
    SEMTEX = "SEMTEX"
    C4 = "C4"
    BREACHER_DRONE = "BREACHER DRONE"
    THROWING_STAR = "TROWING STAR"
    MOLOTOV_COCKTAIL = "MOLOTOV COCKTAIL"


class FieldUpgrade(Enum):
    HEARTBEAT_SENSOR = "HEARTBEAT SENSOR"
    TACTICAL_INSERTION = "TACTICAL INSERTION"
    TROPHY_SYSTEM = "TROPHY SYSTEM"
    COMM_SCRAMBLER = "COMM SCRAMBLER"
    MED_BOX = "MED BOX"
    INFLATABLE_DECOY = "INFLATABLE DECOY"
    ACS = "A.C.S."
    TACTICAL_CAMERA = "TACTICAL CAMERA"
    MUNITIONS_BOX = "MUNITIONS BOX"
    DEPLOYABLE_COVER = "DEPLOYABLE COVER"
    DDOS = "DDOS"
    RECON_DRONE = "RECON DRONE"
    DEAD_SILENCE = "DEAD SILENCE"
    LOADOUT_DROP = "LOADOUT DROP"
    PORTABLE_RADAR = "PORTABLE RADAR"
    SMOKE_AIRDROP = "SMOKE AIRDROP"
    SUPPRESSION_MINE = "SUPPRESSION MINE"
    ANTI_ARMOR_ROUNDS = "ANTI-ARMOR ROUNDS"


class Gloves(Enum):
    QUICK_GRIP_GLOVES = "QUICK GRIP GLOVES"
    ORDNANCE_GLOVES = "ORDNANCE GLOVES"
    COMMANDO_GLOVES = "COMMANDO GLOVES"
    SCAVENGER_GLOVES = "SCAVENGER GLOVES"
    MARKSMAN_GLOVES = "MARKSMAN GLOVES"
    ASSAULT_GLOVES = "ASSAULT GLOVES"


class Boots(Enum):
    LIGHTWEIGHT_BOOTS = "LIGHTWEIGHT BOOTS"
    CLIMBING_BOOTS = "CLIMBING BOOTS"
    RUNNING_SNEAKERS = "RUNNING SNEAKERS"
    TACTICAL_PADS = "TACTICAL PADS"
    STALKER_BOOTS = "STALKER BOOTS"
    COVERT_SNEAKERS = "COVER SNEAKERS"


class Gear(Enum):
    TAC_MASK = "TAC MASK"
    MISSION_CONTROL_COMLINK = "MISSION CONTROL COMLINK"
    BONE_CONDUCTION_HEADSET = "BONE CONDUCTION HEADSET"
    MAG_HOLSTER = "MAG HOLSTER"
    BLACKLIGHT_FLASHLIGHT = "BLACKLIGHT FLASHLIGHT"
    LR_DETECTOR = "L/R DETECOR"
    THREAT_IDENTIFICATION_SYSTEM = "THREAT IDENTIFICATION SYSTEM"
    DATA_JACKER = "DATA JACKER"
    SIGNAL_JAMMER = "SIGNAL JAMMER"
    HIJACKED_IFF_STROBE = "HIJACKED IFF STROBE"
    GHOST_TV_CAMO = "GHOST T/V CAMO"
    EOD_PADDING = "EOD PADDING"