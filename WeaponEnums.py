"""
Enums to hold names of weapons and sort into primary and secondary Enums.
"""

from enum import Enum, auto

class AssaultRifles(Enum):
    SVA_545 = auto()
    RAM_7 = auto()
    MTZ_556 = auto()
    HOLGER_556 = auto()
    MCW = auto()
    DG_56 = auto()
    FR_556 = auto()
    TAQ_56 = auto()
    M4 = auto()
    STB_556 = auto()
    KASTOV_762 = auto()
    M13B = auto()
    CHIMERA = auto()
    ISO_HEMLOCK = auto()
    TEMPUS_RAZORBACK = auto()
    FR_AVANCER = auto()
    M13C = auto()
    TR_76_GEIST = auto()
    LACHMAN_556 = auto()
    M16 = auto()
    KASTOV_74U = auto()
    KASTOV_545 = auto()


class BattleRifles(Enum):
    BAS_B = auto()
    SIDEWINDER = auto()
    MTZ_762 = auto()
    LACHMAN_762 = auto()
    CRONEN_SQUALL = auto()
    FTAC_RECON = auto()
    TAQ_V = auto()
    SO_14 = auto()


class SMGs(Enum):
    STRIKER = auto()
    HRM_9 = auto()
    WSP_SWARM = auto()
    AMR9 = auto()
    WSP_9 = auto()
    RIVAL_9 = auto()
    STRIKER_9 = auto()
    LACHMANN_SHROUD = auto()
    ISO_9MM = auto()
    PDSW_528 = auto()
    VEL_46 = auto()
    FENNEC_45 = auto()
    BAS_P = auto()
    ISO_45 = auto()
    LACHMANN_SUB = auto()
    FSS_HURRICANE = auto()
    MX9 = auto()
    MINIBAK = auto()
    VAZBEV_9K = auto()


class Shotguns(Enum):
    LOCKWOOD_680 = auto()
    HAYMAKER = auto()
    RIVETER = auto()
    LOCKWOOD_300 = auto()
    EXPEDITE_12 = auto()
    BRYSON_800 = auto()
    KV_BROADSIDE = auto()
    MX_GUARDIAN = auto()
    BRYSON_890 = auto()


class LMGs(Enum):
    TAQ_EVOLVERE = auto()
    PULEMYOT_762 = auto()
    DG_58 = auto()
    BRUEN_MK9 = auto()
    TAQ_ERADICATOR = auto()
    HOLGER_26 = auto()
    SAKIN_MG38 = auto()
    RAAL_MG = auto()
    ICARUS_556 = auto()
    RAPP_H = auto()
    HCR_56 = auto()
    RPK = auto()


class MarksmanRifles(Enum):
    KVD_ENFORCER = auto()
    MCW_68 = auto()
    DM56 = auto()
    MTZ_INTERCEPTOR = auto()
    EBR_14 = auto()
    SP_R_208 = auto()
    LOCKWOOD_MK2 = auto()
    TEMPUS_TORRENT = auto()
    CROSSBOW = auto()
    LM_S = auto()
    SA_B_50 = auto()
    TAQ_M = auto()


class SniperRifles(Enum):
    XRK_STALKER = auto()
    KATT_AMR = auto()
    LONGBOW = auto()
    KV_INHIBITOR = auto()
    MCPR_300 = auto()
    SIGNAL_50 = auto()
    VICTUS_XMR = auto()
    FJX_IMPERIUM = auto()
    CARRACK_300 = auto()
    LA_B_330 = auto()
    SP_X_80 = auto()


class MeleePrimary(Enum):
    RIOT_SHIELD = auto()
    

class HandGuns(Enum):
    COR_45 = auto()
    RENETTI = auto()
    TYR = auto()
    WSP_STINGER = auto()
    P890 = auto()
    GS_50 = auto()
    X12 = auto()
    BASILISK = auto()
    FTAC_SIEGE = auto()
    GS_MAGNA = auto()
    DAEMON_9MM = auto()
    X13_AUTO = auto()


class Launchers(Enum):
    STORMENDER = auto()
    RGL_80 = auto()
    PILA = auto()
    JOKR = auto()
    RPG_7 = auto()
    STRELA_P = auto()


class MeleeSecondary(Enum):
    GUTTER_KNIFE = auto()
    KARAMBIT = auto()
    TONFA = auto()
    COMBAT_KNIFE = auto()
    DUAL_KODACHIS = auto()
    DUAL_KAMAS = auto()
    PICKAXE = auto()


class PrimaryWeapon(Enum):
    ASSAULT_RIFLE = AssaultRifles
    BATTLE_RIFLE = BattleRifles
    SMG = SMGs
    SHOTGUN = Shotguns
    LMG = LMGs
    MARKSMAN_RIFLE = MarksmanRifles
    SNIPER_RIFLE = SniperRifles
    MELEE = MeleePrimary


class SecondaryWeapon(Enum):
    HANDGUN = HandGuns
    LAUNCHER = Launchers
    MELEE = MeleeSecondary

