# coding: utf-8
__author__ = 'Insality'

import entity
from src.constants import *

class Creature(entity.Entity):
    def __init__(self, img):
        super(Creature, self).__init__(img)