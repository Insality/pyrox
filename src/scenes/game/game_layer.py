# coding: utf-8

import cocos
import cocos.collision_model as cm
from src.constants import *
from pyglet.window import key
import src.level_manager as level_manager
from src.entities.player import Player

class GameLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()
        # self.player = entities.player.Player()
        # self.add(self.player)
        self.collman = cm.CollisionManagerGrid(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, TILE_SIZE, TILE_SIZE)
        self.schedule(self.update)
        self.schedule_interval(self.update_second, 1)
        self.scale = 1
        self.camera_x = 0
        self.camera_y = 300

        self.level = level_manager.generate_level(15)
        self.add(self.level)

        self.player = Player(212, 409)
        self.level.add(self.player, z=self.player.y-180)

    def on_key_press(self, k, modifiers):
        move = TILE_SIZE
        if (k==key.UP):
            self.camera_y += move
        if (k==key.RIGHT):
            self.camera_x += move
        if (k==key.DOWN):
            self.camera_y -= move
        if (k==key.LEFT):
            self.camera_x -= move

        self.x = -self.camera_x
        self.y = -self.camera_y

        self.player.pressed(k)

    def update(self, dt):
        self.collman.clear()

        # TODO: Вынести в level.update
        for ch in self.level.get_children():
            ch.visible = False
            if ch.x >= self.camera_x-+TILE_SIZE and ch.x <= self.camera_x+WINDOW_WIDTH+TILE_SIZE and ch.y >= self.camera_y-TILE_SIZE and ch.y<= self.camera_y+WINDOW_HEIGHT+TILE_SIZE:
                ch.visible = True
        # for actor in self.get_children():
        #     self.collman.add(actor)
        #
        # for first, other in self.collman.iter_all_collisions():
        #     first.collide(other)
        #     other.collide(first)

    def update_second(self, dt):
        pass