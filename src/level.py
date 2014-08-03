# coding: utf-8
__author__ = 'Insality'

import cocos

class Level(cocos.layer.Layer):
    def __init__(self, dungeon):
        super(Level, self).__init__()
        self.dungeon = dungeon
        self.width = len(dungeon[0])
        self.height = len(dungeon)

        for y in reversed(range(self.height)):
            for x in range(self.width):
                if (self.dungeon[y][x] != None):
                    self.add(self.dungeon[y][x])


    def get_path(self, a, b):
        path = []
        return path

    def get(self, x, y):
        return self.dungeon[y][x]