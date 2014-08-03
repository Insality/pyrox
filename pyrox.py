# coding: utf-8
__author__ = 'Insality'

from src.constants import *
from src.resource import *
from cocos.director import director
from src.scenes.game.game_scene import Game
from pyglet.gl import *


def init_gl():
    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

def main():
    print("Hello, Pyrox!")

    init_gl()
    director.init(resizable=True, caption=GAME_NAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    director.window.set_icon(window_icon)
    game_scene = Game()
    director.run(game_scene)

if __name__ == '__main__':
    main()