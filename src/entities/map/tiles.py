__author__ = 'Insality'

import cocos
from src.constants import *

class Tile(cocos.sprite.Sprite):
    def __init__(self, position, img):
        super(Tile, self).__init__(img, anchor=TILE_ANCHOR)
        self.type = OBJECT_TILE
        self.position = position
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

    def set_brightness(self, value):
        self._brightness = value
        self.update_brightness()

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

class TileFloor(Tile):
    def __init__(self, position, img):
        super(TileFloor, self).__init__(position, img)
        self.passable = True
        self.minimap_color = (150,150,150)