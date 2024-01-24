"""
This file includes the classes for the primary and secondary weapons.
Author: Doug Griep
"""

from typing import List
from .WeaponEnums import PrimaryWeapon, SecondaryWeapon
from .AttachmentEnums import Attachments

class Create_MW3_Class():

    MAX_ATTACHMENTS = 5

    def _make_primary_weapon():
        pass

    def _make_secondary_weapon():
        pass

    def _choose_vest():
        pass

    def _choose_lethal():
        pass

    def _choose_tactical():
        pass

    def _choose_field_upgrade():
        pass

    def _choose_gloves():
        pass

    def _choose_boots():
        pass

    def _choose_gear1():
        pass

    def _choose_gear2():
        pass

    def __init__(self):
        self.primary_weapon = self._make_primary_weapon()
        self.secondary_weapon = self._make_secondary_weapon()
        self.vest = self._choose_vest()
        self.lethal = self._choose_lethal
        self.tactical = self._choose_tactical()
        self.field_upgrade = self._choose_field_upgrade()
        self.gloves = self._choose_gloves()
        self.boots = self._choose_boots()
        self.gear1 = self._choose_gear1()
        self.gear2 = self._choose_gear2()


