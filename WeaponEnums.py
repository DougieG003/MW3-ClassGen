"""
Enums to hold the names of all weapons.
"""

from enum import Enum

class AssaultRifles(Enum):
    BP50 = "BP50"
    SVA_545 = "SVA 545"
    RAM_7 = "RAM-7"
    MTZ_556 = "MTZ-556"
    HOLGER_556 = "HOLGER 556"
    MCW = "MCW"
    DG_56 = "DG-56"
    FR_556 = "FR 5.56"
    TAQ_56 = "TAQ-56"
    M4 = "M4"
    STB_556 = "STB 556"
    KASTOV_762 = "KASTOV 762"
    M13B = "M13B"
    CHIMERA = "CHIMERA"
    ISO_HEMLOCK = "ISO HEMLOCK"
    TEMPUS_RAZORBACK = "TEMPUS RAZORBACK"
    FR_AVANCER = "FR AVANCER"
    M13C = "M13C"
    TR_76_GEIST = "TR-76 GEIST"
    LACHMAN_556 = "LACHMANN-556"
    M16 = "M16"
    KASTOV_74U = "KASTOV-74U"
    KASTOV_545 = "KASTOV 545"


class BattleRifles(Enum):
    BAS_B = "BAS-B"
    SIDEWINDER = "SIDEWINDER"
    MTZ_762 = "MTZ-762"
    LACHMAN_762 = "LACHMANN-762"
    CRONEN_SQUALL = "CRONEN SQUALL"
    FTAC_RECON = "FTAC RECON"
    TAQ_V = "TAQ-V"
    SO_14 = "SO-14"


class SMGS(Enum):
    RAM_9 = "RAM-9"
    STRIKER = "STRIKER"
    HRM_9 = "HRM-9"
    WSP_SWARM = "WSP SWARM"
    AMR9 = "AMR9"
    WSP_9 = "WSP-9"
    RIVAL_9 = "RIVAL-9"
    STRIKER_9 = "STRIKER 9"
    LACHMANN_SHROUD = "LACHMANN SHROUD"
    ISO_9MM = "ISO 9MM"
    PDSW_528 = "PDSW 528"
    VEL_46 = "VEL 46"
    FENNEC_45 = "FENNEC 45"
    BAS_P = "BAS-P"
    ISO_45 = "ISO 45"
    LACHMANN_SUB = "LACHMANN SUB"
    FSS_HURRICANE = "FSS HURRICANE"
    MX9 = "MX9"
    MINIBAK = "MINIBAK"
    VAZNEV_9K = "VAZNEV-9K"


class Shotguns(Enum):
    LOCKWOOD_680 = "LOCKWOOD 680"
    HAYMAKER = "HAYMAKER"
    RIVETER = "RIVETER"
    LOCKWOOD_300 = "LOCKWOOD 300"
    EXPEDITE_12 = "EXPEDITE 12"
    BRYSON_800 = "BRYSON 800"
    KV_BROADSIDE = "KV BROADSIDE"
    MX_GUARDIAN = "MX GUARDIAN"
    BRYSON_890 = "BRYSON 890"


class LMGS(Enum):
    TAQ_EVOLVERE = "TAQ EVOLVERE"
    PULEMYOT_762 = "PULEMYOT 762"
    DG_58_LSW = "DG-58 LSW"
    BRUEN_MK9 = "BRUEN MK9"
    TAQ_ERADICATOR = "TAQ ERADICATOR"
    HOLGER_26 = "HOLGER 26"
    SAKIN_MG38 = "SAKIN MG38"
    RAAL_MG = "RAAL MG"
    ICARUS_556 = "556 ICARUS"
    RAPP_H = "RAPP H"
    HCR_56 = "HCR 56"
    RPK = "RPK"


class MarksmanRifles(Enum):
    KVD_ENFORCER = "KVD ENFORCER"
    MCW_68 = "MCW 6.8"
    DM56 = "DM56"
    MTZ_INTERCEPTOR = "MTZ INTERCEPTOR"
    EBR_14 = "EBR-14"
    SP_R_208 = "SP-R 208"
    LOCKWOOD_MK2 = "LOCKWOOD MK2"
    TEMPUS_TORRENT = "TEMPUS TORRENT"
    CROSSBOW = "CROSSBOW"
    LM_S = "LM-S"
    SA_B_50 = "SA-B 50"
    TAQ_M = "TAZ-M"


class SniperRifles(Enum):
    XRK_STALKER = "XRK STALKER"
    KATT_AMR = "KATT-AMR"
    LONGBOW = "LONGBOW"
    KV_INHIBITOR = "KV INHIBITOR"
    MCPR_300 = "MCPR-300"
    SIGNAL_50 = "SIGNAL 50"
    VICTUS_XMR = "VICTUS XMR"
    FJX_IMPERIUM = "FJX IMPERIUM"
    CARRACK_300 = "CARRACK .300"
    LA_B_330 = "LA-B 330"
    SP_X_80 = "SP-X 80"


class MeleePrimary(Enum):
    RIOT_SHIELD = "RIOT SHIELD"
    

class HandGuns(Enum):
    COR_45 = "COR-45"
    RENETTI = "RENETTI"
    TYR = "TYR"
    WSP_STINGER = "WSP STINGER"
    P890 = "P890"
    GS_50 = ".50 GS"
    X12 = "X12"
    BASILISK = "BASILISK"
    FTAC_SIEGE = "FTAC SIEGE"
    GS_MAGNA = "GS MAGNA"
    DAEMON_9MM = "9MM DAEMON"
    X13_AUTO = "X13 AUTO"


class Launchers(Enum):
    STORMENDER = "STORMENDER"
    RGL_80 = "RGL-80"
    PILA = "PILA"
    JOKR = "JOKR"
    RPG_7 = "RPG-7"
    STRELA_P = "STRELA-P"


class MeleeSecondary(Enum):
    GUTTER_KNIFE = "GUTTER KNIFE"
    KARAMBIT = "KARAMBIT"
    TONFA = "TONFA"
    COMBAT_KNIFE = "COMBAT KNIFE"
    DUAL_KODACHIS = "DUAL KODACHIS"
    DUAL_KAMAS = "DUAL KAMAS"
    PICKAXE = "PICKAXE"
