__author__ = 'Insality'

import cocos
from src.constants import *
from src.resource import *
from src.entities.entity import Entity


class Tile(Entity):
    def __init__(self, position, img):
        super(Tile, self).__init__(position, img, anchor=TILE_ANCHOR)
        self.type = OBJECT_TILE
        self.visible = False

        self.center_x = self.x + TILE_SIZE//2
        # y a little higher for placing creatures and little obj (Anchor in left top corner)
        self.center_y = self.y - TILE_SIZE//4
        self.center = (self.center_x, self.center_y)

        self._brightness = 100
        self.passable = True
        # Was this tile explored by Player?
        self.explored = False
        self.color = (0,0,0)
        self.minimap_color = (0,0,0)

        # Link to creature and object on this tile
        self.creature_on = None
        self.object_on = None

    def set_brightness(self, value):
        self._brightness = value
        self.update_brightness()

    def action(self, other):
        if self.creature_on:
            self.creature_on.action(other)
            return
        if self.object_on:
            self.object_on.action(other)
            return
        self._action(other)

    def _action(self, other):
        pass

    def update_brightness(self):
        bright = int(255*self._brightness/100)
        self.color = (bright, bright, bright)


class TileWorldWall(Tile):
    def __init__(self, position, img):
        super(TileWorldWall, self).__init__(position, img)
        self.passable = False
        self.minimap_color = (60, 60, 60)


class TileWall(Tile):
    def __init__(self, position, img):
        super(TileWall, self).__init__(position, img)
        self.passable = False
        self.minimap_color = (100,100,150)

    def _action(self, other):
        self.image = floor_dungeon
        self.passable = True
        self.minimap_color = (150,150,150)


class TileFloor(Tile):
    def __init__(self, position, img):
        super(TileFloor, self).__init__(position, img)
        self.passable = True
        self.minimap_color = (150,150,150)