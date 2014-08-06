# coding: utf-8
__author__ = 'Insality'

import cocos

from src.constants import *
from pyglet.window import key
import src.level_manager as level_manager
from src.scenes.game.camera import Camera
from src.log import log

class GameLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()

        log("Initialize Game_Layer")

        self.level = level_manager.generate_level(35)
        self.add(self.level)

        self.cam = Camera(self.level.player.position, self.level.player)
        self.add(self.cam)

        self.schedule(self.update)
        self.schedule_interval(self.update_second, 1)

    def on_key_press(self, k, modifiers):
        move = TILE_SIZE
        if k == key.W:
            self.cam.move_by(0, move)
        if k == key.D:
            self.cam.move_by(move, 0)
        if k == key.S:
            self.cam.move_by(0, -move)
        if k == key.A:
            self.cam.move_by(-move, 0)
        if k == key.SPACE:
            self.cam.follow_to(self.player)
        if k == key.C:
            self.cam.unfollow()

    def update(self, dt):
        self.level.update()

    def update_second(self, dt):
        pass