# coding: utf-8
__author__ = 'Insality'

from src.constants import *
from src.resource import *
from cocos.director import director
from cocos import scene
import cocos
from pyglet.gl import *

from src.generator.dungeon_gen import generate

def init_gl():
    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

def main():
    print("Hello, Pyrox!")

    init_gl()

    director.init(resizable=True, caption=GAME_NAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    director.window.set_icon(window_icon)

    game = scene.Scene()
    tiles = generate(3, 2, 10)

    for y in reversed(range(5, 20)):
        for x in reversed(range(30)):
            if tiles[(x, y)] == '#':
                tile = cocos.sprite.Sprite(wall_dungeon, anchor = TILE_ANCHOR)
            elif tiles[(x, y)] == '.':
                tile = cocos.sprite.Sprite(floor_dungeon, anchor = TILE_ANCHOR)
            else:
                tile = cocos.sprite.Sprite(world_stone, anchor = TILE_ANCHOR)
            tile.position=(x*TILE_SIZE, y*TILE_SIZE)
            game.add(tile)



    director.run (game)

if __name__ == '__main__':
    main()