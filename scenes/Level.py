import pygame
import pygame_gui
import os
import json
from scenes.Scene import * 
from components.commands.InNode import *
from components.commands.OutNode import *
from components.commands.CommandManager import *
from components.commands.CommandTester import *
from components.Operand import * 
from graph import * 
from data_manager import *

class GameScene(Scene):
    def __init__(self, level, screen):
        super(GameScene, self).__init__()
        self.level = level
        level_file = self.load_level()
        print(level_file)
        level_data = {}
        self.screen = screen


        with open(level_file, "r") as f:
            level_data = json.load(f)
        
        num_input = level_data["input"]["ports"]
        num_output = level_data["output"]["ports"]
        self.in_node = InNode(None, (GAME_FIELD_POS_X + 50, GAME_FIELD_POS_Y + (GAME_FIELD_HEIGHT//2) - 100), 2)
        self.out_node = OutNode(
            (GAME_FIELD_POS_X + 4*GAME_FIELD_WIDTH//5, GAME_FIELD_POS_Y +  (GAME_FIELD_HEIGHT//2) - 100), 1)
        in_tup = self.in_node.draw(screen)
        out_tup = self.out_node.draw(screen)
        add_shape(in_tup[0], in_tup[1], self.in_node)
        add_shape(out_tup[0], out_tup[1], self.out_node)

        self.tests = level_data["tests"]
        self.run_tests()



    def render(self, event):
        graph_draw(event, self.screen)  
    
    def get_operators(self):
        return [shapes[shape_id][2] for shape_id in shapes]

    def run_tests(self): 
        self.cmd_tester = CommandTester(self.in_node, self.out_node, self.get_operators())

        #test_dict is of the form {"test_n": [input, output]}
        test_dict = {}

        for test_n in self.tests:
            test = self.tests[test_n]
            #Parse operands:
            input = test["input"]
            output = test["output"]

            shape_list = []
            for key in input: 
                data = input[key]
                try:
                    shape = Operand(self.screen, data["filename"], data["scale"], (0,0), data["color"])
                    shape_list.append(shape)
                except:
                    print("Error in level file input: level_" + str(self.level))
                    return            
            expect = []
            for type_of in output:
                print(type_of)
                if type_of == "bool":
                    for v in output[type_of]:
                        val = output[type_of][v]
                        if val == "True":
                            expect.append(True)
                        elif val == "False":
                            expect.append(False)

                elif type_of == "Shape":
                    for s in output[type_of]:
                        data = output[type_of][s]
                        try:
                            shape = Operand(self.screen, data["filename"], data["scale"], (0,0), data["color"])
                            expect.append(shape)
                        except:
                            print("Error in level file output: level_" +str(self.level))
                            return
            test_dict[test_n] = [shape_list, expect]
           
        self.cmd_man = self.cmd_tester.test(shape_list)




    def load_level(self):
        name = "level_" + str(self.level) + ".json"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            if name in files:
                return os.path.join(root, name)
        return "No dir found"
