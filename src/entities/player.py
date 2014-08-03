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
        self.speed = TILE_SIZE

    def move_by(self, x, y):
        if (self.parent.get(self.x + x, self.y + y).passable):
            self.x += x
            self.y += y

    def pressed(self, k):
        if (k==key.UP):
            self.move_by(0, self.speed)
        if (k==key.DOWN):
            self.move_by(0, -self.speed)
        if (k==key.RIGHT):
            self.move_by(self.speed, 0)
        if (k==key.LEFT):
            self.move_by(-self.speed, 0)