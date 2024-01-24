"""
Enums to hold names of attachments.
"""

from enum import Enum, auto


class AssaultRifleMuzzles(Enum):
    # SVA545, MTZ556, HOLGER556, MCW, DG56, TAQ56, M4, STB556, M13B, ISO HEMLOCK, TEMPUS RAVORBACK, FR AVANCER, 
    # M13C, LACHMANN556, M16, KASTOV74U, KASTOV545
    # CHIMERA HAS NO MUZZLE
    SHADOWSTRIKE_SUPPRESSOR = auto()
    HMRES_MOD_SUPPRESSOR = auto()
    SONIC_SUPPRESSOR = auto()
    COLOSSUS_SUPPRESSOR = auto()
    BROADHEAD_3DP = auto()
    SILENTFIRE_XG6 = auto()
    ECHOLINE_GSX = auto() #KASTOV762
    ZULU_60 = auto() #KASTOV762
    HARBINGER_D20 = auto()
    ECHOLESS_80 = auto()
    FSS_COVERT_V = auto()
    GAUGE_9_MONO = auto()
    ELR_BLACKFIRE_COMPENSATOR = auto()
    WRATHGUARD_COMPENSATOR = auto()
    T4LR_SABER_COMPENSATOR = auto()
    EX01_MATCH_COMPENSATOR = auto()
    T51R_BILLETED_BREAK = auto()
    PURIFIER_MUZZLE_BREAK = auto()
    CASUS_BREAK = auto()
    JAK_BFB = auto() #KASTOV762
    RF_CROWN_50 = auto()
    KOMODO_HEAVY = auto()
    XTEN_PORTED_290 = auto()
    FJX_FULCRUM_PRO = auto()
    CRONEN_OP44 = auto()
    FTAC_CASTLE_COMP = auto()
    XTEN_HAVOC_90 = auto()
    SAKIN_TREAD_40 = auto() #KASTOV762
    S37C_DL_BREACHER_DEVICE = auto()
    C400_DOOR_KNOCKER = auto()
    JCZ_390_MUZZLE_DEVICE = auto()
    L4R_FLASH_HIDER = auto() #KASTOV762
    CORVUS_SLASH_GEN2 = auto()
    CRONEN_MAW_86 = auto()
    DARK_KX30 = auto()
    VLK_KOLOSS_FLASH_HIDER = auto()
    VT7_SPIRITFIRE_SUPPRESSOR = auto()
    MONOLITHIC_SUPPRESSOR = auto()
    STER45_SKYFURY_COMPENSATOR = auto()
    ENDLESS_30_COMPENSATOR = auto()
    ZEHMN35_COMPENSATED_FLASH_HIDER = auto() #KASTOV762

    # KASTOV762 ONLY
    VT7_SPIRITFIRE_SUPPRESSOR_L = auto()
    HMRES_MOD_SUPPRESSOR_L = auto()
    BRUENEN_HARMONIC_SUPPRESSOR = auto()
    HUSHER_65_SILENCER = auto()
    FR_TITAN_SILENCER = auto()
    POLOARFIRE_S = auto()
    ZLR_TALON_5 = auto()
    KASTOVIA_DX90 = auto()
    CRONEN_SPDR = auto()
    STER45_SKYFURY_COMPENSATOR_L = auto()
    ELR_BLACKFIRE_COMPENSATOR_L = auto()
    T4LR_SABER_COMPENSATOR_L = auto()
    EX01_MATCH_COMPENSATOR_L = auto()
    PURIFIER_MUZZLE_BREAK_L = auto()
    CASUS_BREAK_L = auto()
    TEMPUS_GH50 = auto()
    TY_LR8 = auto()
    LOCKSHOT_KT85 = auto()
    SA_LEVELER_55 = auto()
    BORE_490 = auto()
    GL_CLEAR_BREACH = auto()
    TA_HULL_BREACH_KL = auto()
    EIGHT_POINT_FLASH_HIDER = auto()
    TZL_90_V3 = auto()
    CRONEN_DARK_KX30 = auto()
    MONOLITHIC_SUPPRESSOR_L = auto()
    SONIC_SUPPRESSOR_L = auto()
    COLOSSUS_SUPPRESSOR_L = auto()
    WRATHGUARD_COMPENSATOR_L = auto()
    T51R_BILLETED_BREAK_L = auto()
    S37C_DL_BREACHER_DEVICE_L = auto()


class AmmoTypes(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()





class Barrels(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Lasers(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Optics(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class RearGrips(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Magazines(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class TriggerActions(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Combs(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Bolts(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Stocks(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Underbarrels(Enum):
    FRANGIBLE = auto()
    HOLLOWPOINT = auto()
    TRACER = auto()
    ARMOR_PIERCING = auto()
    OVERPRESSURE_P = auto()
    INCENDIARY = auto()
    LOW_GRAIN_ROUNDS = auto()
    HIGH_GRAIN_ROUNDS = auto()
    HIGH_VELOCITY = auto()
    ROUND_NOSE = auto()
    MONO = auto()
    HARDENED = auto()
    AUTO_AET = auto()
    EXPLOSIVE = auto()
    SPIRE_POINT = auto()
    BALL = auto()
    SLUG = auto()
    SNAKESHOT = auto()


class Attachments(Enum):
    MUZZLE = Muzzles
    BARREL = Barrels
    LASER = Lasers
    OPTIC = Optics
    STOCK = Stocks
    COMB = Combs
    BOLT = Bolts
    REAR_GRIP = RearGrips
    MAGAZINE = Magazines
    TRIGGER_ACTION = TriggerActions
    AMMO_TYPE = AmmoTypes
    UNDERBARREL = Underbarrels
