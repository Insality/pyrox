# coding: utf-8
__author__ = 'Insality'

import cocos
from constants import *
from entities.player import Player
import cocos.collision_model as cm
from src.log import log


class Level(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, dungeon, start_tile, creatures, objects):
        print creatures

        super(Level, self).__init__()
        self.objects = objects
        self.creatures = creatures
        self.dungeon = dungeon
        self.width = len(dungeon[0])
        self.height = len(dungeon)

        for y in range(self.height):
            for x in range(self.width):
                if self.dungeon[y][x]:
                    self.add(self.dungeon[y][x])

        for obj in self.objects:
            self.add(obj)
            tile = self.get(obj.x, obj.y)
            if not tile.object_on:
                tile.object_on = obj

        for creature in self.creatures:
            self.add(creature)
            tile = self.get(creature.x, creature.y)
            if not tile.creature_on:
                tile.creature_on = creature

        # Player here
        self.start_pos = dungeon[start_tile[1]][start_tile[0]].center
        self.player = Player(self.start_pos)
        self.add(self.player)
        self.creatures.append(self.player)

        self.collman = cm.CollisionManagerGrid(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, TILE_SIZE, TILE_SIZE)

        self.schedule(self.update)


        log("Loading Level object, map sise: %i:%i" % (self.width, self.height))
        log("Count of creatures: %i. Count of Objects: %i" % (len(self.creatures), len(self.objects)) )
        for x in self.get_children():
            if x.type != OBJECT_TILE:
                log(str(x))


    def get_path(self, a, b):
        '''
        return list of Tiles from a to b index. A*
        '''
        path = []
        return path

    def on_mouse_press(self, x, y, buttons, modifiers):
        x, y = cocos.director.director.get_virtual_coordinates(x, y)
        cam = self.parent.cam
        x = int(x + cam.x)
        y = int(y + cam.y)
        tile = self.get(x, y)
        tile.set_brightness(30)

    def on_key_press(self, k, mods):
        self.player.key_press(k)

    def get(self, x, y):
        ''' return Tile by screen x-y pos '''
        return self.dungeon[y // TILE_SIZE][x // TILE_SIZE]

    def get_index_from_pos(self, x, y):
        ''' return Tile index(x,y) from screen pos '''
        return x // TILE_SIZE, y // TILE_SIZE

    def get_by_index(self, x, y):
        ''' return Tile by index '''
        return self.dungeon[y][x]

    def get_object(self, x, y):
        ''' get the Object in x-y pos. If no object - return tile '''
        pass

    def get_objects_in_area(self, a, b):
        ''' return all objects in arena (exclude tiles) from a to b rect, by screen pos '''
        objects = set()
        return objects


    def _blocked(self, x, y):
        return (x < 0 or y < 0
                or x >= self.width or y >= self.height
                or not self.dungeon[y][x].passable)

    def _cast_light(self, cx, cy, row, start, end, radius, xx, xy, yx, yy, id):
        ''' Recursive lightcasting function '''
        if start < end:
            return
        radius_squared = radius * radius
        for j in range(row, radius + 1):
            dx, dy = -j - 1, -j
            blocked = False
            while dx <= 0:
                dx += 1
                # Translate the dx, dy coordinates into map coordinates:
                X, Y = cx + dx * xx + dy * xy, cy + dx * yx + dy * yy
                # l_slope and r_slope store the slopes of the left and right
                # extremities of the square we're considering:
                l_slope, r_slope = (dx - 0.5) / (dy + 0.5), (dx + 0.5) / (dy - 0.5)
                if start < r_slope:
                    continue
                elif end > l_slope:
                    break
                else:
                    # Our light beam is touching this square; light it:
                    if dx * dx + dy * dy < radius_squared and X >= 0 and Y >= 0 and X < self.width and Y < self.height:
                        # self.set_lit(X, Y)
                        self.tiles.append(self.dungeon[Y][X])
                    if blocked:
                        # we're scanning a row of blocked squares:
                        if self._blocked(X, Y):
                            new_start = r_slope
                            continue
                        else:
                            blocked = False
                            start = new_start
                    else:
                        if self._blocked(X, Y) and j < radius:
                            # This is a blocking square, start a child scan:
                            blocked = True
                            self._cast_light(cx, cy, j + 1, start, l_slope,
                                             radius, xx, xy, yx, yy, id + 1)
                            new_start = r_slope
            # Row is scanned; do next row unless last square was blocked:
            if blocked:
                break

    def get_fov(self, position, radius):
        ''' fov - field of view, get all viewed tiles from position '''
        # Multipliers for transforming coordinates to other octants:
        mult = [[1, 0, 0, -1, -1, 0, 0, 1],
                [0, 1, -1, 0, 0, -1, 1, 0],
                [0, 1, 1, 0, 0, -1, -1, 0],
                [1, 0, 0, 1, -1, 0, 0, -1]]
        self.tiles = []
        for oct in range(8):
            self._cast_light(position[0], position[1], 1, 1.0, 0.0, radius, mult[0][oct],
                             mult[1][oct], mult[2][oct], mult[3][oct], 0)

        self.tiles.append(self.dungeon[position[1]][position[0]])
        for tile in self.get_children():
            if (tile.type == OBJECT_TILE):
                tile.set_brightness(40)

        for tile in self.tiles:
            tile.set_brightness(100)
            tile.explored = True

        return self.tiles

    def update(self, dt=1):
        self._update_visible()
        self._update_z()

    # TODO: Перебирает все элементы. Можно упростить?
    def _update_visible(self):
        for ch in self.get_children():
            ch.visible = False
            if (ch.type == OBJECT_TILE and not ch.explored):
                continue
            if self.parent.cam.is_object_in(ch):
                ch.visible = True

    def _update_z(self):
        ''' Sort all children objects by Y coord to correct render
            TODO: grab objects placed in camera zone only '''
        is_changed = False
        for i in range(len(self.children)):
            ch = self.children[i]
            if ch[1].visible:
                # ty - pos y in render_list (from up to down)
                ty = ch[0]
                # ch[1].y - cur y in real obj (from down to up). That's why WHeight - ch[1].y
                ty_obj = WINDOW_HEIGHT - ch[1].y
                # if now checking tile: get -2y , for low render prioriry
                if ch[1].type == OBJECT_TILE:
                    ty_obj -= 2
                if ty != ty_obj:
                    tmp = list(ch)
                    tmp[0] = ty_obj
                    self.children[i] = tuple(tmp)
                    is_changed = True

        if is_changed:
            self.children.sort()
