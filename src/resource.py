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


window_icon = pyglet.image.load('res/icon/icon.png')

# Player:
player = pyglet.image.ImageGrid( pyglet.resource.image('player.png'), 1, 2)
player_stay_seq = player[0:2]
player_stay = pyglet.image.Animation.from_image_sequence(player_stay_seq, 0.3, loop=True)

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

# Map tiles:
floors_dungeon =  pyglet.image.ImageGrid( pyglet.resource.image('floors_dungeon.png'), 2, 2)
floor_dungeon = floors_dungeon[0]
floor_dungeon_crack = floors_dungeon[1]
wall_dungeon = pyglet.resource.image('wall_dungeon.png')
world_stone = pyglet.resource.image('world_stone.png')


# Fonts:
kongtext_font = pyglet.resource.add_font("kongtext.ttf")


# Animations:
# dungeon = pyglet.resource.image('chess_board.png')
# dungeons = pyglet.image.ImageGrid(dungeon, 2, 2)
# floor_dungeons = dungeons[0:2]
# floor_dungeon = pyglet.image.Animation.from_image_sequence(floor_dungeons, 0.1, loop=True)

