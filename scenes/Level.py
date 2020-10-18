import pygame
import pygame_gui
import os
import json
from scenes.Scene import * 
from components.commands.InNode import *
from components.commands.OutNode import *
from graph import * 
from data_manager import *



class GameScene(Scene):
    def __init__(self, level):
        super(GameScene, self).__init__()
        self.level = level
        level_file = self.load_level()
        print(level_file)
        level_data = {}


        with open(level_file, "r") as f:
            level_data = json.load(f)
        
        num_input = level_data["input"]["ports"]
        num_output = level_data["output"]["ports"]
        tests = level_data["tests"]

        self.in_node = InNode(None, (GAME_FIELD_POS_X + 50, GAME_FIELD_POS_Y + (GAME_FIELD_HEIGHT//2) - 100))
        self.out_node = OutNode(
            (GAME_FIELD_POS_X + 4*GAME_FIELD_WIDTH//5, GAME_FIELD_POS_Y +  (GAME_FIELD_HEIGHT//2) - 100))
        in_tup = self.in_node.draw()
        out_tup = self.out_node.draw()
        add_shape(in_tup[0], in_tup[1], self.in_node)
        add_shape(out_tup[0], pygame.transform.rotate(out_tup[1], 180), self.in_node)


    def render(self, screen, event):
        graph_draw(event)  




    def load_level(self):
        name = "level_" + str(self.level) + ".json"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            if name in files:
                return os.path.join(root, name)
        return "No dir found"
