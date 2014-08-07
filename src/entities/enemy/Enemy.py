# coding: utf-8
__author__ = 'Insality'

import creature
from src.resource import *
from src.constants import *
from pyglet.window import key
from src.scenes.input_layer import Input
from src.log import log


class Enemy(creature.Creature):
    def __init__(self, position, img):
        super(Enemy, self).__init__(position, img)\
        log("Initialize Enemy object. Position: %i:%i" % position)
        self.speed = TILE_SIZE
        self.sight_radius = 6
        self.buttons = input.buttons
        self.minimap_color = (0, 250, 0)

    def init_after(self, dt=0):
        super(Enemy, self).init_after()