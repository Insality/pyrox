# coding: utf-8
__author__ = 'Insality'

import creature
from src.resource import *
from src.constants import *
from pyglet.window import key
from src.scenes.input_layer import Input


class Player(creature.Creature):
    is_event_handler = True

    def __init__(self, position):
        super(Player, self).__init__(player_stay)
        self.position = position
        self.speed = TILE_SIZE

        input = Input()
        self.add(input)
        self.sight_radius = 5
        self.buttons = input.buttons

    def move_by(self, x, y):
        if self.parent.get(self.x + x, self.y + y).passable:
            self.x += x
            self.y += y
            self.parent.get_fov((self.x // TILE_SIZE, self.y // TILE_SIZE), self.sight_radius)

    def key_press(self, k):
        if k == key.UP:
            self.move_by(0, self.speed)
        if k == key.DOWN:
            self.move_by(0, -self.speed)
        if k == key.RIGHT:
            self.move_by(self.speed, 0)
        if k == key.LEFT:
            self.move_by(-self.speed, 0)

        self.parent.parent.cam.update_following()