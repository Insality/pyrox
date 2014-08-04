__author__ = 'Insality'

import generator.dungeon_gen
import level
from entities.map.tiles import *


class LevelManager:
    def __init__(self):
        pass

    def generate_level(self, room_count):
        ascii_lvl = generator.dungeon_gen.generate(room_count)
        lvl = self.ascii_to_level(ascii_lvl)
        return lvl

    def load_level(self):
        pass

    def save_level(self):
        pass

    def get_level(self, level):
        pass

    def ascii_to_level(self, ascii_lvl):

        width = len(ascii_lvl[0])
        height = len(ascii_lvl)
        print ("Translate ascii to obj. %i:%i" % (width, height))
        dungeon = [[None for col in range(width)] for row in range(height)]

        # reverse by y to new coord. system:
        ascii_lvl.reverse()

        start_tile = (0, 0)
        for y in range(height):
            for x in range(width):
                position = (x * TILE_SIZE, TILE_ANCHOR[1] + y * TILE_SIZE)

                if ascii_lvl[y][x] == TILE_SOLID or ascii_lvl[y][x] == TILE_EMPTY:
                    tile = TileWorldWall(position, world_stone)
                elif ascii_lvl[y][x] == TILE_FLOOR or ascii_lvl[y][x] == TILE_DOOR:
                    tile = TileFloor(position, floor_dungeon)
                elif ascii_lvl[y][x] == TILE_WALL:
                    tile = TileWall(position, wall_dungeon)
                elif ascii_lvl[y][x] == TILE_EXIT:
                    tile = TileFloor(position, map_exit)
                elif ascii_lvl[y][x] == TILE_ENTER:
                    tile = TileFloor(position, floor_dungeon_crack)
                    start_tile = (x, y)
                else:
                    tile = None

                if tile:
                    dungeon[y][x] = tile

        return level.Level(dungeon, start_tile)


_inst = LevelManager()
generate_level = _inst.generate_level
load_level = _inst.load_level
save_level = _inst.save_level
get_level = _inst.get_level