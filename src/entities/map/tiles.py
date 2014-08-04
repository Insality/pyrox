__author__ = 'Insality'

import cocos
from src.constants import *
from src.resource import *

class Tile(cocos.sprite.Sprite):
    def __init__(self, position, img):
        super(Tile, self).__init__(img, anchor=TILE_ANCHOR)
        self.position = position
        self.visible = False

        self.center_x = self.x + TILE_SIZE//2
        # y a little higher for placing creatures and little obj (Anchor in left top corner)
        self.center_y = self.y - TILE_SIZE//4
        self.center = (self.center_x, self.center_y)

        self.passable = True

class TileWorldWall(Tile):
    def __init__(self, position, img):
        super(TileWorldWall, self).__init__(position, img)
        self.passable = False

class TileWall(Tile):
    def __init__(self, position, img):
        super(TileWall, self).__init__(position, img)
        self.passable = False

class TileFloor(Tile):
    def __init__(self, position, img):
        super(TileFloor, self).__init__(position, img)
        self.passable = True