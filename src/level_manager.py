__author__ = 'Insality'

import generator.dungeon_gen

class LevelManager:
    def __init__(self):
        pass

    def get_level(self):
        return generator.dungeon_gen.generate(3, 2, 10)