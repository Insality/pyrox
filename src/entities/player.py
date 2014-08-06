# coding: utf-8
__author__ = 'Insality'

import creature
from src.resource import *
from src.constants import *
from pyglet.window import key
from src.scenes.input_layer import Input
from src.log import log


class Player(creature.Creature):
    is_event_handler = True

    def __init__(self, position):
        super(Player, self).__init__(position, player_stay)

        log("Initialize Player object. Position: %i:%i" % position)

        self.speed = TILE_SIZE
        input = Input()
        self.add(input)
        self.sight_radius = 6
        self.buttons = input.buttons
        self.minimap_color = (255, 0, 0)

    def init_after(self, dt=0):
        super(Player, self).init_after()
        self._update_fov()

    def move_by(self, x, y):
        tile = self.parent.get(self.x + x, self.y + y)
        if tile.passable:
            self.x += x
            self.y += y

        tile.action(self)
        self._update_fov()

    def _update_fov(self):
        self.parent.get_fov((self.x // TILE_SIZE, self.y // TILE_SIZE), self.sight_radius)


    def key_press(self, k):
        speed = self.speed
        if key.LSHIFT in self.buttons:
            speed *= 2

        if k == key.UP:
            self.move_by(0, speed)
        if k == key.DOWN:
            self.move_by(0, -speed)
        if k == key.RIGHT:
            self.move_by(speed, 0)
        if k == key.LEFT:
            self.move_by(-speed, 0)

        self.parent.parent.cam.update_following()