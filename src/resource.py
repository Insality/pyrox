from pyglet.image import Texture

__author__ = 'Insality'

import pyglet
from pyglet.gl import *

pyglet.resource.path = ["res/"]
pyglet.resource.path += ["res/font/"]
pyglet.resource.path += ["res/icon/"]
pyglet.resource.path += ["res/image/"]
pyglet.resource.path += ["res/image/map/"]
pyglet.resource.path += ["res/music/"]
pyglet.resource.path += ["res/sound/"]
pyglet.resource.reindex()


def load_resource(string):
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    return pyglet.resource.image(string)


window_icon = pyglet.image.load('res/icon/icon.png')

# Player:
_player = pyglet.image.ImageGrid(load_resource('player.png'), 1, 2)
_player_stay_seq = _player[0:2]
player_stay = pyglet.image.Animation.from_image_sequence(_player_stay_seq, 0.3, loop=True)

# Map tiles:
_floors_dungeon = pyglet.image.ImageGrid(load_resource('floors_dungeon.png'), 2, 2)
floor_dungeon = _floors_dungeon[0]
floor_dungeon_crack = _floors_dungeon[1]

wall_dungeon = load_resource('wall_dungeon.png')
world_stone = load_resource('world_stone.png')



map_exit = load_resource('stairs.png')

_doors = pyglet.image.ImageGrid(load_resource('doors.png'), 1, 2)
map_door_front = _doors[0]
map_door_side = _doors[1]


pixel = load_resource('pixel.png')

# Fonts:
kongtext_font = pyglet.resource.add_font("kongtext.ttf")
