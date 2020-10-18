import pygame
import pygame_gui
import os
import json
from scenes.Scene import * 



class GameScene(Scene):
    def __init__(self, level):
        super(GameScene, self).__init__()
        self.level = level
        level_file = self.load_level()
        print(level_file)
        level_data = {}
        with open(level_file, "r") as f:
            level_data = json.load(f)
        print(level_data)





    def load_level(self):
        name = "level_" + str(self.level) + ".json"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            if name in files:
                return os.path.join(root, name)
        return "No dir found"
