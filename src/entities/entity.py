# coding: utf-8
__author__ = 'Insality'

import cocos
from src.constants import *

class Entity(cocos.sprite.Sprite):
    def __init__(self, img):
        super(Entity, self).__init__(img)
        self.type = None