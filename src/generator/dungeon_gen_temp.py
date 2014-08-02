__author__ = 'Insality'

from src.constants import *
import math
from random import randint, choice



class Hall:
    def __init__(self, from_point, to_point):
        self.x_from, self.y_from = from_point
        self.x_to, self.y_to = to_point

class Room:
    def __init__(self, pos_x, pos_y, width, height):
        self.x = 0
        self.y = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.center = (self.pos_x + self.width // 2, self.pos_y - self.height // 2)

        self.free_direction = DIRECTIONS[:]
        self.make_room()

    def make_room(self):
        self.room = [[TILE_SOLID for col in range(self.width)] for row in range(self.height)]
        _fill_with(self.room, self.x, self.y, self.width, self.height, TILE_WALL)
        _fill_with(self.room, self.x + 1, self.y + 1, self.width - 2, self.height - 2, TILE_EMPTY)

    def place_tile(self, x, y, tile):
        self.room[y][x] = tile

    def make_random_door(self, direction):
        dx, dy = 0, 0
        if (direction == UP or direction == DOWN):
            rnd = randint(1, self.width - 2)
        else:
            rnd = randint(1, self.height - 2)

        if direction == UP:
            dx, dy = rnd, 0
        elif direction == DOWN:
            dx, dy = rnd, self.height -1
        elif direction == RIGHT:
            dx, dy = self.width - 1, rnd
        elif direction == LEFT:
            dx, dy = 0, rnd

        print ("door", dx, dy)
        # self.room[dy][dx] = TILE_DOOR
        return dx+self.pos_x, dy+self.pos_y

    def overlaps(self, other):
        return ( abs(self.center[0] - other.center[0]) < (self.width // 2) + (other.width // 2) and
                 abs(self.center[1] - other.center[1]) < (self.width // 2) + (other.height // 2) )


class Dungeon:
    def __init__(self, room_count):
        self.room_count = room_count
        self.width = 0
        self.height = 0

        self.rooms = []
        self.halls = []
        self.dungeon = []


    def generate(self):
        if len(self.rooms) <= 0:
            self.make_room(0, 0, randint(ROOM_MIN_WIDTH, ROOM_MAX_WIDTH), randint(ROOM_MIN_HEIGHT, ROOM_MAX_HEIGHT))

        # while (len(self.rooms) <= self.room_count):
        self.make_random_room()
        self.make_random_room()
        self.make_random_room()
        self.make_random_room()
        self.make_random_room()
        self.make_random_room()


    def make_random_room(self):
        assert len(self.rooms) > 0, "A main room must me created"

        rooms = filter(lambda x: len(x.free_direction) > 0, self.rooms)
        print("Aviable rooms: %i" % len(rooms))

        # room_from = choice(rooms)
        room_from = choice(rooms)
        direction = choice(room_from.free_direction)
        door_from = room_from.make_random_door(direction)

        room_new = None
        for i in range(GEN_MAX_TRY_PLACE_ROOM):
            hall_len = randint(HALL_MIN_LENGTH, HALL_MAX_LENGTH)
            door_new = get_new_pos_by_direction(door_from[0], door_from[1], hall_len, direction)

            room_width = randint(ROOM_MIN_WIDTH, ROOM_MAX_WIDTH)
            room_height = randint(ROOM_MIN_HEIGHT, ROOM_MAX_HEIGHT)
            room_x = door_new[0]
            room_y = door_new[1]
            if (direction == UP):
                room_x -= room_width // 2
                room_y -= room_height-1
            elif (direction == RIGHT):
                room_y -= room_height // 2
            elif (direction == DOWN):
                room_x -= room_width // 2
            elif (direction == LEFT):
                room_y -= room_height // 2
                room_x -= room_width-1

            room_new = Room(room_x, room_y, room_width, room_height)
            hall_new = Hall(door_from, door_new)

            for room in self.rooms:
                if room_new.overlaps(room):
                    print("new room overlap old rooms")
                    room_new = None
                    break

        # If new room was not created
        if (room_new == None):
            print ("Cannot create new room, remove aviable direction")
            room_from.free_direction.remove(direction)
            return

        room_from.free_direction.remove(direction)
        room_new.free_direction.remove((direction+2)% 4)

        self.halls.append(hall_new)
        self.rooms.append(room_new)


    def make_dungeon(self):
        self.dungeon = [[TILE_SOLID for col in range(self.width)] for row in range(self.height)]

    def make_room(self, x, y, width, height):
        assert width >= ROOM_MIN_WIDTH, "Incorrect room width"
        assert height >= ROOM_MIN_HEIGHT, "Incorrect room height"

        self.rooms.append(Room(x, y, width, height))

    def _is_empty(self, x, y, width, height):
        for i in range(y, y + height):
            for j in range(x, x + width):
                if (not self.dungeon[i][j] == TILE_EMPTY):
                    return False
        return True

    def place_room(self, room, offset_x, offset_y):
        offset_x += room.pos_x
        offset_y += room.pos_y
        for i in range(room.height):
            for j in range(room.width):
                self.dungeon[i + offset_y][j + offset_x] = room.room[i][j]

    def compile(self):
        assert len(self.rooms) > 0

        # Calculating borders of all rooms
        min_x, max_x = self.rooms[0].pos_x, self.rooms[0].pos_x + self.rooms[0].width
        min_y, max_y = self.rooms[0].pos_y, self.rooms[0].pos_y + self.rooms[0].height

        for room in self.rooms:
            if min_x > room.pos_x:
                min_x = room.pos_x
            if min_y > room.pos_y:
                min_y = room.pos_y
            if max_x < room.pos_x + room.width:
                max_x = room.pos_x + room.width
            if max_y < room.pos_y + room.height:
                max_y = room.pos_y + room.height

        self.width = max_x - min_x
        self.height = max_y - min_y

        # offsets for start with (0,0)
        self.room_offset_x = -min_x
        self.room_offset_y = -min_y

        self.make_dungeon()

        print "offsets"
        print self.room_offset_x
        print self.room_offset_y
        for room in self.rooms:
            self.place_room(room, self.room_offset_x, self.room_offset_y)

        for hall in self.halls:
            from_x = hall.x_from+self.room_offset_x
            from_y = hall.y_from+self.room_offset_y
            to_y = hall.y_to + self.room_offset_y
            to_x = hall.x_to + self.room_offset_x

            for x in range(from_x, to_x+1):
                for y in range(from_y, to_y+1):
                    self.dungeon[y][x] = TILE_EMPTY
            for x in range(from_x, to_x-1, -1):
                for y in range(from_y, to_y-1, -1):
                    self.dungeon[y][x] = TILE_EMPTY

            self.dungeon[from_y][from_x] = TILE_DOOR
            self.dungeon[to_y][to_x] = TILE_DOOR

    def draw(self):
        for row in self.dungeon:
            print(''.join(row))


def _fill_with(source, x, y, width, height, type):
    for i in range(y, y + height):
        for j in range(x, x + width):
            source[i][j] = type


def get_new_pos_by_direction(x, y, len, direction):
    if (direction == RIGHT):
        x += len
    elif (direction == UP):
        y -= len
    elif (direction == LEFT):
        x -= len
    elif (direction == DOWN):
        y += len
    return x, y


def create_dungeon(room_count):
    assert room_count >= 3, "Room_count must be more than 3"

    dungeon = Dungeon(room_count)

    dungeon.generate()
    dungeon.compile()
    dungeon.draw()


if __name__ == "__main__":
    create_dungeon(4)