# coding: utf-8
__author__ = 'Insality'

import entity
from src.constants import *
from src.resource import *
from cocos.director import director

class GameObject(entity.Entity):
    def __init__(self, position, img):
        super(GameObject, self).__init__(position, img, anchor=TILE_ANCHOR)

        self.type = OBJECT_GAMEOBJ
        self.minimap_color = (0,0,0)

    def action(self, other):
        pass

class LevelExit(GameObject):
    def __init__(self, position):
        super(LevelExit, self).__init__(position, map_exit)
        self.minimap_color = (225,225,100)

    def action(self, other):
        print("go_to_next_level")
        for im in other.image.frames:
            im.duration = 0.1
        # from src.scenes.game.game_scene import Game
        # game_scene = Game()
        # director.replace(game_scene)





