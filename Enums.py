"""
Enums to hold names of weapons, attachments, gadgets, and other items.
"""

from enum import Enum

class AssaultRifles(Enum):
    SVA_545 = 1
    RAM_7 = 2
    MTZ_556 = 3
    HOLGER_556 = 4
    MCW = 5
    DG_56 = 6
    FR_556 = 7
    TAQ_56 = 8
    M4 = 9
    STB_556 = 10
    KASTOV_762 = 11
    M13B = 12
    CHIMERA = 13
    ISO_HEMLOCK = 14
    TEMPUS_RAZORBACK = 15
    FR_AVANCER = 16
    M13C = 17
    TR_76_GEIST = 18
    LACHMAN_556 = 19
    M16 = 20
    KASTOV_74U = 21
    KASTOV_545 = 22


class BattleRifles(Enum):
    BAS_B = 1
    SIDEWINDER = 2
    MTZ_762 = 3
    LACHMAN_762 = 4
    CRONEN_SQUALL = 5
    FTAC_RECON = 6
    TAQ_V = 7
    SO_14 = 8


class SMGs(Enum):
    STRIKER = 1
    HRM_9 = 2
    WSP_SWARM = 3
    AMR9 = 4
    WSP_9 = 5
    RIVAL_9 = 6
    STRIKER_9 = 7
    LACHMANN_SHROUD = 8
    ISO_9MM = 9
    PDSW_528 = 10
    VEL_46 = 11
    FENNEC_45 = 12
    BAS_P = 13
    ISO_45 = 14
    LACHMANN_SUB = 15
    FSS_HURRICANE = 16
    MX9 = 17
    MINIBAK = 18
    VAZBEV_9K = 19


class Shotguns(Enum):
    LOCKWOOD_680 = 1
    HAYMAKER = 2
    RIVETER = 3
    LOCKWOOD_300 = 4
    EXPEDITE_12 = 5
    BRYSON_800 = 6
    KV_BROADSIDE = 7
    MX_GUARDIAN = 8
    BRYSON_890 = 9


class LMGs(Enum):
    TAQ_EVOLVERE = 1
    PULEMYOT_762 = 2
    DG_58 = 3
    BRUEN_MK9 = 4
    TAQ_ERADICATOR = 5
    HOLGER_26 = 6
    SAKIN_MG38 = 7
    RAAL_MG = 8
    ICARUS_556 = 9
    RAPP_H = 10
    HCR_56 = 11
    RPK = 12


class MarksmanRifles(Enum):
    KVD_ENFORCER = 1
    MCW_68 = 2
    DM56 = 3
    MTZ_INTERCEPTOR = 4
    EBR_14 = 5
    SP_R_208 = 6
    LOCKWOOD_MK2 = 7
    TEMPUS_TORRENT = 8
    CROSSBOW = 9
    LM_S = 10
    SA_B_50 = 11
    TAQ_M = 12


class SniperRifles(Enum):
    XRK_STALKER = 1
    KATT_AMR = 2
    LONGBOW = 3
    KV_INHIBITOR = 4
    MCPR_300 = 5
    SIGNAL_50 = 6
    VICTUS_XMR = 7
    FJX_IMPERIUM = 8
    CARRACK_300 = 9
    LA_B_330 = 10
    SP_X_80 = 11


class MeleePrimary(Enum):
    RIOT_SHIELD = 1
    

class HandGuns(Enum):
    COR_45 = 1
    RENETTI = 2
    TYR = 3
    WSP_STINGER = 4
    P890 = 5
    GS_50 = 6
    X12 = 7
    BASILISK = 8
    FTAC_SIEGE = 9
    GS_MAGNA = 10
    DAEMON_9MM = 11
    X13_AUTO = 12


class Launchers(Enum):
    STORMENDER = 1
    RGL_80 = 2
    PILA = 3
    JOKR = 4
    RPG_7 = 5
    STRELA_P = 6


class MeleeSecondary(Enum):
    GUTTER_KNIFE = 1
    KARAMBIT = 2
    TONFA = 3
    COMBAT_KNIFE = 4
    DUAL_KODACHIS = 5
    DUAL_KAMAS = 6
    PICKAXE = 7


class Attachments(Enum):
    MUZZLE = 1
    BARREL = 2
    LASER = 3
    OPTIC = 4
    STOCK = 5
    COMB = 6
    BOLT = 7
    REAR_GRIP = 8
    MAGAZINE = 9
    TRIGGER_ACTION = 10
    AMMO_TYPE = 11
    UNDERBARREL = 12