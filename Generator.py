# -*- coding: utf-8 -*-

"""
This file includes the functions and GUI creation for MW3 classes.
"""

from random import choice
from re import findall
import tkinter
from tkinter import ttk

from Enums import Attachments
from Enums.GearEnums import (
    Vest,
    Tactical,
    Lethal,
    FieldUpgrade,
    Gloves,
    Boots,
    Gear,
    Killstreaks,
)
# could do 
# from Enums import (
#     Vest,
#     ...
# )
# because of __init__.py in Enums folder

from Enums.WeaponEnums import (
    PrimaryWeapons,
    SecondaryWeapons,
)
from WeaponInfo.WeaponAttachmentCombos import weapons_attachment_combos_dict
from WeaponInfo.Additional_Info_Dictionaries import season_info_dict, locked_items_info_dict

equippable_true_str = "Equippable"
equippable_false_str = "Not Equippable"

def _choose_vest():
    vest = choice(list(Vest))
    return vest

def _set_vest(vest: Vest):
    selected_vest.set(vest.value)

def _choose_primary_weapon(first_primary = None):

    primary_weapons = []
    for category in PrimaryWeapons:
        for weapon in category.value:
            primary_weapons.append(weapon)

    if first_primary is None:
        weapon_choice = choice(primary_weapons)
        weapon_category = weapon_choice.__class__.__name__

        # weapon_category all one word (i.e. AssaultRifles, LMGS, SMGS, BattleRifles, etc.), 
        # need to split based on capital letters
        # UNLESS all letters are capital (i.e. LMGS, SMGS)
        weapon_category_words = findall('[A-Z][^A-Z]*', weapon_category)

        # if a weapon_category value is all capital letters (i.e. LMGS), 
        # the length of findall returned list is equal to length of the original weapon_category value
        if len(weapon_category) != len(weapon_category_words):
            # if lengths not equal, need to split into multiple words
            for idx, word in enumerate(weapon_category_words):
                if idx == 0:
                    weapon_category = word
                else:
                    weapon_category += " " + word
        return weapon_category, weapon_choice
    else:
        # second primary weapon, remove first primary weapon so first primary weapon not chosen again
        primary_weapons.remove(first_primary)
        weapon_choice = choice(primary_weapons)
        weapon_category = weapon_choice.__class__.__name__
        weapon_category_words = findall('[A-Z][^A-Z]*', weapon_category)
        if len(weapon_category) != len(weapon_category_words):
            for idx, word in enumerate(weapon_category_words):
                if idx == 0:
                    weapon_category = word
                else:
                    weapon_category += " " + word
        return weapon_category, weapon_choice

def _set_primary_weapon(weapon_category: PrimaryWeapons, weapon_enum):
    selected_primary_weapon.set(f"{weapon_category} {weapon_enum.value}")

def _choose_secondary_weapon():
    secondary_weapons = []
    for category in SecondaryWeapons:
        for weapon in category.value:
            secondary_weapons.append(weapon)      

    weapon_choice = choice(secondary_weapons)
    weapon_category = weapon_choice.__class__.__name__
    weapon_category_words = findall('[A-Z][^A-Z]*', weapon_category)
    if len(weapon_category) != len(weapon_category_words):
        for idx, word in enumerate(weapon_category_words):
            if idx == 0:
                weapon_category = word
            else:
                weapon_category += " " + word
    return weapon_category, weapon_choice

def _set_secondary_weapon(weapon_category: SecondaryWeapons, weapon_enum):
    selected_secondary_weapon.set(f"{weapon_category} {weapon_enum.value}")

def _choose_lethal():
    lethal = choice(list(Lethal))
    return lethal

def _set_lethal(lethal_enum: Lethal):
    selected_lethal.set(lethal_enum.value)

def _choose_tactical():
    tactical = choice(list(Tactical))
    return tactical

def _set_tactical(tactical_enum: Tactical):
    selected_tactical.set(tactical_enum.value)

def _choose_field_upgrade():
    field_upgrade = choice(list(FieldUpgrade))
    return field_upgrade

def _set_field_upgrade(field_upgrade_enum: FieldUpgrade):
    selected_field_upgrade.set(field_upgrade_enum.value)

def _choose_gloves():
    gloves = choice(list(Gloves))
    return gloves

def _set_gloves(gloves_enum: Gloves):
    selected_gloves.set(gloves_enum.value)

def _choose_boots():
    boots = choice(list(Boots))
    return boots

def _set_boots(boots_enum: Boots):
    selected_boots.set(boots_enum.value)

def _choose_gear(first_gear = None):
    if first_gear is None:
        gear = choice(list(Gear))
        return gear
    else:
        gear_list = list(Gear)
        gear_list.remove(first_gear)
        gear = choice(gear_list)
        return gear

def _set_gear1(gear1_enum: Gear):
    selected_gear1.set(gear1_enum.value)

def _set_gear2(gear2_enum: Gear):
    selected_gear2.set(gear2_enum.value)

def _choose_attachments(weapon_enum, number_of_attachments: int = 5):
    assert type(number_of_attachments) == int, "Number of attachments must be an integer 0-5"
    assert 0 <= number_of_attachments <= 5, "Number of attachments must be between (inclusive) 0-5"

    weapon_attachment_categories = weapons_attachment_combos_dict[weapon_enum]

    # get available attachments categories (muzzles, barrels, etc.) for selected weapon
    available_attachment_categories = []
    for category in weapon_attachment_categories:
        if weapon_attachment_categories[category] != []:
            available_attachment_categories.append(category)
        else:
            pass

    # choose {number_of_attachments} random attachment categories and one attachment from that category
    chosen_attachment_categories = []
    chosen_attachments = []
    try:
        for i in range(number_of_attachments):
            category_choice = _choose_attachment_category(available_attachment_categories=available_attachment_categories)

            attachment_category_disabled = _check_attachment_category_disabled(
                weapon_enum=weapon_enum,
                weapon_attachment_category_enum=category_choice,
                chosen_attachment_categories=chosen_attachment_categories,
                chosen_attachments=chosen_attachments,
            )

            if attachment_category_disabled is True:
                # remove category from available attachments and chose new attachment category again
                available_attachment_categories.remove(category_choice)
                i -= 1
                continue
            else:
                chosen_attachment_categories.append(category_choice)
                available_attachment_categories.remove(category_choice) # remove so category is not chosen again

            # choose one attachment from category
            attachments_in_category = weapons_attachment_combos_dict[weapon_enum][category_choice]
            chosen_attachment = _choose_attachment(available_attachments=attachments_in_category)

            attachment_disabled = _check_attachment_disabled(
                weapon_enum=weapon_enum,
                weapon_attachment_enum=chosen_attachment,
                chosen_attachment_categories=chosen_attachment_categories,
                chosen_attachments=chosen_attachments,
            )
            while attachment_disabled is True:
                # remove attachment and try picking new attachment
                attachments_in_category.remove(chosen_attachment)
                chosen_attachment = _choose_attachment(available_attachments=attachments_in_category)
            
            chosen_attachments.append(chosen_attachment)

    except IndexError: # some weapons maximum attachments are below 5
        pass

    return chosen_attachments

def _set_attachments(attachments_list: list, primary: bool = True):
    if primary is True:
        try:
            for attachment in attachments_list:
                if attachment.__class__.__name__ == "Muzzles":
                    primary_muzzle_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Barrels":
                    primary_barrel_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Arms":
                    primary_arms_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Lasers":
                    primary_laser_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Optics":
                    primary_optic_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Stocks":
                    primary_stock_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Combs":
                    primary_comb_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Guards":
                    primary_guard_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Bolts":
                    primary_bolt_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Levers":
                    primary_lever_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "RearGrips":
                    primary_reargrip_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "TriggerActions":
                    primary_triggeraction_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Magazines":
                    primary_mag_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Loaders":
                    primary_loader_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Wires":
                    primary_wire_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Rails":
                    primary_rail_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "AmmoTypes":
                    primary_ammo_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Underbarrels":
                    primary_underbarrel_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "CarryHandles":
                    primary_carryhandle_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "ConversionKits":
                    primary_kit_attachment.set(attachment.value)
                else:
                    print(f"Attachment not within {list(Attachments)}")
        except IndexError:
            pass

    else:
        try:
            for attachment in attachments_list:
                if attachment.__class__.__name__ == "Muzzles":
                    secondary_muzzle_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Barrels":
                    secondary_barrel_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Arms":
                    secondary_arms_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Lasers":
                    secondary_laser_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Optics":
                    secondary_optic_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Stocks":
                    secondary_stock_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Combs":
                    secondary_comb_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Guards":
                    secondary_guard_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Bolts":
                    secondary_bolt_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Levers":
                    secondary_lever_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "RearGrips":
                    secondary_reargrip_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "TriggerActions":
                    secondary_triggeraction_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Magazines":
                    secondary_mag_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Loaders":
                    secondary_loader_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Wires":
                    secondary_wire_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Rails":
                    secondary_rail_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "AmmoTypes":
                    secondary_ammo_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "Underbarrels":
                    secondary_underbarrel_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "CarryHandles":
                    secondary_carryhandle_attachment.set(attachment.value)
                elif attachment.__class__.__name__ == "ConversionKits":
                    secondary_kit_attachment.set(attachment.value)
                else:
                    print(f"Attachment not within {list(Attachments)}")
        except IndexError:
            pass

def _choose_attachment_category(available_attachment_categories: list):
    category_choice = choice(available_attachment_categories)
    return category_choice

def _choose_attachment(available_attachments: list):
    attachment_choice = choice(available_attachments)
    return attachment_choice

def equippable_status(
        weapon_enum,
        attachment_category_enum: Attachments,
        chosen_attachment_categories: list,
        attachment_enum,
        chosen_attachments: list,
    ):

    # CHIMERA Assault Rifle - muzzle disabled by default unless a barrel equipped
    if (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.CHIMERA 
        and 
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str

    # so 14 battle rifle - rear grip disabled by default unless FTAC stock or SOR55 stock equipped
    elif (
        weapon_enum == PrimaryWeapons.BATTLE_RIFLES.value.SO_14
        and
        attachment_category_enum == Attachments.REAR_GRIPS
    ):
        if Attachments.STOCKS not in chosen_attachment_categories:
            return equippable_false_str
        else:
            if (
                Attachments.STOCKS.value.FTAC_RTP_40_STOCK in chosen_attachments 
                or 
                Attachments.STOCKS.value.SO_R55_ADAPTOR in chosen_attachments
            ):
                return equippable_true_str
            else:
                return equippable_false_str

    # pdsw smg - muzzle disabled when cloak90 barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.PDSW_528
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.CLOAK_90_16 in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # pdsw smg - cloak90 barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.PDSW_528
        and
        attachment_enum == Attachments.BARRELS.value.CLOAK_90_16
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # pdsw smg - underbarrel disabled by default, when duke30 barrel or ftacSeriesIX barrel equipped
    # pdsw smg - underbarrel enabled when any other barrels equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.PDSW_528
        and
        attachment_category_enum == Attachments.UNDERBARRELS
    ):
        # by default underbarrel disabled if barrel not equipped
        if Attachments.BARRELS not in chosen_attachment_categories:
            return equippable_false_str
        
        # underbarrel disabled if 1 of 2 specific barrels equipped
        elif (
            Attachments.BARRELS.value.DUKE_30_9p5 in chosen_attachments 
            or 
            Attachments.BARRELS.value.FTAC_SERIES_IX_14p5 in chosen_attachments
        ):
            return equippable_false_str
        
        # underbarrel enabled if barrel in chosen attachment categories and not 1 of 2 barrels
        else:
            return equippable_true_str
        
    # lockwood 680 shotgun - rear grip disabled when no stock or sawed off stock equipped
    elif (
        weapon_enum == PrimaryWeapons.SHOTGUNS.value.LOCKWOOD_680
        and
        attachment_category_enum == Attachments.REAR_GRIPS
    ):
        if (
            Attachments.STOCKS.value.NO_STOCK in chosen_attachments
            or 
            Attachments.STOCKS.value.SAWED_OFF_MOD in chosen_attachments
        ):
            return equippable_false_str
        else:
            return equippable_true_str
        
    # lockwood 680 shotgun - no stock and sawed off stock disabled when rear grip equipped
    elif (
        weapon_enum == PrimaryWeapons.SHOTGUNS.value.LOCKWOOD_680
        and
        (
            attachment_enum == Attachments.STOCKS.value.NO_STOCK
            or
            attachment_enum == Attachments.STOCKS.value.SAWED_OFF_MOD
        )
    ):
        if Attachments.REAR_GRIPS in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # ebr marksman rifle - comb disabled by default unless so-90 factory stock equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.EBR_14
        and
        attachment_category_enum == Attachments.COMBS
    ):
        if Attachments.STOCKS.value.SO_90_FACTORY_STOCK not in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # lockwood mk2 marksman rifle - comb disabled when cut off stock equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.LOCKWOOD_MK2
        and
        attachment_category_enum == Attachments.COMBS
    ):
        if Attachments.STOCKS.value.CUT_OFF_STOCK_MOD in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # lockwood mk2 marksman rifle - cut off stock disabled when comb equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.LOCKWOOD_MK2
        and
        attachment_enum == Attachments.STOCKS.value.CUT_OFF_STOCK_MOD
    ):
        if Attachments.COMBS in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # COR45 handgun - trigger action disabled when conversion kit equipped
    elif (
        weapon_enum == SecondaryWeapons.HANDGUNS.value.COR_45
        and
        attachment_category_enum == Attachments.TRIGGER_ACTIONS
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # COR45 handgun - conversion kit disabled when trigger action equipped
    elif (
        weapon_enum == SecondaryWeapons.HANDGUNS.value.COR_45
        and
        attachment_category_enum == Attachments.CONVERSION_KITS
    ):
        if Attachments.TRIGGER_ACTIONS in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # COR45 handgun - underbarrel disabled unless conversion kit equipped
    elif (
        weapon_enum == SecondaryWeapons.HANDGUNS.value.COR_45
        and
        attachment_category_enum == Attachments.UNDERBARRELS
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    # RENETTI handgun - underbarrel disabled unless conversion kit equipped
    elif (
        weapon_enum == SecondaryWeapons.HANDGUNS.value.RENETTI
        and
        attachment_category_enum == Attachments.UNDERBARRELS
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
    
    # x13 handgun - stock and underbarrel disabled unless impact_point barrel equipped
    elif (
        weapon_enum == SecondaryWeapons.HANDGUNS.value.X13_AUTO
        and
        (
            attachment_category_enum == Attachments.STOCKS
            or
            attachment_category_enum == Attachments.UNDERBARRELS
        )
    ):
        if Attachments.BARRELS.value.IMPACT_POINT in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str

    # fjx imperium sniper rifle - rear grip disabled when fjx kilo tac stock equipped 
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.FJX_IMPERIUM
        and
        attachment_category_enum == Attachments.REAR_GRIPS
    ):
        if Attachments.STOCKS.value.FJX_KILO_TAC in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # fjx imperium sniper rifle - fjx kilo tac stock disabled when rear grip equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.FJX_IMPERIUM
        and
        attachment_enum == Attachments.STOCKS.value.FJX_KILO_TAC
    ):
        if Attachments.REAR_GRIPS in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # x12 akimbo disabled when stock equipped
    elif (
        weapon_enum == SecondaryWeapons.HANDGUNS.value.X12
        and
        attachment_enum == Attachments.REAR_GRIPS.value.AKIMBO_X12
    ):
        if Attachments.STOCKS in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # stock disabled when x12 akimbo equipped
    elif (
        weapon_enum == SecondaryWeapons.HANDGUNS.value.X12
        and
        attachment_category_enum == Attachments.STOCKS
    ):
        if Attachments.REAR_GRIPS.value.AKIMBO_X12 in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # MCW 6.8 Marksman Rifle - HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.MCW_68
        and
        attachment_enum == Attachments.BARRELS.value.HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # MCW 6.8 Marksman Rifle - muzzle disabled when HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.MCW_68
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str 

    # MCW Assault Rifle - KIMURA_SILENTSHOT_INTEGRAL_SUPPRESSOR barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW 
        and 
        attachment_enum == Attachments.BARRELS.value.KIMURA_SILENTSHOT_INTEGRAL_SUPPRESSOR
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # MCW Assault Rifle -  muzzle disabled when KIMURA_SILENTSHOT_INTEGRAL_SUPPRESSOR barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW 
        and 
        attachment_category_enum == Attachments.MUZZLES 
    ):
        if Attachments.BARRELS.value.KIMURA_SILENTSHOT_INTEGRAL_SUPPRESSOR in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # SIDEWINDER Battle Rifle - HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.BATTLE_RIFLES.value.SIDEWINDER 
        and 
        attachment_enum == Attachments.BARRELS.value.HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # SIDEWINDER Battle Rifle -  muzzle disabled when HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL equipped
    elif (
        weapon_enum == PrimaryWeapons.BATTLE_RIFLES.value.SIDEWINDER 
        and 
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # MCW 6.8 Marksman Rifle - HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.MCW_68 
        and 
        attachment_enum == Attachments.BARRELS.value.HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # MCW 6.8 Marksman Rifle - muzzle disabled when HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.MCW_68 
        and 
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.HUNTSMAN_SERIES_R_INTEGRATED_SUPPRESSOR_BARREL in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # WSP SWARM SMG - WSP_INFILTRATOR_INTREGRATED_SUPPRESSOR barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.WSP_SWARM
        and 
        attachment_enum == Attachments.BARRELS.value.WSP_INFILTRATOR_INTEGRATED_SUPPRESSOR
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # WSP SWARM SMG - muzzle barrel disabled when WSP_INFILTRATOR_INTREGRATED_SUPPRESSOR equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.WSP_SWARM
        and 
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.WSP_INFILTRATOR_INTEGRATED_SUPPRESSOR in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # AMR9 SMG - TECTONIC_MICRO_INTEGRAL_SUPPRESSOR barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.AMR9
        and
        attachment_enum == Attachments.BARRELS.value.TECTONIC_MICRO_INTEGRAL_SUPPRESSOR
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # AMR9 SMG - muzzle disabled when TECTONIC_MICRO_INTEGRAL_SUPPRESSOR barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.AMR9
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.TECTONIC_MICRO_INTEGRAL_SUPPRESSOR in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # AMR9 SMG - NIMBUS_6_INTEGRATED_SUPPRESSOR barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.AMR9
        and
        attachment_enum == Attachments.BARRELS.value.NIMBUS_6_INTEGRATED_SUPPRESSOR
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # AMR9 SMG - muzzle barrel disabled when NIMBUS_6_INTEGRATED_SUPPRESSOR equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.AMR9
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.NIMBUS_6_INTEGRATED_SUPPRESSOR in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # WSP-9 SMG - WSP_INFILTRATOR_INTREGRATED_SUPPRESSOR barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.WSP_9
        and
        attachment_enum == Attachments.BARRELS.value.WSP_INFILTRATOR_INTEGRATED_SUPPRESSOR
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # WSP-9 SMG - muzzle disabled when WSP_INFILTRATOR_INTREGRATED_SUPPRESSOR barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.WSP_9
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.WSP_INFILTRATOR_INTEGRATED_SUPPRESSOR in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # BRYSON 800 shotgun - XRK_CQB_8_BARREL barrel disabled when underbarrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SHOTGUNS.value.BRYSON_800
        and
        attachment_enum == Attachments.BARRELS.value.XRK_CQB_8_BARREL
    ):
        if Attachments.UNDERBARRELS in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # BRYSON 800 shotgun - underbarrel disabled when XRK_CQB_8_BARREL barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SHOTGUNS.value.BRYSON_800
        and
        attachment_category_enum == Attachments.UNDERBARRELS
    ):
        if Attachments.BARRELS.value.XRK_CQB_8_BARREL in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # KVD ENFORCER marksman rifle - KAS_7_INTEGRATED_SUPPRESSOR barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.KVD_ENFORCER
        and
        attachment_enum == Attachments.BARRELS.value.KAS_7_INTEGRATED_SUPPRESSOR
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # KVD ENFORCER marksman rifle - muzzle disabled when KAS_7_INTEGRATED_SUPPRESSOR barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.MARKSMAN_RIFLES.value.KVD_ENFORCER
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.KAS_7_INTEGRATED_SUPPRESSOR in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # KV INHIBITOR sniper rifle - KAS_7_INTEGRATED_SUPPRESSOR barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.KV_INHIBITOR
        and
        attachment_enum == Attachments.BARRELS.value.KAS_7_INTEGRATED_SUPPRESSOR
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # KV INHIBITOR sniper rifle - muzzle disabled when KAS_7_INTEGRATED_SUPPRESSOR barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.KV_INHIBITOR
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.KAS_7_INTEGRATED_SUPPRESSOR in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # XRK STALKER sniper rifle - XRK_STOIC_4_SUPPRESSED_BARREL barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.XRK_STALKER
        and
        attachment_enum == Attachments.BARRELS.value.XRK_STOIC_4_SUPPRESSED_BARREL
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str
        
    # XRK STALKER sniper rifle - muzzle disabled when XRK_STOIC_4_SUPPRESSED_BARREL barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.XRK_STALKER
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.XRK_STOIC_4_SUPPRESSED_BARREL in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # LONGBOW sniper rifle - TAC_BRUTE_SUPPRESSED_BARREL barrel disabled muzzle when equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.LONGBOW
        and
        attachment_enum == Attachments.BARRELS.value.TAC_BRUTE_SUPPRESSED_BARREL
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # LONGBOW sniper rifle - muzzle disabled TAC_BRUTE_SUPPRESSED_BARREL barrel when equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.LONGBOW
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.TAC_BRUTE_SUPPRESSED_BARREL in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # MCPR sniper rifle - SILENTFIRE_19_BARREL barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.MCPR_300
        and
        attachment_enum == Attachments.BARRELS.value.SILENTFIRE_19_BARREL
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # MCPR sniper rifle - muzzle disabled when SILENTFIRE_19_BARREL barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SNIPER_RIFLES.value.MCPR_300
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.SILENTFIRE_19_BARREL in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # ISO 9MM SMG - AXEBLADE barrel disabled when muzzle equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.ISO_9MM
        and
        attachment_enum == Attachments.BARRELS.value.AXEBLADE_6
    ):
        if Attachments.MUZZLES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # ISO 9MM SMG - muzzle disabled when AXEBLADE barrel equipped
    elif (
        weapon_enum == PrimaryWeapons.SUB_MACHINE_GUN.value.ISO_9MM
        and
        attachment_category_enum == Attachments.MUZZLES
    ):
        if Attachments.BARRELS.value.AXEBLADE_6 in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # SIDEWINDER Battle Rifle - jak thunder conversion kit disabled when magazine equipped
    elif (
        weapon_enum == PrimaryWeapons.BATTLE_RIFLES.value.SIDEWINDER
        and
        attachment_enum == Attachments.CONVERSION_KITS.value.JAK_THUNDER_LMG_KIT
    ):
        if Attachments.MAGAZINES in chosen_attachment_categories:
            return equippable_false_str
        else:
            return equippable_true_str

    # SIDEWINDER Battle Rifle - magazine disabled when jak thunder conversion kit equipped
    elif (
        weapon_enum == PrimaryWeapons.BATTLE_RIFLES.value.SIDEWINDER
        and
        attachment_category_enum == Attachments.MAGAZINES
    ):
        if Attachments.CONVERSION_KITS.value.JAK_THUNDER_LMG_KIT in chosen_attachments:
            return equippable_false_str
        else:
            return equippable_true_str

    # taq evolvere lmg - 5.56 and nato rounds enabled when 100/200 round 556 belt magazine equipped
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.NATO_LOW_GRAIN_ROUNDS_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str

    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.NATO_HIGH_GRAIN_ROUNDS_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str
    
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.INCENDIARY_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str

    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.HIGH_VELOCITY_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str

    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.OVERPRESSURED_P_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str

    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.ARMOR_PIERCING_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str

    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.HOLLOWPOINT_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str

    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.FRANGIBLE_5_56
    ):
        if (
            Attachments.MAGAZINES.value.ROUND_100_556_BELT in chosen_attachments 
            or 
            Attachments.MAGAZINES.value.ROUND_200_556_BELT in chosen_attachments
        ):
            return equippable_true_str
        else:
            return equippable_false_str

    # taq evolvere lmg - 7.62x51mm enabled when default or 50 round magazine equipped
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.FRANGIBLE_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str

    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.HOLLOWPOINT_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.ARMOR_PIERCING_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.OVERPRESSURED_P_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.HIGH_VELOCITY_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.INCENDIARY_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.HIGH_GRAIN_ROUNDS_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.LIGHT_MACHINE_GUNS.value.TAQ_EVOLVERE
        and
        attachment_enum == Attachments.AMMO_TYPES.value.LOW_GRAIN_ROUNDS_7_62X51MM
    ):
        if Attachments.MAGAZINES not in chosen_attachment_categories:
            return equippable_true_str
        elif Attachments.MAGAZINES.value.ROUND_50 in chosen_attachments:
            return equippable_true_str
        else:
            return equippable_false_str

    # mcw assault rifle - jak raven kit allows new ammo and disables other ammo 
    # enables blackout low and high grain, round nose, mono, .300 blk frangible, hollowpoint, armor pierce, overpressured +P 
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLACKOUT_HIGH_GRAIN_ROUNDS
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLACKOUT_LOW_GRAIN_ROUNDS
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLACKOUT_ROUND_NOSE
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLACKOUT_MONO
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLK_FRANGIBLE_300
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLK_HOLLOWPOINT_300
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLK_ARMOR_PIERCING_300
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
        
    elif (
        weapon_enum == PrimaryWeapons.ASSAULT_RIFLES.value.MCW
        and
        attachment_enum == Attachments.AMMO_TYPES.value.BLK_OVERPRESSURED_P_300
    ):
        if Attachments.CONVERSION_KITS in chosen_attachment_categories:
            return equippable_true_str
        else:
            return equippable_false_str
    

    # jak signal burst on holger AR disables laser
    # underbarrel locked but available with certain attachments
    #  lockwood mk2 marksman rifle
    #  cor 45 handgun
    #  X13 auto handgun


def _choose_killstreaks():
    killstreak_cost_categories = list(Killstreaks)

    # choose 3 killstreak cost categories
    killstreaks_dict = {}
    for i in range(3):
        killstreak_cost_choice = choice(killstreak_cost_categories)
        chosen_killstreak = choice(list(killstreak_cost_choice.value))
        killstreak_cost_str = chosen_killstreak.__class__.__name__
        killstreaks_dict[int(killstreak_cost_str[11:])] = chosen_killstreak
        killstreak_cost_categories.remove(killstreak_cost_choice)  # make sure killstreak from same cost not chosen again

    # sort killstreaks by cost - ascending
    sorted_killstreaks_dict = dict(sorted(killstreaks_dict.items()))
    return sorted_killstreaks_dict

def _set_killstreaks(killstreaks_dict: dict):
    for killstreak_cost in killstreaks_dict:
        killstreak_name = killstreaks_dict[killstreak_cost].value

        if killstreak_cost == 4:
            killstreak4_name.set(killstreak_name)
        elif killstreak_cost == 5:
            killstreak5_name.set(killstreak_name)
        elif killstreak_cost == 6:
            killstreak6_name.set(killstreak_name)
        elif killstreak_cost == 7:
            killstreak7_name.set(killstreak_name)
        elif killstreak_cost == 8:
            killstreak8_name.set(killstreak_name)
        elif killstreak_cost == 10:
            killstreak10_name.set(killstreak_name)
        elif killstreak_cost == 12:
            killstreak12_name.set(killstreak_name)
        elif killstreak_cost == 13:
            killstreak13_name.set(killstreak_name)
        elif killstreak_cost == 15:
            killstreak15_name.set(killstreak_name)
        else:
            # TODO - list(killstreaks) only list killstreak categories - should it list all killstreaks?
            print(f"Killstreak not in {list(Killstreaks)}")

def clear_label_values():
   """When _reroll_all called, clear previous values"""
   # killstreak values
   killstreak4_name.set("")
   killstreak5_name.set("")
   killstreak6_name.set("")
   killstreak7_name.set("")
   killstreak8_name.set("")
   killstreak10_name.set("")
   killstreak12_name.set("")
   killstreak13_name.set("")
   killstreak15_name.set("")

   # gear values
   selected_vest.set("")
   selected_tactical.set("")
   selected_lethal.set("")
   selected_field_upgrade.set("")
   selected_gloves.set("")
   selected_boots.set("")
   selected_gear1.set("")
   selected_gear2.set("")

   # primary weapon values
   selected_primary_weapon.set("")
   primary_muzzle_attachment.set("")
   primary_barrel_attachment.set("")
   primary_arms_attachment.set("")
   primary_laser_attachment.set("")
   primary_optic_attachment.set("")
   primary_stock_attachment.set("")
   primary_comb_attachment.set("")
   primary_guard_attachment.set("")
   primary_bolt_attachment.set("")
   primary_lever_attachment.set("")
   primary_reargrip_attachment.set("")
   primary_triggeraction_attachment.set("")
   primary_mag_attachment.set("")
   primary_loader_attachment.set("")
   primary_wire_attachment.set("")
   primary_rail_attachment.set("")
   primary_ammo_attachment.set("")
   primary_underbarrel_attachment.set("")
   primary_carryhandle_attachment.set("")
   primary_kit_attachment.set("")

   # secondary weapon values
   selected_secondary_weapon.set("")
   secondary_muzzle_attachment.set("")
   secondary_barrel_attachment.set("")
   secondary_arms_attachment.set("")
   secondary_laser_attachment.set("")
   secondary_optic_attachment.set("")
   secondary_stock_attachment.set("")
   secondary_comb_attachment.set("")
   secondary_guard_attachment.set("")
   secondary_bolt_attachment.set("")
   secondary_lever_attachment.set("")
   secondary_reargrip_attachment.set("")
   secondary_triggeraction_attachment.set("")
   secondary_mag_attachment.set("")
   secondary_loader_attachment.set("")
   secondary_wire_attachment.set("")
   secondary_rail_attachment.set("")
   secondary_ammo_attachment.set("")
   secondary_underbarrel_attachment.set("")
   secondary_carryhandle_attachment.set("")
   secondary_kit_attachment.set("")

def _reroll_all(first_roll:bool = False):
    if first_roll is False:
        clear_label_values()
    else:
        pass

    # choose killstreaks
    killstreaks_dict = _choose_killstreaks()
    _set_killstreaks(killstreaks_dict=killstreaks_dict)

    # vest dictates if there are 2 primary weapons, or if there is a lethal, tactical, etc.
    vest = _choose_vest()
    _set_vest(vest=vest)

    if vest == Vest.INFANTRY_VEST:
        # primary weapon
        primary_category, primary_weapon_enum = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category, weapon_enum=primary_weapon_enum)
        primary_attachments_list = _choose_attachments(weapon_enum=primary_weapon_enum)
        _set_attachments(attachments_list=primary_attachments_list)

        # secondary weapon
        secondary_category, secondary_weapon_enum = _choose_secondary_weapon()
        _set_secondary_weapon(weapon_category=secondary_category, weapon_enum=secondary_weapon_enum)
        secondary_attachments_list = _choose_attachments(weapon_enum=secondary_weapon_enum)
        _set_attachments(attachments_list=secondary_attachments_list, primary=False)

        # gear
        tactical_enum = _choose_tactical()
        _set_tactical(tactical_enum=tactical_enum)
        lethal_enum = _choose_lethal()
        _set_lethal(lethal_enum=lethal_enum)
        field_upgrade_enum = _choose_field_upgrade()
        _set_field_upgrade(field_upgrade_enum=field_upgrade_enum)
        gloves_enum = _choose_gloves()
        _set_gloves(gloves_enum=gloves_enum)
        boots_enum = _choose_boots()
        _set_boots(boots_enum=boots_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)
    
    elif vest == Vest.ASSASSIN_VEST:
        # primary
        primary_category, primary_weapon_enum = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category, weapon_enum=primary_weapon_enum)
        primary_attachments_list = _choose_attachments(weapon_enum=primary_weapon_enum)
        _set_attachments(attachments_list=primary_attachments_list)

        # secondary weapon
        secondary_category, secondary_weapon_enum = _choose_secondary_weapon()
        _set_secondary_weapon(weapon_category=secondary_category, weapon_enum=secondary_weapon_enum)
        secondary_attachments_list = _choose_attachments(weapon_enum=secondary_weapon_enum)
        _set_attachments(attachments_list=secondary_attachments_list, primary=False)

        # gear
        tactical_enum = _choose_tactical()
        _set_tactical(tactical_enum=tactical_enum)
        lethal_enum = _choose_lethal()
        _set_lethal(lethal_enum=lethal_enum)
        gloves_enum = _choose_gloves()
        _set_gloves(gloves_enum=gloves_enum)
        boots_enum = _choose_boots()
        _set_boots(boots_enum=boots_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)

    elif vest == Vest.CCT_COMMS_VEST:
        # primary
        primary_category, primary_weapon_enum = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category, weapon_enum=primary_weapon_enum)
        primary_attachments_list = _choose_attachments(weapon_enum=primary_weapon_enum)
        _set_attachments(attachments_list=primary_attachments_list)

        # secondary weapon
        secondary_category, secondary_weapon_enum = _choose_secondary_weapon()
        _set_secondary_weapon(weapon_category=secondary_category, weapon_enum=secondary_weapon_enum)
        secondary_attachments_list = _choose_attachments(weapon_enum=secondary_weapon_enum)
        _set_attachments(attachments_list=secondary_attachments_list, primary=False)

        # gear
        lethal_enum = _choose_lethal()
        _set_lethal(lethal_enum=lethal_enum)
        field_upgrade_enum = _choose_field_upgrade()
        _set_field_upgrade(field_upgrade_enum=field_upgrade_enum)
        gloves_enum = _choose_gloves()
        _set_gloves(gloves_enum=gloves_enum)
        boots_enum = _choose_boots()
        _set_boots(boots_enum=boots_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)
        gear2_enum = _choose_gear(first_gear=gear1_enum)
        _set_gear2(gear2_enum=gear2_enum)

    elif vest == Vest.DEMOLITION_VEST:
        # primary
        primary_category, primary_weapon_enum = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category, weapon_enum=primary_weapon_enum)
        primary_attachments_list = _choose_attachments(weapon_enum=primary_weapon_enum)
        _set_attachments(attachments_list=primary_attachments_list)

        # secondary weapon
        secondary_category, secondary_weapon_enum = _choose_secondary_weapon()
        _set_secondary_weapon(weapon_category=secondary_category, weapon_enum=secondary_weapon_enum)
        secondary_attachments_list = _choose_attachments(weapon_enum=secondary_weapon_enum)
        _set_attachments(attachments_list=secondary_attachments_list, primary=False)

        # gear
        tactical_enum = _choose_tactical()
        _set_tactical(tactical_enum=tactical_enum)
        lethal_enum = _choose_lethal()
        _set_lethal(lethal_enum=lethal_enum)
        field_upgrade_enum = _choose_field_upgrade()
        _set_field_upgrade(field_upgrade_enum=field_upgrade_enum)
        gloves_enum = _choose_gloves()
        _set_gloves(gloves_enum=gloves_enum)
        boots_enum = _choose_boots()
        _set_boots(boots_enum=boots_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)

    elif vest == Vest.ENGINEER_VEST:
        # primary
        primary_category, primary_weapon_enum = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category, weapon_enum=primary_weapon_enum)
        primary_attachments_list = _choose_attachments(weapon_enum=primary_weapon_enum)
        _set_attachments(attachments_list=primary_attachments_list)

        # secondary weapon
        secondary_category, secondary_weapon_enum = _choose_secondary_weapon()
        _set_secondary_weapon(weapon_category=secondary_category, weapon_enum=secondary_weapon_enum)
        secondary_attachments_list = _choose_attachments(weapon_enum=secondary_weapon_enum)
        _set_attachments(attachments_list=secondary_attachments_list, primary=False)

        # gear
        tactical_enum = _choose_tactical()
        _set_tactical(tactical_enum=tactical_enum)
        field_upgrade_enum = _choose_field_upgrade()
        _set_field_upgrade(field_upgrade_enum=field_upgrade_enum)
        gloves_enum = _choose_gloves()
        _set_gloves(gloves_enum=gloves_enum)
        boots_enum = _choose_boots()
        _set_boots(boots_enum=boots_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)
        gear2_enum = _choose_gear(first_gear=gear1_enum)
        _set_gear2(gear2_enum=gear2_enum)

    elif vest == Vest.GUNNER_VEST:
        # primary
        primary_category_1, primary_weapon_enum_1 = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category_1, weapon_enum=primary_weapon_enum_1)
        primary_attachments_list_1 = _choose_attachments(weapon_enum=primary_weapon_enum_1)
        _set_attachments(attachments_list=primary_attachments_list_1)

        # secondary
        primary_category_2, primary_weapon_enum_2 = _choose_primary_weapon(first_primary=primary_weapon_enum_1)
        _set_secondary_weapon(weapon_category=primary_category_2, weapon_enum=primary_weapon_enum_2)
        primary_attachments_list_2 = _choose_attachments(weapon_enum=primary_weapon_enum_2)
        _set_attachments(attachments_list=primary_attachments_list_2, primary=False)

        # gear
        tactical_enum = _choose_tactical()
        _set_tactical(tactical_enum=tactical_enum)
        lethal_enum = _choose_lethal()
        _set_lethal(lethal_enum=lethal_enum)
        field_upgrade_enum = _choose_field_upgrade()
        _set_field_upgrade(field_upgrade_enum=field_upgrade_enum)
        gloves_enum = _choose_gloves()
        _set_gloves(gloves_enum=gloves_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)

    elif vest == Vest.NINJA_VEST:
        # primary
        primary_category, primary_weapon_enum = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category, weapon_enum=primary_weapon_enum)
        primary_attachments_list = _choose_attachments(weapon_enum=primary_weapon_enum)
        _set_attachments(attachments_list=primary_attachments_list)

        # secondary weapon
        secondary_category, secondary_weapon_enum = _choose_secondary_weapon()
        _set_secondary_weapon(weapon_category=secondary_category, weapon_enum=secondary_weapon_enum)
        secondary_attachments_list = _choose_attachments(weapon_enum=secondary_weapon_enum)
        _set_attachments(attachments_list=secondary_attachments_list, primary=False)

        # gear
        tactical_enum = _choose_tactical()
        _set_tactical(tactical_enum=tactical_enum)
        lethal_enum = _choose_lethal()
        _set_lethal(lethal_enum=lethal_enum)
        field_upgrade_enum = _choose_field_upgrade()
        _set_field_upgrade(field_upgrade_enum=field_upgrade_enum)
        boots_enum = _choose_boots()
        _set_boots(boots_enum=boots_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)

    elif vest == Vest.OVERKILL_VEST:
        # primary
        primary_category_1, primary_weapon_enum_1 = _choose_primary_weapon()
        _set_primary_weapon(weapon_category=primary_category_1, weapon_enum=primary_weapon_enum_1)
        primary_attachments_list_1 = _choose_attachments(weapon_enum=primary_weapon_enum_1)
        _set_attachments(attachments_list=primary_attachments_list_1)

        # secondary
        primary_category_2, primary_weapon_enum_2 = _choose_primary_weapon(first_primary=primary_weapon_enum_1)
        _set_secondary_weapon(weapon_category=primary_category_2, weapon_enum=primary_weapon_enum_2)
        primary_attachments_list_2 = _choose_attachments(weapon_enum=primary_weapon_enum_2)
        _set_attachments(attachments_list=primary_attachments_list_2, primary=False)

        # gear
        tactical_enum = _choose_tactical()
        _set_tactical(tactical_enum=tactical_enum)
        lethal_enum = _choose_lethal()
        _set_lethal(lethal_enum=lethal_enum)
        gloves_enum = _choose_gloves()
        _set_gloves(gloves_enum=gloves_enum)
        boots_enum = _choose_boots()
        _set_boots(boots_enum=boots_enum)
        gear1_enum = _choose_gear()
        _set_gear1(gear1_enum=gear1_enum)

    else:
        print(f"Vest selected not within {list(Vest)}")

if __name__ == "__main__":
    root_window = tkinter.Tk()
    root_window.title("MW3 Random Class Generator")
    root_window.geometry("800x750")

    # reroll button at top of root window
    reroll_btn = ttk.Button(master=root_window, text="Reroll", command=_reroll_all)
    reroll_btn.pack(side=tkinter.TOP)

    # top frame
    tab1_top_frame = tkinter.Frame(master=root_window)
    tab1_top_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)

    # 2 frames (left and right) - each in top frame
    tab1_top_left_frame = tkinter.Frame(master=tab1_top_frame)
    tab1_top_left_frame.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1, anchor=tkinter.W)
    tab1_top_right_frame = tkinter.Frame(master=tab1_top_frame)
    tab1_top_right_frame.pack(side=tkinter.RIGHT, fill=tkinter.X, expand=1, anchor=tkinter.E)

    # 8 frames in top left frame - 1 frame (row) for each gear
    tab1_top_left_row1_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row1_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_left_row2_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row2_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_left_row3_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row3_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_left_row4_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row4_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_left_row5_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row5_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_left_row6_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row6_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_left_row7_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row7_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_left_row8_frame = tkinter.Frame(master=tab1_top_left_frame)
    tab1_top_left_row8_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)

    # 9 frames in top right frame - 1 frame (row) for each killstreak level
    tab1_top_right_row1_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row1_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row2_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row2_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row3_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row3_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row4_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row4_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row5_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row5_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row6_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row6_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row7_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row7_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row8_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row8_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_top_right_row9_frame = tkinter.Frame(master=tab1_top_right_frame)
    tab1_top_right_row9_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)

    # add gear to to left frames
    selected_vest = tkinter.StringVar() # for dynamically populating text
    selected_tactical = tkinter.StringVar()
    selected_lethal = tkinter.StringVar()
    selected_field_upgrade = tkinter.StringVar()
    selected_gloves = tkinter.StringVar()
    selected_boots = tkinter.StringVar()
    selected_gear1 = tkinter.StringVar()
    selected_gear2 = tkinter.StringVar()

    ttk.Label(master=tab1_top_left_row1_frame, font=("Times New Roman", 12), text="Vest - ").pack(side=tkinter.LEFT)
    vest_label = ttk.Label(master=tab1_top_left_row1_frame, font=("Times New Roman", 12), textvariable=selected_vest)
    vest_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_left_row2_frame, font=("Times New Roman", 12), text="Tactical - ").pack(side=tkinter.LEFT)
    tactical_label = ttk.Label(master=tab1_top_left_row2_frame, font=("Times New Roman", 12), textvariable=selected_tactical)
    tactical_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_left_row3_frame, font=("Times New Roman", 12), text="Lethal - ").pack(side=tkinter.LEFT)
    lethal_label = ttk.Label(master=tab1_top_left_row3_frame, font=("Times New Roman", 12), textvariable=selected_lethal)
    lethal_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_left_row4_frame, font=("Times New Roman", 12), text="Field Upgrade - ").pack(side=tkinter.LEFT)
    field_upgrade_label = ttk.Label(master=tab1_top_left_row4_frame, font=("Times New Roman", 12), textvariable=selected_field_upgrade)
    field_upgrade_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_left_row5_frame, font=("Times New Roman", 12), text="Gloves - ").pack(side=tkinter.LEFT)
    gloves_label = ttk.Label(master=tab1_top_left_row5_frame, font=("Times New Roman", 12), textvariable=selected_gloves)
    gloves_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_left_row6_frame, font=("Times New Roman", 12), text="Boots - ").pack(side=tkinter.LEFT)
    boots_label = ttk.Label(master=tab1_top_left_row6_frame, font=("Times New Roman", 12), textvariable=selected_boots)
    boots_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_left_row7_frame, font=("Times New Roman", 12), text="Gear 1 - ").pack(side=tkinter.LEFT)
    gear1_label = ttk.Label(master=tab1_top_left_row7_frame, font=("Times New Roman", 12), textvariable=selected_gear1)
    gear1_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_left_row8_frame, font=("Times New Roman", 12), text="Gear 2 - ").pack(side=tkinter.LEFT)
    gear2_label = ttk.Label(master=tab1_top_left_row8_frame, font=("Times New Roman", 12), textvariable=selected_gear2)
    gear2_label.pack(side=tkinter.LEFT)

    # add killstreaks to top right frames
    killstreak4_name = tkinter.StringVar()
    killstreak5_name = tkinter.StringVar()
    killstreak6_name = tkinter.StringVar()
    killstreak7_name = tkinter.StringVar()
    killstreak8_name = tkinter.StringVar()
    killstreak10_name = tkinter.StringVar()
    killstreak12_name = tkinter.StringVar()
    killstreak13_name = tkinter.StringVar()
    killstreak15_name = tkinter.StringVar()

    ttk.Label(master=tab1_top_right_row1_frame, font=("Times New Roman", 12), text="4 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak4_label = ttk.Label(master=tab1_top_right_row1_frame, font=("Times New Roman", 12), textvariable=killstreak4_name)
    killstreak4_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row2_frame, font=("Times New Roman", 12), text="5 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak5_label = ttk.Label(master=tab1_top_right_row2_frame, font=("Times New Roman", 12), textvariable=killstreak5_name)
    killstreak5_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row3_frame, font=("Times New Roman", 12), text="6 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak6_label = ttk.Label(master=tab1_top_right_row3_frame, font=("Times New Roman", 12), textvariable=killstreak6_name)
    killstreak6_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row4_frame, font=("Times New Roman", 12), text="7 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak7_label = ttk.Label(master=tab1_top_right_row4_frame, font=("Times New Roman", 12), textvariable=killstreak7_name)
    killstreak7_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row5_frame, font=("Times New Roman", 12), text="8 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak8_label = ttk.Label(master=tab1_top_right_row5_frame, font=("Times New Roman", 12), textvariable=killstreak8_name)
    killstreak8_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row6_frame, font=("Times New Roman", 12), text="10 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak10_label = ttk.Label(master=tab1_top_right_row6_frame, font=("Times New Roman", 12), textvariable=killstreak10_name)
    killstreak10_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row7_frame, font=("Times New Roman", 12), text="12 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak12_label = ttk.Label(master=tab1_top_right_row7_frame, font=("Times New Roman", 12), textvariable=killstreak12_name)
    killstreak12_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row8_frame, font=("Times New Roman", 12), text="13 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak13_label = ttk.Label(master=tab1_top_right_row8_frame, font=("Times New Roman", 12), textvariable=killstreak13_name)
    killstreak13_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_top_right_row9_frame, font=("Times New Roman", 12), text="15 Killstreak - ").pack(side=tkinter.LEFT)
    killstreak15_label = ttk.Label(master=tab1_top_right_row9_frame, font=("Times New Roman", 12), textvariable=killstreak15_name)
    killstreak15_label.pack(side=tkinter.LEFT)

    # bottom frame
    tab1_bot_frame = tkinter.Frame(master=root_window)
    tab1_bot_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=1, anchor=tkinter.S)

    # 2 frames (left and right) - each in bottom frame
    tab1_bot_left_frame = tkinter.Frame(master=tab1_bot_frame)
    tab1_bot_left_frame.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1, anchor=tkinter.W)
    tab1_bot_right_frame = tkinter.Frame(master=tab1_bot_frame)
    tab1_bot_right_frame.pack(side=tkinter.RIGHT, fill=tkinter.X, expand=1, anchor=tkinter.E)

    # 21 frames in bottom left and bottom right for weapon label and 20 attachment labels
    # bottom left
    tab1_bot_left_row1_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row1_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row2_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row2_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row3_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row3_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row4_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row4_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row5_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row5_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row6_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row6_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row7_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row7_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row8_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row8_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row9_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row9_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row10_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row10_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row11_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row11_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row12_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row12_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row13_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row13_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row14_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row14_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row15_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row15_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row16_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row16_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row17_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row17_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row18_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row18_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row19_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row19_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row20_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row20_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_left_row21_frame = tkinter.Frame(master=tab1_bot_left_frame)
    tab1_bot_left_row21_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)

    # bottom right
    tab1_bot_right_row1_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row1_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row2_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row2_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row3_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row3_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row4_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row4_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row5_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row5_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row6_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row6_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row7_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row7_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row8_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row8_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row9_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row9_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row10_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row10_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row11_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row11_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row12_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row12_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row13_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row13_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row14_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row14_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row15_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row15_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row16_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row16_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row17_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row17_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row18_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row18_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row19_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row19_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row20_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row20_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)
    tab1_bot_right_row21_frame = tkinter.Frame(master=tab1_bot_right_frame)
    tab1_bot_right_row21_frame.pack(side=tkinter.TOP, fill=tkinter.X, expand=1, anchor=tkinter.N)

    # bottom left frames for primary weapon and its attachments
    selected_primary_weapon = tkinter.StringVar()
    primary_muzzle_attachment = tkinter.StringVar()
    primary_barrel_attachment = tkinter.StringVar()
    primary_arms_attachment = tkinter.StringVar()
    primary_laser_attachment = tkinter.StringVar()
    primary_optic_attachment = tkinter.StringVar()
    primary_stock_attachment = tkinter.StringVar()
    primary_comb_attachment = tkinter.StringVar()
    primary_guard_attachment = tkinter.StringVar()
    primary_bolt_attachment = tkinter.StringVar()
    primary_lever_attachment = tkinter.StringVar()
    primary_reargrip_attachment = tkinter.StringVar()
    primary_triggeraction_attachment = tkinter.StringVar()
    primary_mag_attachment = tkinter.StringVar()
    primary_loader_attachment = tkinter.StringVar()
    primary_wire_attachment = tkinter.StringVar()
    primary_rail_attachment = tkinter.StringVar()
    primary_ammo_attachment = tkinter.StringVar()
    primary_underbarrel_attachment = tkinter.StringVar()
    primary_carryhandle_attachment = tkinter.StringVar()
    primary_kit_attachment = tkinter.StringVar()

    ttk.Label(master=tab1_bot_left_row1_frame, font=("Times New Roman", 12), text="Primary Weapon - ").pack(side=tkinter.LEFT)
    primary_weapon_label = ttk.Label(master=tab1_bot_left_row1_frame, font=("Times New Roman", 12), textvariable=selected_primary_weapon)
    primary_weapon_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row2_frame, font=("Times New Roman", 12), text="Muzzle - ").pack(side=tkinter.LEFT)
    primary_muzzle_label = ttk.Label(master=tab1_bot_left_row2_frame, font=("Times New Roman", 12), textvariable=primary_muzzle_attachment)
    primary_muzzle_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row3_frame, font=("Times New Roman", 12), text="Barrel - ").pack(side=tkinter.LEFT)
    primary_barrel_label = ttk.Label(master=tab1_bot_left_row3_frame, font=("Times New Roman", 12), textvariable=primary_barrel_attachment)
    primary_barrel_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row4_frame, font=("Times New Roman", 12), text="Arms - ").pack(side=tkinter.LEFT)
    primary_arms_label = ttk.Label(master=tab1_bot_left_row4_frame, font=("Times New Roman", 12), textvariable=primary_arms_attachment)
    primary_arms_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row5_frame, font=("Times New Roman", 12), text="Laser - ").pack(side=tkinter.LEFT)
    primary_laser_label = ttk.Label(master=tab1_bot_left_row5_frame, font=("Times New Roman", 12), textvariable=primary_laser_attachment)
    primary_laser_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row6_frame, font=("Times New Roman", 12), text="Optic - ").pack(side=tkinter.LEFT)
    primary_optic_label = ttk.Label(master=tab1_bot_left_row6_frame, font=("Times New Roman", 12), textvariable=primary_optic_attachment)
    primary_optic_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row7_frame, font=("Times New Roman", 12), text="Stock - ").pack(side=tkinter.LEFT)
    primary_stock_label = ttk.Label(master=tab1_bot_left_row7_frame, font=("Times New Roman", 12), textvariable=primary_stock_attachment)
    primary_stock_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row8_frame, font=("Times New Roman", 12), text="Comb - ").pack(side=tkinter.LEFT)
    primary_comb_label = ttk.Label(master=tab1_bot_left_row8_frame, font=("Times New Roman", 12), textvariable=primary_comb_attachment)
    primary_comb_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row9_frame, font=("Times New Roman", 12), text="Guard - ").pack(side=tkinter.LEFT)
    primary_guard_label = ttk.Label(master=tab1_bot_left_row9_frame, font=("Times New Roman", 12), textvariable=primary_guard_attachment)
    primary_guard_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row10_frame, font=("Times New Roman", 12), text="Bolt - ").pack(side=tkinter.LEFT)
    primary_bolt_label = ttk.Label(master=tab1_bot_left_row10_frame, font=("Times New Roman", 12), textvariable=primary_bolt_attachment)
    primary_bolt_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row11_frame, font=("Times New Roman", 12), text="Lever - ").pack(side=tkinter.LEFT)
    primary_lever_label = ttk.Label(master=tab1_bot_left_row11_frame, font=("Times New Roman", 12), textvariable=primary_lever_attachment)
    primary_lever_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row12_frame, font=("Times New Roman", 12), text="Rear Grip - ").pack(side=tkinter.LEFT)
    primary_reargrip_label = ttk.Label(master=tab1_bot_left_row12_frame, font=("Times New Roman", 12), textvariable=primary_reargrip_attachment)
    primary_reargrip_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row13_frame, font=("Times New Roman", 12), text="Trigger Action - ").pack(side=tkinter.LEFT)
    primary_triggeraction_label = ttk.Label(master=tab1_bot_left_row13_frame, font=("Times New Roman", 12), textvariable=primary_triggeraction_attachment)
    primary_triggeraction_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row14_frame, font=("Times New Roman", 12), text="Magazine - ").pack(side=tkinter.LEFT)
    primary_mag_label = ttk.Label(master=tab1_bot_left_row14_frame, font=("Times New Roman", 12), textvariable=primary_mag_attachment)
    primary_mag_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row15_frame, font=("Times New Roman", 12), text="Loader - ").pack(side=tkinter.LEFT)
    primary_loader_label = ttk.Label(master=tab1_bot_left_row15_frame, font=("Times New Roman", 12), textvariable=primary_loader_attachment)
    primary_loader_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row16_frame, font=("Times New Roman", 12), text="Wire - ").pack(side=tkinter.LEFT)
    primary_wire_label = ttk.Label(master=tab1_bot_left_row16_frame, font=("Times New Roman", 12), textvariable=primary_wire_attachment)
    primary_wire_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row17_frame, font=("Times New Roman", 12), text="Rail - ").pack(side=tkinter.LEFT)
    primary_rail_label = ttk.Label(master=tab1_bot_left_row17_frame, font=("Times New Roman", 12), textvariable=primary_rail_attachment)
    primary_rail_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row18_frame, font=("Times New Roman", 12), text="Ammo Type - ").pack(side=tkinter.LEFT)
    primary_ammo_label = ttk.Label(master=tab1_bot_left_row18_frame, font=("Times New Roman", 12), textvariable=primary_ammo_attachment)
    primary_ammo_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row19_frame, font=("Times New Roman", 12), text="Underbarrel - ").pack(side=tkinter.LEFT)
    primary_underbarrel_label = ttk.Label(master=tab1_bot_left_row19_frame, font=("Times New Roman", 12), textvariable=primary_underbarrel_attachment)
    primary_underbarrel_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row20_frame, font=("Times New Roman", 12), text="Carry Handle - ").pack(side=tkinter.LEFT)
    primary_carryhandle_label = ttk.Label(master=tab1_bot_left_row20_frame, font=("Times New Roman", 12), textvariable=primary_carryhandle_attachment)
    primary_carryhandle_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_left_row21_frame, font=("Times New Roman", 12), text="Conversion Kit - ").pack(side=tkinter.LEFT)
    primary_kit_label = ttk.Label(master=tab1_bot_left_row21_frame, font=("Times New Roman", 12), textvariable=primary_kit_attachment)
    primary_kit_label.pack(side=tkinter.LEFT)

    # bottom right frame for secondary weapon and its attachments
    selected_secondary_weapon = tkinter.StringVar()
    secondary_muzzle_attachment = tkinter.StringVar()
    secondary_barrel_attachment = tkinter.StringVar()
    secondary_arms_attachment = tkinter.StringVar()
    secondary_laser_attachment = tkinter.StringVar()
    secondary_optic_attachment = tkinter.StringVar()
    secondary_stock_attachment = tkinter.StringVar()
    secondary_comb_attachment = tkinter.StringVar()
    secondary_guard_attachment = tkinter.StringVar()
    secondary_bolt_attachment = tkinter.StringVar()
    secondary_lever_attachment = tkinter.StringVar()
    secondary_reargrip_attachment = tkinter.StringVar()
    secondary_triggeraction_attachment = tkinter.StringVar()
    secondary_mag_attachment = tkinter.StringVar()
    secondary_loader_attachment = tkinter.StringVar()
    secondary_wire_attachment = tkinter.StringVar()
    secondary_rail_attachment = tkinter.StringVar()
    secondary_ammo_attachment = tkinter.StringVar()
    secondary_underbarrel_attachment = tkinter.StringVar()
    secondary_carryhandle_attachment = tkinter.StringVar()
    secondary_kit_attachment = tkinter.StringVar()

    ttk.Label(master=tab1_bot_right_row1_frame, font=("Times New Roman", 12), text="Secondary Weapon - ").pack(side=tkinter.LEFT)
    secondary_weapon_label = ttk.Label(master=tab1_bot_right_row1_frame, font=("Times New Roman", 12), textvariable=selected_secondary_weapon)
    secondary_weapon_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row2_frame, font=("Times New Roman", 12), text="Muzzle - ").pack(side=tkinter.LEFT)
    secondary_muzzle_label = ttk.Label(master=tab1_bot_right_row2_frame, font=("Times New Roman", 12), textvariable=secondary_muzzle_attachment)
    secondary_muzzle_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row3_frame, font=("Times New Roman", 12), text="Barrel - ").pack(side=tkinter.LEFT)
    secondary_barrel_label = ttk.Label(master=tab1_bot_right_row3_frame, font=("Times New Roman", 12), textvariable=secondary_barrel_attachment)
    secondary_barrel_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row4_frame, font=("Times New Roman", 12), text="Arms - ").pack(side=tkinter.LEFT)
    secondary_arms_label = ttk.Label(master=tab1_bot_right_row4_frame, font=("Times New Roman", 12), textvariable=secondary_arms_attachment)
    secondary_arms_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row5_frame, font=("Times New Roman", 12), text="Laser - ").pack(side=tkinter.LEFT)
    secondary_laser_label = ttk.Label(master=tab1_bot_right_row5_frame, font=("Times New Roman", 12), textvariable=secondary_laser_attachment)
    secondary_laser_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row6_frame, font=("Times New Roman", 12), text="Optic - ").pack(side=tkinter.LEFT)
    secondary_optic_label = ttk.Label(master=tab1_bot_right_row6_frame, font=("Times New Roman", 12), textvariable=secondary_optic_attachment)
    secondary_optic_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row7_frame, font=("Times New Roman", 12), text="Stock - ").pack(side=tkinter.LEFT)
    secondary_stock_label = ttk.Label(master=tab1_bot_right_row7_frame, font=("Times New Roman", 12), textvariable=secondary_stock_attachment)
    secondary_stock_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row8_frame, font=("Times New Roman", 12), text="Comb - ").pack(side=tkinter.LEFT)
    secondary_comb_label = ttk.Label(master=tab1_bot_right_row8_frame, font=("Times New Roman", 12), textvariable=secondary_comb_attachment)
    secondary_comb_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row9_frame, font=("Times New Roman", 12), text="Guard - ").pack(side=tkinter.LEFT)
    secondary_guard_label = ttk.Label(master=tab1_bot_right_row9_frame, font=("Times New Roman", 12), textvariable=secondary_guard_attachment)
    secondary_guard_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row10_frame, font=("Times New Roman", 12), text="Bolt - ").pack(side=tkinter.LEFT)
    secondary_bolt_label = ttk.Label(master=tab1_bot_right_row10_frame, font=("Times New Roman", 12), textvariable=secondary_bolt_attachment)
    secondary_bolt_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row11_frame, font=("Times New Roman", 12), text="Lever - ").pack(side=tkinter.LEFT)
    secondary_lever_label = ttk.Label(master=tab1_bot_right_row11_frame, font=("Times New Roman", 12), textvariable=secondary_lever_attachment)
    secondary_lever_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row12_frame, font=("Times New Roman", 12), text="Rear Grip - ").pack(side=tkinter.LEFT)
    secondary_reargrip_label = ttk.Label(master=tab1_bot_right_row12_frame, font=("Times New Roman", 12), textvariable=secondary_reargrip_attachment)
    secondary_reargrip_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row13_frame, font=("Times New Roman", 12), text="Trigger Action - ").pack(side=tkinter.LEFT)
    secondary_triggeraction_label = ttk.Label(master=tab1_bot_right_row13_frame, font=("Times New Roman", 12), textvariable=secondary_triggeraction_attachment)
    secondary_triggeraction_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row14_frame, font=("Times New Roman", 12), text="Magazine - ").pack(side=tkinter.LEFT)
    secondary_mag_label = ttk.Label(master=tab1_bot_right_row14_frame, font=("Times New Roman", 12), textvariable=secondary_mag_attachment)
    secondary_mag_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row15_frame, font=("Times New Roman", 12), text="Loader - ").pack(side=tkinter.LEFT)
    secondary_loader_label = ttk.Label(master=tab1_bot_right_row15_frame, font=("Times New Roman", 12), textvariable=secondary_loader_attachment)
    secondary_loader_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row16_frame, font=("Times New Roman", 12), text="Wire - ").pack(side=tkinter.LEFT)
    secondary_wire_label = ttk.Label(master=tab1_bot_right_row16_frame, font=("Times New Roman", 12), textvariable=secondary_wire_attachment)
    secondary_wire_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row17_frame, font=("Times New Roman", 12), text="Rail - ").pack(side=tkinter.LEFT)
    secondary_rail_label = ttk.Label(master=tab1_bot_right_row17_frame, font=("Times New Roman", 12), textvariable=secondary_rail_attachment)
    secondary_rail_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row18_frame, font=("Times New Roman", 12), text="Ammo Type - ").pack(side=tkinter.LEFT)
    secondary_ammo_label = ttk.Label(master=tab1_bot_right_row18_frame, font=("Times New Roman", 12), textvariable=secondary_ammo_attachment)
    secondary_ammo_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row19_frame, font=("Times New Roman", 12), text="Underbarrel - ").pack(side=tkinter.LEFT)
    secondary_underbarrel_label = ttk.Label(master=tab1_bot_right_row19_frame, font=("Times New Roman", 12), textvariable=secondary_underbarrel_attachment)
    secondary_underbarrel_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row20_frame, font=("Times New Roman", 12), text="Carry Handle - ").pack(side=tkinter.LEFT)
    secondary_carryhandle_label = ttk.Label(master=tab1_bot_right_row20_frame, font=("Times New Roman", 12), textvariable=secondary_carryhandle_attachment)
    secondary_carryhandle_label.pack(side=tkinter.LEFT)

    ttk.Label(master=tab1_bot_right_row21_frame, font=("Times New Roman", 12), text="Conversion Kit - ").pack(side=tkinter.LEFT)
    secondary_kit_label = ttk.Label(master=tab1_bot_right_row21_frame, font=("Times New Roman", 12), textvariable=secondary_kit_attachment)
    secondary_kit_label.pack(side=tkinter.LEFT)

    # first time opening, run immediately
    _reroll_all(first_roll=True)

    root_window.mainloop()