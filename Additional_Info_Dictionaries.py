"""File for storing information about weapons and attachments."""
from enum import Enum
from datetime import date

from WeaponEnums import (
    AssaultRifles,
    BattleRifles,
    SMGS,
    Shotguns,
    LMGS,
    MarksmanRifles,
    SniperRifles,
    MeleePrimary,
    HandGuns,
    Launchers,
    MeleeSecondary,
)
from AttachmentEnums import (
    Muzzles,
    Barrels,
    Arms,
    Lasers,
    Optics,
    Stocks,
    Combs,
    Guards,
    Bolts,
    Levers,
    RearGrips,
    TriggerActions,
    Magazines,
    Wires,
    AmmoTypes,
    Underbarrels,
    CarryHandles,
    ConversionKits,
)
from OperatorItemsEnums import (
    Vest,
    Tactical,
    Lethal,
    FieldUpgrade,
    Gloves,
    Boots,
    Gear,
)

season_str = "season"
battlepass_only_str = "battlepass_only"
start_date_str = "start_date"
end_date_str = "end_date"

class Seasons(Enum):
    LAUNCH = 0
    SEASON_ONE = 1
    SEASON_TWO = 2



season_info_dict = {
    Seasons.SEASON_ONE.name: {
        start_date_str: date(2023, 12, 6),
        end_date_str: date(2024, 2, 6),
    },
    Seasons.SEASON_TWO.name: {
        start_date_str: date(2024, 2, 7),
        end_date_str: date(2024, 4, 2),
    },
}


locked_items_info_dict = {
    "Weapons": {
        "AssaultRifles": {
            AssaultRifles.DG_56.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            AssaultRifles.FR_556.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            AssaultRifles.RAM_7.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            AssaultRifles.TR_76_GEIST.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: True},
            AssaultRifles.BP50.value: {season_str: Seasons.SEASON_TWO.value, battlepass_only_str: True},
        },
        "BattleRifles": {
            BattleRifles.SIDEWINDER.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            BattleRifles.MTZ_762.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            BattleRifles.SOA_SUBVERTER.value: {season_str: Seasons.SEASON_TWO.value, battlepass_only_str: False},
        },
        "SMGS": {
            SMGS.WSP_9.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            SMGS.RIVAL_9.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            SMGS.STRIKER_9.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            SMGS.HRM_9.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: True},
            SMGS.RAM_9.value: {season_str: Seasons.SEASON_TWO.value, battlepass_only_str: True},
        },
        "Shotguns": {
            Shotguns.RIVETER.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
        },
        "LMGS": {
            LMGS.HOLGER_26.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            LMGS.TAQ_ERADICATOR.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            LMGS.TAQ_EVOLVERE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        },
        "MarksmanRifles": {
            MarksmanRifles.MCW_68.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            MarksmanRifles.DM56.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            MarksmanRifles.MTZ_INTERCEPTOR.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
        },
        "SniperRifles": {
            SniperRifles.LONGBOW.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            SniperRifles.KV_INHIBITOR.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            SniperRifles.XRK_STALKER.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        },
        "MeleePrimary": {},
        "Handguns": {
            HandGuns.WSP_STINGER.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
        },
        "Launchers": {
            Launchers.STORMENDER.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        },
        "MeleeSecondary": {
            MeleeSecondary.KARAMBIT.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            MeleeSecondary.SOULRENDER.value: {season_str: Seasons.SEASON_TWO.value, battlepass_only_str: False},
        },
    },
    "AftermarketParts": {
        "Muzzles": {
            Muzzles.JAK_BFB.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
        },
        "Optics": {
            Optics.KR_INTLAS_LSJ_3.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            Optics.CRONEN_INTLAS_MSP_12.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            Optics.INTLAS_CAS_14.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            Optics.JAK_BULLSEYE.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
            Optics.TPS_INCENDIO_REFLEX.value: {season_str: Seasons.LAUNCH.value, battlepass_only_str: False},
        },
        "Underbarrels": {
            Underbarrels.JAK_PURIFIER.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        },
        "Kits": {
            ConversionKits.JAK_SIGNAL_BURST.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.JAK_HEADHUNTER_CARBINE_CONVERSION.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.JAK_ETTIN_DOUBLE_BARREL.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.WSP_AKIMBO_BRACE_STOCK.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.BROODMOTHER_45_KIT.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.XRK_IP_V2_CONVERSION_KIT.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.MCW_6_8_FULL_AUTO_CONVERSION.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.JAK_NIGHTSHADE_RIFLE_KIT.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
            ConversionKits.JAK_RAVEN_KIT.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        },
    },
    "Perks": {
        Vest.ASSASSIN_VEST.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Vest.NINJA_VEST.value: {season_str: Seasons.SEASON_TWO.value, battlepass_only_str: False},
        Gloves.MARKSMAN_GLOVES.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Gloves.ASSAULT_GLOVES.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Boots.COVERT_SNEAKERS.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Gear.THREAT_IDENTIFICATION_SYSTEM.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Gear.DATA_JACKER.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Gear.SIGNAL_JAMMER.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Gear.HIJACKED_IFF_STROBE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Gear.GHOST_TV_CAMO.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
    },
    "Equipment": {
        Lethal.PROXIMITY_MINE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Lethal.DRILL_CHARGE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Lethal.SEMTEX.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Lethal.C4.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Lethal.BREACHER_DRONE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Lethal.MOLOTOV_COCKTAIL.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Tactical.FLASH_GRENADE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Tactical.SNAPSHOT_GRENADE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Tactical.SHOCK_STICK.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Tactical.STIM.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Tactical.TEAR_GAS.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        Tactical.EMD_GRENADE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
    },
    "FieldUpgrades": {
        FieldUpgrade.HEARTBEAT_SENSOR.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.TROPHY_SYSTEM.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.INFLATABLE_DECOY.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.TACTICAL_CAMERA.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.DDOS.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.DEAD_SILENCE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.LOADOUT_DROP.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.SMOKE_AIRDROP.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.SUPPRESSION_MINE.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        FieldUpgrade.ANTI_ARMOR_ROUNDS.value: {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
    },
    "Killstreaks": {
        "BOMB DRONE": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "CARE PACKAGE": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "CLUSTER MINE": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "MORTAR STRIKE": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "WHEELSON": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "EMERGENCY AIRDROP": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "VTOL JET": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "ADVANCED UAV": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "GUNSHIP": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "EMP": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "JUGGERNAUT": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
        "SWARM": {season_str: Seasons.SEASON_ONE.value, battlepass_only_str: False},
    },
}
