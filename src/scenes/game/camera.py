# coding: utf-8
__author__ = 'Insality'

from src.constants import *
import cocos


class Camera(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

    #   self.schedule(self.update)

    def update(self, dt):
        pass

