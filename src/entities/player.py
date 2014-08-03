# coding: utf-8
__author__ = 'Insality'

import creature
from src.resource import *
from src.constants import *
from pyglet.window import key

class Player(creature.Creature):
    is_event_handler = True

    def __init__(self, x, y):
        super(Player, self).__init__(player_stay)
        self.position = x, y

    def pressed(self, k):
        if (k==key.UP):
            self.y += TILE_SIZE
        if (k==key.DOWN):
            self.y -= TILE_SIZE
        if (k==key.RIGHT):
            self.x += TILE_SIZE
        if (k==key.LEFT):
            self.x -= TILE_SIZE