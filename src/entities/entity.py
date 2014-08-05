# coding: utf-8
__author__ = 'Insality'

import cocos
import pyglet
from src.constants import *

class Entity(cocos.sprite.Sprite):
    def __init__(self, position, img, anchor):
        super(Entity, self).__init__(img, anchor=anchor)
        self.position = position

        # смещение координат
        if anchor:
            self.x += anchor[0]
            self.y += anchor[1]
        self.type = None

