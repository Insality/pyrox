# coding: utf-8
__author__ = 'Insality'

import cocos

from src.scenes.input_layer import Input
from game_layer import GameLayer


class Game(cocos.scene.Scene):
    def __init__(self):
        super(Game, self).__init__()

        self.add( Input(), z=0, name='input')

        self.game_layer = self.get_game_layer()
        self.add( self.game_layer, z=1, name='game_layer')

        # self.enemy_manager = EnemyManager()
        # self.add( self.enemy_manager, z = 1, name='enemy_manager')

        # self.start_music()

        self.hud_layer = self.get_hud_layer()
        self.add( self.hud_layer, z=3, name='hud_layer')

    def get_game_layer(self):
        return GameLayer()

    def get_hud_layer(self):
        return HUDLayer()

class HUDLayer(cocos.layer.Layer):
    def __init__(self):
        super(HUDLayer, self).__init__()

        # self.hud_score = profile.profile['score']
        # self.score_label = cocos.text.Label('', font_size=18, x=0, y=config.GAME_HEIGHT, anchor_x='left', anchor_y='top')
        # self.add(self.score_label)

        self.schedule(self.update)

    def update(self, dt):
        pass