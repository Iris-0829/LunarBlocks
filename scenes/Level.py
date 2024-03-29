import pygame
import pygame_gui
from ast import literal_eval as make_tuple
import os
import json
from scenes.Scene import * 
from components.commands.InNode import *
from components.commands.OutNode import *
from components.commands.Node import *
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
        
        port_loc_in = get_port_loc(num_input, 1)
        port_loc_out = get_port_loc(num_output, 0)

        #could be one lined but lol 
        for loc in port_loc_in:
            self.in_node.add_input_port(loc)
        for loc in port_loc_out:
            self.out_node.add_output_port(loc)

        self.in_tup = self.in_node.draw(screen)
        self.out_tup = self.out_node.draw(screen)
        add_shape(self.in_tup[0], self.in_tup[1], self.in_node)
        add_shape(self.out_tup[0], self.out_tup[1], self.out_node)

        self.tests = self.construct_test_set(level_data["tests"])
        print(self.tests)
        #self.run_test(1)

    def render(self, event)->Tuple[int]:
        return graph_draw(event, self.screen, self)  
    
    def get_operators(self):
        s = []
        for shape_id in shapes:
            shp = shapes[shape_id][2]
            if shp != self.in_node and shp != self.out_node:
                s.append(shp)

        return s

    def construct_test_set(self, tests): 
        #test_dict is of the form {"test_n": [input, output]}
        test_dict = {}

        for test_n in tests:
            test = tests[test_n]
            #Parse operands:
            input = test["input"]
            output = test["output"]

            shape_list = []
            for key in input: 
                data = input[key]
                try:
                    shape = Operand(self.screen, data["filename"], data["scale"], (0,0), make_tuple(data["color"]))
                    shape_list.append(shape)
                except Exception as e:
                    print("Error in level file input: level_" + str(self.level))
                    print(e)
                    return   



            expect = []
            for type_of in output:
                if type_of == "bool":
                    for v in output[type_of]:
                        val = output[type_of][v]
                        if val == "True":
                            expect.append(True)
                        elif val == "False":
                            expect.append(False)

                elif type_of == "Shape":
                    data = output[type_of]
                    try:
                        shape = Operand(self.screen, data["filename"], data["scale"], (0, 0), make_tuple(data["color"]))
                        expect.append(shape)
                    except Exception as e:
                        print("Error in level file output: level_" + str(self.level))
                        print(e)
                        
            test_dict[test_n] = [shape_list, expect]
        
        return test_dict
    
    def do_test_step(self, n):
        self.cmd_tester = CommandTester(self.in_node, self.out_node, self.get_operators())
        test = []
        try:
            test = self.tests["test_" + str(n)]
        except Exception as e:
            print("Test does not exist!")
            print(e)
        
        self.cmd_man = self.cmd_tester.test(test[0])
    
    def run_full_test(self, n):
        self.cmd_tester = CommandTester(self.in_node, self.out_node, self.get_operators())
        test = []
        try:
            test = self.tests["test_" + str(n)]
        except Exception as e:
            print("Test does not exist!")
            print(e)
            return 
        print(test)
        print(self.cmd_tester.test_auto(test[0], test[1]))
        





    def load_level(self):
        name = "level_" + str(self.level) + ".json"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            if name in files:
                return os.path.join(root, name)
        return "No dir found"
