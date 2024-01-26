"""
This file includes the classes for the primary and secondary weapons.
Author: Doug Griep
"""
from enum import Enum

import Muzzles 
import Barrels
import Lasers
import Optics
import Stocks
import Combs
import Bolts
import RearGrips
import TriggerActions
import Magazines
import AmmoTypes
import Underbarrels

class Attachments(Enum):
    MUZZLES = Muzzles
    BARRELS = Barrels
    LASERS = Lasers
    OPTICS = Optics
    STOCKS = Stocks
    COMBS = Combs
    BOLTS = Bolts
    REAR_GRIPS = RearGrips
    TRIGGER_ACTIONS = TriggerActions
    MAGAZINES = Magazines
    AMMO_TYPES = AmmoTypes
    UNDERBARRELS = Underbarrels


class Create_MW3_Class():

    MAX_ATTACHMENTS = 5

    def _choose_primary_weapon():
        pass

    def _choose_vest():
        pass

    def _choose_lethal(self):
        if self.vest == "Vest Name":
            self.lethal = None
        else:
            self.lethal = "Random Lethal"

    def _choose_tactical():
        pass

    def _choose_field_upgrade():
        pass

    def _choose_gloves():
        pass

    def _choose_boots():
        pass

    def _choose_gear_1():
        pass

    def _choose_gear_2():
        pass

    def _choose_secondary_weapon():
        pass

    def _choose_primary_attachments():
        pass

    def _choose_secondary_attachments():
        pass


    def __init__(self):
        self.primary_weapon = self._choose_primary_weapon()
        self.primary_weapon_attachments = self._choose_primary_attachments()
        self.secondary_weapon = self._choose_secondary_weapon()
        self.secondary_weapon_attachments = self._choose_secondary_attachments()
        self.vest = self._choose_vest()
        self.lethal = self._choose_lethal
        self.tactical = self._choose_tactical()
        self.field_upgrade = self._choose_field_upgrade()
        self.gloves = self._choose_gloves()
        self.boots = self._choose_boots()
        self.gear1 = self._choose_gear_1()
        self.gear2 = self._choose_gear_2()
