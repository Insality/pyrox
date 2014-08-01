__author__ = 'Insality'

from src.constants import *
import math
from random import randint


class Dungeon:
    def __init__(self, room_count, dungeon_width, dungeon_height):
        self.room_count = room_count
        self.width = dungeon_width
        self.height = dungeon_height

        # room format: (x, y, width, height, door_x, door_y)
        self.room_list = []

        self.room_max_width = dungeon_width // math.sqrt(room_count)
        self.room_max_height = dungeon_height // math.sqrt(room_count)
        if (self.room_max_width < ROOM_MIN_WIDTH or self.room_max_height < ROOM_MIN_HEIGHT):
            raise ValueError("Room count is not valid for this dungeon dimension")

        self.dungeon = [[TILE_SOLID for col in range(dungeon_width)] for row in range(dungeon_height)]


    def make_room(self, x, y, width, height):
        # room = [ [EMPTY_TILE for col in range(width)] for row in range(height) ]
        assert width >= ROOM_MIN_WIDTH, "Incorrect room width"
        assert height >= ROOM_MIN_HEIGHT, "Incorrect room height"

        self._fill_dungeon_with(x, y, width, height, TILE_WALL)
        self._fill_dungeon_with(x + 1, y + 1, width - 2, height - 2, TILE_EMPTY)
        free_directions = []

    def _is_empty(self, x, y, width, height):
        for i in range(y, y + height):
            for j in range(x, x + width):
                if (not self.dungeon[i][j] == TILE_EMPTY):
                    return False
        return True

    def _fill_dungeon_with(self, x, y, width, height, type):
        assert x + width <= self.width
        assert y + height <= self.height

        for i in range(y, y + height):
            for j in range(x, x + width):
                self.dungeon[i][j] = type

    def draw(self):
        for row in self.dungeon:
            print(''.join(row))


def create_dungeon(room_count, dungeon_width, dungeon_height):
    assert room_count >= 3, "Room_count must be more than 3"

    dungeon = Dungeon(room_count, dungeon_width, dungeon_height)

    dungeon.make_room(1, 2, 8, 5)
    dungeon.draw()


if __name__ == "__main__":
    print(create_dungeon(4, 16, 16))