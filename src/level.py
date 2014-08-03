# coding: utf-8
__author__ = 'Insality'

import cocos
from constants import *

class Level(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self, dungeon):
        super(Level, self).__init__()
        self.dungeon = dungeon
        self.width = len(dungeon[0])
        self.height = len(dungeon)

        for y in reversed(range(self.height)):
            for x in range(self.width):
                if (self.dungeon[y][x] != None):
                    self.add(self.dungeon[y][x])

        self.schedule(self.update_z)


    def get_path(self, a, b):
        path = []
        return path


    def on_mouse_press (self, x, y, buttons, modifiers):
        posx, posy = cocos.director.director.get_virtual_coordinates (x, y)
        posx -= self.parent.x
        posy -= self.parent.y
        self.get(int(posx),int(posy))

    def get(self, x, y):
        self.dungeon[y//TILE_SIZE][x//TILE_SIZE].color = (100, 100, 100)
        return self.dungeon[y//TILE_SIZE][x//TILE_SIZE]

    def update_z(self, dt):
        '''
        Sort all children objects by Y coord to correct render
        TODO: grab objects placed in camera zone only
        '''
        is_changed = False
        for i in range(len(self.children)):
            ch = self.children[i]
            # ty - pos y in render_list (from up to down)
            ty = ch[0]
            # ch[1].y - cur y in real obj (from down to up). That's why WHeight - ch[1].y
            ty_obj = WINDOW_HEIGHT - ch[1].y
            if (ty != ty_obj):
                tmp = list(ch)
                tmp[0] = ty_obj
                self.children[i] = tuple(tmp)
                is_changed = True

        if is_changed:
            self.children.sort()
