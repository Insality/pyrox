# coding: utf-8
__author__ = 'Insality'

import cocos

class Entity(cocos.sprite.Sprite):
    def __init__(self, img):
        super(Entity, self).__init__(img)