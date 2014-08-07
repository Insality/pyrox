# coding: utf-8
__author__ = 'Insality'

from src.entities.creature import Creature
from src.resource import *
from src.constants import *
from src.log import log


class Enemy(Creature):
    def __init__(self, position, img):
        super(Enemy, self).__init__(position, img)
        log("Initialize Enemy object. Position: %i:%i" % position)
        self.speed = TILE_SIZE
        self.minimap_color = (250, 0, 0)

    def init_after(self, dt=0):
        super(Enemy, self).init_after()

    def action(self, other):
        print("action enemy")

