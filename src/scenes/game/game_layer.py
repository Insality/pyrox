# coding: utf-8

import cocos
import cocos.collision_model as cm
from src.constants import *
from src.generator.dungeon_gen import generate
from src.resource import *
from src.entities.map.tile import Tile
from pyglet.window import key

class GameLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()

        # self.player = entities.player.Player()
        # self.add(self.player)
        self.collman = cm.CollisionManagerGrid(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, TILE_SIZE, TILE_SIZE)
        self.schedule(self.update)
        self.schedule_interval(self.update_second, 1)
        self.init_level()
        self.scale = 1
        self.camera_x = 0
        self.camera_y = 300


    def init_level(self):
        tiles, width, height = generate(15)

        print ("%i:%i" % (width, height))

        for y in reversed(range(height)):
            for x in range(width):
                if tiles[y][x] == TILE_SOLID:
                    type = wall_dungeon
                elif tiles[y][x] == TILE_FLOOR or tiles[y][x] == TILE_DOOR:
                    type = floor_dungeon
                elif tiles[y][x] == TILE_WALL:
                    type = world_stone
                else:
                    type = None

                if not type==None:
                    position=(30+x*TILE_SIZE, 30+TILE_ANCHOR[1] + y*TILE_SIZE)
                    tile = Tile(type, position[0], position[1])
                    self.add(tile)

    def on_key_press(self, k, modifiers):
        move = TILE_SIZE*2
        if (k==key.UP):
            self.camera_y += move
        if (k==key.RIGHT):
            self.camera_x += move
        if (k==key.DOWN):
            self.camera_y -= move
        if (k==key.LEFT):
            self.camera_x -= move

        self.x = -self.camera_x
        self.y = -self.camera_y

    def update(self, dt):
        self.collman.clear()


        for ch in self.get_children():
            ch.visible = False
            if ch.x >= self.camera_x-+TILE_SIZE and ch.x <= self.camera_x+WINDOW_WIDTH+TILE_SIZE and ch.y >= self.camera_y-TILE_SIZE and ch.y<= self.camera_y+WINDOW_HEIGHT+TILE_SIZE:
                ch.visible = True
        # for actor in self.get_children():
        #     self.collman.add(actor)
        #
        # for first, other in self.collman.iter_all_collisions():
        #     first.collide(other)
        #     other.collide(first)

    def update_second(self, dt):
        pass