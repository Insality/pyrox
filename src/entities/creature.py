# coding: utf-8
__author__ = 'Insality'

import entity
from src.constants import *

class Creature(entity.Entity):
    def __init__(self, position, img):
        super(Creature, self).__init__(position, img, None)
        self.type = OBJECT_CREATURE
        self.minimap_color = (0,0,0)