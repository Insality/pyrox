# coding: utf-8
__author__ = 'Insality'

import cocos

from src.scenes.input_layer import Input
from game_layer import GameLayer
from src.resource import *
from src.constants import *
from pyglet.gl import *


class Game(cocos.scene.Scene):
    def __init__(self):
        super(Game, self).__init__()

        self.input = Input()
        self.add(self.input, z=0, name='input')

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
        self.minimap = Minimap(self.level.dungeon, self.level.creatures, self.level.objects)
        self.add(self.minimap)
        self.schedule(self.update)
        self.unschedule(self.init_after)

    def update(self, dt):
        self.draw_minimap()

    def draw_minimap(self):
        self.minimap.render()


class Minimap(cocos.sprite.Sprite):
    def __init__(self, dungeon, creatures, objects):

        self.dungeon = dungeon
        self.creatures = creatures
        self.objects = objects

        self.format = 'RGBA'
        self.map_width = len(dungeon[0])
        self.map_height = len(dungeon)

        self.minimap = pyglet.image.create(self.map_width, self.map_height)
        self.data = len(self.format) * self.map_width * self.map_height * [chr(0)]

        for y in range(self.map_height):
            for x in range(self.map_width):
                self._setPixel(x, y, (230, 130, 0), 0)

        self.minimap.format = self.format
        datas = ''.join(self.data)
        self.minimap.set_data(self.format, self.map_width * len(self.format), datas)

        super(Minimap, self).__init__(self.minimap)


        w, h = cocos.director.director.get_window_size()
        self.x = w - self.map_width
        self.y = self.map_height

    def _setPixel(self, x, y, color, alpha):
        ''' color is tuple of (R, G, B) as integers'''
        pixelIdx = x + (y * self.map_width)
        byteIdx = pixelIdx * len(self.format)
        r, g, b = color
        self.data[byteIdx] = chr(r)
        self.data[byteIdx + 1] = chr(g)
        self.data[byteIdx + 2] = chr(b)
        self.data[byteIdx + 3] = chr(alpha)

    def setPixel(self, x, y, color):
        self._setPixel(x, y, color, 255)


    def render(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                if (self.dungeon[y][x] and self.dungeon[y][x].explored):
                    self.setPixel(x, y, self.dungeon[y][x].minimap_color)

        for object in self.objects:
            self.setPixel(object.x // TILE_SIZE, (object.y) // TILE_SIZE, object.minimap_color)

        for creature in self.creatures:
            self.setPixel(creature.x // TILE_SIZE, creature.y // TILE_SIZE, creature.minimap_color)

        data = ''.join(self.data)
        self.minimap.set_data(self.format, self.map_width * len(self.format), data)
        self.image = self.minimap
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)







