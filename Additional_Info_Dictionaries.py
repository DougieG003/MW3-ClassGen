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
    "Muzzles": [],
    "Barrels": [],
    "Arms": [],
    "Lasers": [],
    "Optics": [
        Optics.KR_INTLAS_LSJ_3.value,
        Optics.CRONEN_INTLAS_MSP_12.value,
        Optics.INTLAS_CAS_14.value,
    ],
    "Stocks": [],
    "Combs": [],
    "Guards": [],
    "Bolts": [],
    "Levers": [],
    "RearGrips": [],
    "TriggerActions": [],
    "Magazines": [],
    "Wires": [],
    "AmmoTypes": [],
    "Underbarrels": [],
    "CarryHandles": [],
}

armory_unlocks = {
    "Weapons": {
        "AssaultRifles": [
            AssaultRifles.DG_56.value,
            AssaultRifles.FR_556.value,
        ],
        "BattleRifles": [
            BattleRifles.SIDEWINDER.value,
            BattleRifles.MTZ_762.value,
        ],
        "SMGS": [
            SMGS.WSP_9.value,
            SMGS.RIVAL_9,
            SMGS.STRIKER_9.value,
        ],
        "Shotguns": [
            Shotguns.RIVETER.value,
        ],
        "LMGS": [
            LMGS.HOLGER_26.value,
            LMGS.TAQ_ERADICATOR.value,
        ],
        "MarksmanRifles": [
            MarksmanRifles.MCW_68.value,
            MarksmanRifles.DM56.value,
            MarksmanRifles.MTZ_INTERCEPTOR.value,
        ],
        "SniperRifles": [
            SniperRifles.LONGBOW.value,
            SniperRifles.KV_INHIBITOR.value,
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
        "Stocks": [
            "MCW FULL AUTO CONVERTER",
            "WSP AKIMBO BRACE STOCK"
        ],
        "Underbarrels": [
            Underbarrels.JAK_PURIFIER.value,
        ],
        "Kits": [
            "BROODMOTHER .45 KIT",
            "JAK NIGHTSHADE RIFLE KIT"
            "XRK IP-V2 CONVERSION KIT",
            "JAK RAVEN KIT"
        ],
    },
    "Perks": [
        Vest.ASSASSIN_VEST.value,
        Gloves.MARKSMAN_GLOVES.value,
        Gloves.ASSAULT_GLOVES.value,
        Boots.COVERT_SNEAKERS.value,
        Gear.THREAT_IDENTIFICATION_SYSTEM.value,
        Gear.DATA_JACKER.value,
        Gear.SIGNAL_JAMMER.value,
        Gear.HIJACKED_IFF_STROBE.value,
        Gear.GHOST_TV_CAMO.value,
    ],
    "Equipment": [
        Lethal.PROXIMITY_MINE.value,
        Lethal.DRILL_CHARGE.value,
        Lethal.SEMTEX.value,
        Lethal.C4.value,
        Lethal.BREACHER_DRONE.value,
        Lethal.MOLOTOV_COCKTAIL.value,
        Tactical.FLASH_GRENADE.value,
        Tactical.SNAPSHOT_GRENADE.value,
        Tactical.SHOCK_STICK.value,
        Tactical.STIM.value,
        Tactical.TEAR_GAS.value,
        Tactical.EMD_GRENADE.value,
    ],
    "FieldUpgrades": [
        FieldUpgrade.HEARTBEAT_SENSOR.value,
        FieldUpgrade.TROPHY_SYSTEM.value,
        FieldUpgrade.INFLATABLE_DECOY.value,
        FieldUpgrade.TACTICAL_CAMERA.value,
        FieldUpgrade.DDOS.value,
        FieldUpgrade.DEAD_SILENCE.value,
        FieldUpgrade.LOADOUT_DROP.value,
        FieldUpgrade.SMOKE_AIRDROP.value,
        FieldUpgrade.SUPPRESSION_MINE.value,
        FieldUpgrade.ANTI_ARMOR_ROUNDS.value,
    ],
    "Killstreaks": [
        "BOMB DRONE",
        "CARE PACKAGE",
        "CLUSTER MINE",
        "MORTAR STRIKE",
        "WHEELSON", 
        "EMERGENCY AIRDROP",       
        "VTOL JET",
        "ADVANCED UAV",
        "GUNSHIP",
        "EMP",
        "JUGGERNAUT",
        "SWARM"
    ],
}

