"""
Enums and dictionary to hold names and attributes of optic attachments.
"""

from enum import Enum
from Weapons import *

invalid_weapons_str = "invalid_weapons"
aftermarket_str = "aftermarket"

# AR BR MeleePrimary MeleeSecondary

class Optics(Enum):
    NO_MODIFICATIONS = "NO MODIFICATIONS"
    KR_INTLAS_LSJ_3 = "KR INTLAS LSJ-3"
    SLATE_REFLECTOR = "SLATE REFLECTOR"
    JAK_BULLSEYE = "JAK BULLSEYE"
    SLIMLINE_PRO = "SLIMLINE PRO"
    SZ_MINI = "SZ MINI"
    CRONEN_MINI_DOT = "CRONEN MINI DOT"
    CRONEN_MINI_PRO = "CRONEN MINI PRO"
    SZ_SIGMA_IV_OPTIC = "SZ SIGMA-IV OPTIC"
    SZ_MINITAC_40 = "SZ_MINITAC-40"
    QTG_REFLEX_SIGHT = "QTG REFLEX SIGHT"
    CAUCASUS_REFLEX_SIGHT = "CAUCASUS REFLEX SIGHT"
    MK3_REFLECTOR = "MK. 3 REFLECTOR"
    RHINO_REFLEX = "RHINO REFLEX"
    XRK_ON_POINT_OPTIC = "XRK ON-POINT OPTIC"
    AIM_OP_V4 = "AIM OP-V4"
    DF105_REFLEX_SIGHT = "DF105 REFLEX SIGHT"
    MONOCLE_CT90 = "MONOCLE CT90"
    CORVUS_SOL_76 = "CORVUS SOL-76"
    SZ_RECHARGE_DX = "SZ RECHARGE-DX"
    SZ_SRO_7 = "SZ SRO-7"
    CORIO_RE_X_PRO = "CORIO RE-X PRO"
    CHRIOS_HOLO = "CHRIOS HOLO"
    CORIO_ENFORCER_OPTIC = "CORIO ENFORCER OPTIC"
    SZ_LONEWOLF_OPTIC = "SZ LONEWOLF OPTIC"
    KAZAN_HOLO = "KAZAN-HOLO"
    SZ_BATTLE_OPTIC = "SZ BATTLE OPTIC"
    CORVUS_DOWNRANGE_00 = "CORVUS DOWNRANGE-00"
    XTEN_ANGEL_40 = "XTEN ANGEL-40"
    SZ_HOLOTHERM = "SZ HOLOTHERM"
    CORIO_ELT_10_2p5 = "CORIO ELT-10 2.5"
    KR_MORTIS_PRECISION_2p5X = "KR MORTIS PRECISION 2.5X"
    SL_TRUESIGHT_2p5X = "SL TRUESIGHT 2.5X"
    KR_MARAUDER_9_RISER = "KR MARAUDER 9 RISER"
    TOS_NIGHTFALL_2p5X_THERMAL_OPTIC = "TOS NIGHTFALL 2.5X THERMAL OPTIC"
    AOK_4p0X_RQ_9_RECON = "AOK 4.0X RQ-9 RECON"
    TX4_HAVOC = "TX4 HAVOC"
    VLK_4p0_OPTIC = "VLK 4.0 OPTIC"
    SCHLAGER_3p4X = "SCHLAGER 3.4X"
    FORGE_TAC_DELTA_4 = "FORGE TAC DELTA 4"
    CRONEN_ZERO_P_OPTIC = "CRONEN ZERO-P OPTIC"
    SZ_BULLSEYE_OPTIC = "SZ BULLSEYE OPTIC"
    SZ_AGGRESSOR_IR_OPTIC = "SZ AGGRESSOR-IR OPTIC"
    SCHLAGER_NIGHT_VIEW = "SCHLAGER NIGHT VIEW"
    VX350_THERMAL_OPTIC = "VX350 THERMAL OPTIC"
    TEPLO_OP3_SCOPE = "TEPLO-OP3 SCOPE"
    HEINRICHTER_HYBRID_SCOPE = "HEINRICHTER HYBRID SCOPE" #smg
    CORVUS_GHOSTVIEW = "CORVUS GHOSTVIEW"
    DR582_HYBRID_SIGHT = "DR582 HYBRID SIGHT"
    HYBRID_FIREPOINT = "HYBRID FIREPOINT"
    SZ_VOREX_90 = "SZ VOREX-90"
    BPZ40_HYBRID = "BPZ40 HYBRID"
    SZ_OSCAR_9 = "SZ OSCAR-9"
    ANGEL_40_4p8X = "ANGEL-40 4.8X" #smg
    THERMO_OPTIC_X9 = "THERMO-OPTIC X9"
    TEPLO_CLEAR_SHOT = "TEPLO CLEAR SHOT"
    FTAC_CHARLIE7 = "FTAC CHARLIE7"  #smg
    HMW_20_OPTIC = "HMW-20 OPTIC"  #smg
    LUCA_BANDERA_SCOPE = "LUCA BANDERA SCOPE"  #smg
    DS_FARSIGHT_11 = "DS FARSIGHT 11"  #smg
    RFL_OPTIC_3X = "3X RFL-OPTIC"   #smg
    DREXSOM_PRIME_90 = "DREXSOM PRIME-90"  #smg
    ARES_CLEAR_SHOT = "ARES CLEAR SHOT"  #smg
    VIGILANT_30_C_IRON = "VIGILANT-30 C-IRON"  #smg
    LUCA_CANIS_4X_OPTIC = "LUCA CANIS 4X OPTIC"  #smg
    XTEN_ERX_10_MINI = "XTEN ERX-10 MINI"
    KR_MINITAC_40_RISER = "KR MINITAC-40 RISER"
    FSS_SPECTRE_MICROTHERM = "FSS SPECTRE MICROTHERM"
    NYDAR_MODEL_2023 = "NYDAR MODEL 2023"
    DRAGONS_EYE_OPTIC = "DRAGONS' EYE OPTIC"
    KR_V4_1X_RISER = "KR V4 1X RISER"
    TPS_INCENDIO_REFLEX = "TPS INCENDIO REFLEX"
    CORIO_EAGLESEYE_2p5X = "CORIO EAGLESEYE 2.5X"
    SZ_HM5_PRECISION_HYBRID_OPTIC = "SZ HM5 PRECISION HYBRID OPTIC"
    CRONEN_INTLAS_MSP_12 = "CRONEN INTLAS MSP-12"
    INTLAS_CAS_14 = "INTLAS CAS-14"


# create a dictionary with key as name of optic, and properties for use in class generator
optics_dict = {}
optics_dict[Optics.AIM_OP_V4.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.ANGEL_40_4p8X.value] = {
    invalid_weapons_str: [
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.AOK_4p0X_RQ_9_RECON.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.ARES_CLEAR_SHOT.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_74U.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.BPZ40_HYBRID.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CAUCASUS_REFLEX_SIGHT.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CHRIOS_HOLO.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CORIO_EAGLESEYE_2p5X.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CORIO_ELT_10_2p5.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CORIO_ENFORCER_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CORIO_RE_X_PRO.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CORVUS_DOWNRANGE_00.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CORVUS_GHOSTVIEW.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CORVUS_SOL_76.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CRONEN_INTLAS_MSP_12.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: True
}

optics_dict[Optics.CRONEN_MINI_DOT.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CRONEN_MINI_PRO.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.CRONEN_ZERO_P_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.DF105_REFLEX_SIGHT.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.DR582_HYBRID_SIGHT.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.DRAGONS_EYE_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.DREXSOM_PRIME_90.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_74U.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.DS_FARSIGHT_11.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_74U.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.FORGE_TAC_DELTA_4.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.FSS_SPECTRE_MICROTHERM.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.FTAC_CHARLIE7.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_74U.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.HEINRICHTER_HYBRID_SCOPE.value] = {
    invalid_weapons_str: [
        AssaultRifles.TEMPUS_RAZORBACK.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.HMW_20_OPTIC.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_74U.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.HYBRID_FIREPOINT.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.INTLAS_CAS_14.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: True
}

optics_dict[Optics.JAK_BULLSEYE.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.KAZAN_HOLO.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.KR_INTLAS_LSJ_3.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: True
}

optics_dict[Optics.KR_MARAUDER_9_RISER.value] = {
    invalid_weapons_str: [
        AssaultRifles.M16.value, 
        AssaultRifles.FR_AVANCER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.KR_MINITAC_40_RISER.value] = {
    invalid_weapons_str: [
        AssaultRifles.M16.value, 
        AssaultRifles.FR_AVANCER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.KR_MORTIS_PRECISION_2p5X.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.KR_V4_1X_RISER.value] = {
    invalid_weapons_str: [
        AssaultRifles.M16.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.LUCA_BANDERA_SCOPE.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_74U.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.LUCA_CANIS_4X_OPTIC.value] = {
    invalid_weapons_str: [
        AssaultRifles.CHIMERA.value,
        AssaultRifles.DG_56.value,
        AssaultRifles.FR_556.value,
        AssaultRifles.FR_AVANCER.value,
        AssaultRifles.HOLGER_556.value,
        AssaultRifles.ISO_HEMLOCK.value,
        AssaultRifles.KASTOV_545.value,
        AssaultRifles.KASTOV_74U.value,
        AssaultRifles.KASTOV_762.value,
        AssaultRifles.LACHMAN_556.value,
        AssaultRifles.M13B.value,
        AssaultRifles.M13C.value,
        AssaultRifles.M16.value,
        AssaultRifles.M4.value,
        AssaultRifles.MCW.value,
        AssaultRifles.MTZ_556.value,
        AssaultRifles.RAM_7.value,
        AssaultRifles.SVA_545.value,
        AssaultRifles.TAQ_56.value,
        AssaultRifles.TEMPUS_RAZORBACK.value,
        AssaultRifles.TR_76_GEIST.value,
        BattleRifles.BAS_B,
        BattleRifles.SIDEWINDER,
        BattleRifles.MTZ_762,
        BattleRifles.LACHMAN_762,
        BattleRifles.CRONEN_SQUALL,
        BattleRifles.FTAC_RECON,
        BattleRifles.TAQ_V,
        BattleRifles.SO_14,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.MK3_REFLECTOR.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.MONOCLE_CT90.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.NO_MODIFICATIONS.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.NYDAR_MODEL_2023.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.QTG_REFLEX_SIGHT.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.RFL_OPTIC_3X.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_74U.value,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.RHINO_REFLEX.value] = {
    invalid_weapons_str: [
        AssaultRifles.LACHMAN_556.value, 
        AssaultRifles.KASTOV_74U.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SCHLAGER_3p4X.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SCHLAGER_NIGHT_VIEW.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SL_TRUESIGHT_2p5X.value] = {
    invalid_weapons_str: [
        AssaultRifles.DG_56.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SLATE_REFLECTOR.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SLIMLINE_PRO.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_AGGRESSOR_IR_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_BATTLE_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_BULLSEYE_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_HM5_PRECISION_HYBRID_OPTIC.value] = {
    invalid_weapons_str: [
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_HOLOTHERM.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_LONEWOLF_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_MINI.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_MINITAC_40.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_OSCAR_9.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_RECHARGE_DX.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_SIGMA_IV_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.SZ_SRO_7.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.TEPLO_CLEAR_SHOT.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.TEPLO_OP3_SCOPE.value] = {
    invalid_weapons_str: [
        AssaultRifles.FR_AVANCER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.THERMO_OPTIC_X9.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.TOS_NIGHTFALL_2p5X_THERMAL_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.TPS_INCENDIO_REFLEX.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.TX4_HAVOC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.VIGILANT_30_C_IRON.value] = {
    invalid_weapons_str: [
        AssaultRifles.KASTOV_762.value,
        AssaultRifles.M4.value,
        AssaultRifles.TEMPUS_RAZORBACK.value,
        AssaultRifles.FR_AVANCER.value,
        AssaultRifles.LACHMAN_556.value,
        AssaultRifles.M16.value,
        AssaultRifles.KASTOV_74U.value,
        AssaultRifles.KASTOV_545.value,
        BattleRifles.LACHMAN_762,
        BattleRifles.FTAC_RECON,
        BattleRifles.SO_14,
        SMGS.STRIKER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.VLK_4p0_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.VX350_THERMAL_OPTIC.value] = {
    invalid_weapons_str: [
        AssaultRifles.DG_56.value, 
        AssaultRifles.FR_AVANCER.value,
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.XRK_ON_POINT_OPTIC.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.XTEN_ANGEL_40.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}

optics_dict[Optics.XTEN_ERX_10_MINI.value] = {
    invalid_weapons_str: [
        MeleePrimary.RIOT_SHIELD.value,
        MeleeSecondary.COMBAT_KNIFE.value,
        MeleeSecondary.DUAL_KAMAS.value,
        MeleeSecondary.DUAL_KODACHIS.value,
        MeleeSecondary.GUTTER_KNIFE.value,
        MeleeSecondary.KARAMBIT.value,
        MeleeSecondary.PICKAXE.value,
        MeleeSecondary.TONFA.value,
        Launchers.JOKR.value,
        Launchers.PILA.value,
        Launchers.RGL_80.value,
        Launchers.RPG_7.value,
        Launchers.STORMENDER.value,
        Launchers.STRELA_P.value,
    ],
    aftermarket_str: False
}
