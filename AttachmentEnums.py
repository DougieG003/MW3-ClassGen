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


class Optics(Enum):
    # SVA545, 
    NO_MODIFICATIONS = auto()
    KR_INTLAS_LSJ_3 = auto() #aftermarket
    SLATE_REFLECTOR = auto()
    JAK_BULLSEYE = auto()
    SLIMLINE_PRO = auto()
    SZ_MINI = auto()
    CRONEN_MINI_DOT = auto()
    CRONEN_MINI_PRO = auto()
    SZ_SIGMA_IV_OPTIC = auto()
    SZ_MINITAC_40 = auto()
    QTG_REFLEX_SIGHT = auto()
    CAUCASUS_REFLEX_SIGHT = auto()
    MK3_REFLECTOR = auto()
    RHINO_REFLEX = auto()
    XRK_ON_POINT_OPTIC = auto()
    AIM_OP_V4 = auto()
    DF105_REFLEX_SIGHT = auto()
    MONOCLE_CT90 = auto()
    CORVUS_SQL_76 = auto()
    SZ_RECHARGE_DX = auto()
    SZ_SRO_7 = auto()
    CORIO_RE_X_PRO = auto()
    CHRIOS_HOLO = auto()
    CORIO_ENFORCER_OPTIC = auto()
    SZ_LONEWOLF_OPTIC = auto()
    KAZAN_HOLO = auto()
    SZ_BATTLE_OPTIC = auto()
    CORVUS_DOWNRANGE_00 = auto()
    XTEN_ANGEL_40 = auto()
    SZ_HOLOTHERM = auto()
    CORIO_ELT_10_2p5 = auto()
    KR_MORTIS_PRECISION_2p5X = auto()
    SL_TRUESIGHT_2p5X = auto()
    KR_MARAUDER_9_RISER = auto()
    TOS_NIGHTFALL_2p5X_THERMAL_OPTIC = auto()
    AOK_4p0X_RQ_9_RECON = auto()
    TX4_HAVOC = auto()
    VLK_4p0_OPTIC = auto()
    SCHLAGER_3p4X = auto()
    FORGE_TAC_DELTA_4 = auto()
    CRONEN_ZERO_P_OPTIC = auto()
    SZ_BULLSEYE_OPTIC = auto()
    SZ_AGGRESSOR_IR_OPTIC = auto()
    SCHLAGER_NIGHT_VIEW = auto()
    VX350_THERMAL_OPTIC = auto()
    TEPLO_OP3_SCOPE = auto()
    HEINRICHTER_HYBRID_SCOPE = auto()
    CORVUS_GHOSTVIEW = auto()
    DR582_HYBRID_SIGHT = auto()
    HYBRID_FIREPOINT = auto()
    SZ_VOREX_90 = auto()
    BPZ40_HYBRID = auto()
    SZ_OSCAR_9 = auto()
    ANGEL_40_4p8X = auto()
    THERMO_OPTIC_X9 = auto()
    TEPLO_CLEAR_SHOT = auto()
    FTAC_CHARLIE7 = auto()
    HMW_20_OPTIC = auto()
    LUCA_BANDERA_SCOPE = auto()
    DS_FARSIGHT_11 = auto()
    RFL_OPTIC_3X = auto()
    DREXSOM_PRIME_90 = auto()
    ARES_CLEAR_SHOT = auto()
    VIGILANT_30_C_IRON = auto()
    XTEN_ERX_10_MINI = auto()
    KR_MINITAC_40_RISER = auto()
    FSS_SPECTRE_MICROTHERM = auto()
    NYDAR_MODEL_2023 = auto()
    DRAGONS_EYE_OPTIC = auto()
    KR_V4_1X_RISER = auto()
    TPS_INCENDIO_REFLEX = auto()
    CORIO_EAGLESEYE_2p5X = auto()
    SZ_HM5_PRECISION_HYBRID_OPTIC = auto()
    CRONEN_INTLAS_MSP_12 = auto()
    INTLAS_CAS_14 = auto()



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
