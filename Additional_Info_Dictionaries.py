"""File for storing information about weapons and attachments."""

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
    Optics,
    Muzzles,
    Underbarrels,
    RearGrips,
    AmmoTypes,
    Combs,
    Stocks,
    Lasers,
    Barrels,
    Magazines,
    Guards
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

aftermarket_parts = {
    "Optics": [
        Optics.KR_INTLAS_LSJ_3.value,
        Optics.CRONEN_INTLAS_MSP_12.value,
        Optics.INTLAS_CAS_14.value,
    ],
    "Muzzles": [],
    "Underbarrels": [],
    "RearGrips": [],
    "AmmoTypes": [],
    "Combs": [],
    "Stocks": [],
    "Lasers": [],
    "Barrels": [],
    "Magazines": [],
    "Guards": []
}

armory_unlocks = {
    "Weapons": {
        "AssaultRifles": [
            AssaultRifles.DG_56.value,
            AssaultRifles.FR_556.value
        ],
        "BattleRifles": [
            BattleRifles.SIDEWINDER.value,
            BattleRifles.MTZ_762.value
        ],
        "SMGS": [
            SMGS.WSP_9.value,
            SMGS.RIVAL_9,
            SMGS.STRIKER_9.value
        ],
        "Shotguns": [
            Shotguns.RIVETER.value
        ],
        "LMGS": [
            LMGS.HOLGER_26.value,
            LMGS.TAQ_ERADICATOR.value
        ],
        "MarksmanRifles": [
            MarksmanRifles.DM56.value,
            MarksmanRifles.MTZ_INTERCEPTOR.value,
            MarksmanRifles.MCW_68.value
        ],
        "SniperRifles": [
            SniperRifles.LONGBOW.value,
            SniperRifles.KV_INHIBITOR.value
        ],
        "MeleePrimary": [],
        "Handguns": [
            HandGuns.WSP_STINGER.value,
        ],
        "Launchers": [],
        "MeleeSecondary": [
            MeleeSecondary.KARAMBIT,
        ]
    },
    "AftermarketParts": {
        "Optics": [
            Optics.KR_INTLAS_LSJ_3.value,
            Optics.CRONEN_INTLAS_MSP_12.value,
            Optics.INTLAS_CAS_14.value,
        ],
        "Underbarrels": [
            Underbarrels.JAK_PURIFIER.value,
        ],
        "Stocks": [
            "MCW FULL AUTO CONVERTER",
            "WSP AKIMBO BRACE STOCK"
        ],
        "Kits": [
            "BROODMOTHER .45 KIT",
            "JAK NIGHTSHADE RIFLE KIT"
            "XRK IP-V2 CONVERSION KIT",
            "JAK RAVEN KIT"
        ],

    },
    "Perks": [
        Gear.GHOST_TV_CAMO.value,
        Gloves.ASSAULT_GLOVES.value,
        Gear.SIGNAL_JAMMER.value,
        Gear.HIJACKED_IFF_STROBE.value,
        Gear.THREAT_IDENTIFICATION_SYSTEM.value,
        Boots.COVERT_SNEAKERS.value,
        Gear.DATA_JACKER.value,
        Gloves.MARKSMAN_GLOVES.value,
        Vest.ASSASSIN_VEST.value,
    ],
    "Equipment": [
        Lethal.SEMTEX.value,
        Lethal.PROXIMITY_MINE.value,
        Lethal.C4.value,
        Lethal.BREACHER_DRONE.value,
        Lethal.DRILL_CHARGE.value,
        Lethal.MOLOTOV_COCKTAIL.value,
        Tactical.FLASH_GRENADE.value,
        Tactical.SHOCK_STICK.value,
        Tactical.STIM.value,
        Tactical.TEAR_GAS.value,
        Tactical.EMD_GRENADE.value,
        Tactical.SNAPSHOT_GRENADE.value,
    ],
    "FieldUpgrades": [
        FieldUpgrade.DDOS.value,
        FieldUpgrade.INFLATABLE_DECOY.value,
        FieldUpgrade.TROPHY_SYSTEM.value,
        FieldUpgrade.LOADOUT_DROP.value,
        FieldUpgrade.TACTICAL_CAMERA.value,
        FieldUpgrade.HEARTBEAT_SENSOR.value,
        FieldUpgrade.SUPPRESSION_MINE.value,
        FieldUpgrade.ANTI_ARMOR_ROUNDS.value,
        FieldUpgrade.SMOKE_AIRDROP.value,
        FieldUpgrade.DEAD_SILENCE.value,
    ],
    "Killstreaks": [
        "CARE PACKAGE",
        "CLUSTER MINE",
        "WHEELSON",
        "MORTAR STRIKE",
        "JUGGERNAUT",
        "ADVANCED UAV",
        "EMERGENCY AIRDROP",
        "VTOL JET",
        "GUNSHIP",
        "BOMB DRONE",
        "EMP",
        "SWARM"
    ],
}

