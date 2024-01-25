"""
Enums to hold names of ammo type attachments.
"""

from enum import Enum, auto
from Weapons import *

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