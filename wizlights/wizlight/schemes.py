from dataclasses import dataclass
from enum import Enum


class Group(Enum):
    NA = 0
    LivingRoom = 1
    Bathroom = 2
    Bedroom = 3


class Subgroup(Enum):
    NA = 0
    Table = 1
    Sofa = 1


