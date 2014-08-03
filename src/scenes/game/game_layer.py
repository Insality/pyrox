# coding: utf-8

import cocos
import cocos.collision_model as cm
from src.constants import *
from pyglet.window import key
import src.level_manager as level_manager
from src.entities.player import Player
from src.scenes.game.camera import Camera

class GameLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()
        self.collman = cm.CollisionManagerGrid(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, TILE_SIZE, TILE_SIZE)
        self.schedule(self.update)
        self.schedule_interval(self.update_second, 1)
        self.cam = Camera(100, 300)
        self.add(self.cam)

        self.level = level_manager.generate_level(15)
        self.add(self.level)

        pos = self.level.get(210, 530).center
        self.player = Player(pos[0], pos[1])
        self.level.add(self.player, z=self.player.y-180)

    def on_key_press(self, k, modifiers):
        move = TILE_SIZE
        if (k==key.W):
            self.cam.move_by(0, move)
        if (k==key.D):
            self.cam.move_by(move, 0)
        if (k==key.S):
            self.cam.move_by(0, -move)
        if (k==key.A):
            self.cam.move_by(-move, 0)
        if (k==key.SPACE):
            self.cam.follow_to(self.player)
        if (k==key.C):
            self.cam.unfollow()

        self.player.pressed(k)

    def update(self, dt):
        self.collman.clear()

        # TODO: Вынести в level.update
        for ch in self.level.get_children():
            ch.visible = False
            if self.cam.is_obj_in(ch):
                ch.visible = True
        # for actor in self.get_children():
        #     self.collman.add(actor)
        #
        # for first, other in self.collman.iter_all_collisions():
        #     first.collide(other)
        #     other.collide(first)

    def update_second(self, dt):
        pass