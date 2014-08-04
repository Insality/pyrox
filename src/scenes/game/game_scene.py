# coding: utf-8
__author__ = 'Insality'

import cocos

from src.scenes.input_layer import Input
from game_layer import GameLayer
from pyglet.gl import *
from pyglet.graphics import *
from src.resource import *


class Game(cocos.scene.Scene):
    def __init__(self):
        super(Game, self).__init__()

        self.add(Input(), z=0, name='input')

        self.game_layer = self.get_game_layer()
        self.add(self.game_layer, z=1, name='game_layer')

        self.hud_layer = self.get_hud_layer()
        self.add(self.hud_layer, z=3, name='hud_layer')

    def get_game_layer(self):
        return GameLayer()

    def get_hud_layer(self):
        return HUDLayer()


class HUDLayer(cocos.layer.Layer):
    def __init__(self):
        super(HUDLayer, self).__init__()

        self.level = None
        self.schedule_interval(self.init_after, 0.2)
        self.minimap = None

    def init_after(self, dt):
        self.level = self.parent.game_layer.level
        self.minimap = Minimap(self.level.dungeon)
        self.add(self.minimap)
        self.schedule(self.update)
        self.unschedule(self.init_after)


    def update(self, dt):
        self.draw_minimap()

    def draw_minimap(self):
        self.minimap.render()


class Minimap(cocos.layer.Layer):
    def __init__(self, dungeon):
        super(Minimap, self).__init__()
        self.dungeon = dungeon

        self.map_width = len(dungeon[0])
        self.map_height = len(dungeon)
        w, h = cocos.director.director.get_window_size()
        self.pixel_size = 2
        self.x = w - self.map_width * self.pixel_size
        self.y = self.map_height * self.pixel_size
        for y in range(self.map_height):
            for x in range(self.map_width):
                if self.dungeon[y][x]:
                    sprite = cocos.sprite.Sprite(pixel)
                    sprite.scale = 1
                    sprite.position = x, y
                    sprite.visible = self.dungeon[y][x].visible
                    sprite.color = self.dungeon[y][x].minimap_color
                    self.add(sprite)

    def render(self):
        for sprite in self.get_children():
            sprite.visible = self.dungeon[sprite.y][sprite.x].explored