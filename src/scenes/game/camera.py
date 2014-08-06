# coding: utf-8
__author__ = 'Insality'

from src.constants import *
import cocos
from src.log import log

class Camera(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, position, obj=None):
        super(Camera, self).__init__()
        log("Initialize Camera object")
        self.position = position
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.follow_obj = obj

        self.schedule(self.update)

    def move_by(self, x, y):
        self.x += x
        self.y += y

    def look_at(self, obj):
        self.move_to(obj.x, obj.y)

    def move_to(self, x, y):
        self.x = x - WINDOW_WIDTH//2
        self.y = y - WINDOW_HEIGHT//2

    def is_object_in(self, obj):
        if obj.x < self.x-TILE_SIZE or obj.x > self.x+WINDOW_WIDTH+TILE_SIZE \
                or obj.y < self.y-TILE_SIZE or obj.y > self.y+WINDOW_HEIGHT+TILE_SIZE:
            return False
        return True

    def follow_to(self, obj):
        self.follow_obj = obj

    def unfollow(self):
        self.follow_obj = None

    def update(self, dt):
        self.update_parent_offset()
        self.update_following()

    def on_key_press(self, k, mods):
        self.update_following()

    def update_following(self):
        if self.follow_obj != None:
            self.look_at(self.follow_obj)

    def update_parent_offset(self):
        self.parent.x = -self.x
        self.parent.y = -self.y

