from typing import Tuple
import pygame
from components.commands.AdditionNode import AdditionNode
from graph import add_shape


class CreateOperator:
    def __init__(self, screen, filename: str, loc: Tuple[float, float], spawn_loc: Tuple[float, float]):
        self.img = pygame.image.load(filename)
        self.loc = loc
        self.spawn_loc = spawn_loc
        self.screen = screen
        self.dim = self.img.get_size()

        self.filename = filename
        self.draggable_operator = []
        self.is_on = False

        self.upper_limit = 100
        self.lower_limit = 500

    def change_loc(self, change_height):
        if self.upper_limit <= self.loc[1] <= self.lower_limit:
            self.loc = (self.loc[0], self.loc[1] - change_height)
        elif self.upper_limit >= self.loc[1]:
            self.loc = (self.loc[0], self.upper_limit)
        else:
            self.loc = (self.loc[0], self.lower_limit)


    def display(self):
        # draw img at loc
        self.screen.blit(self.img, self.loc)

    def isOn(self, mouse_loc: Tuple[float, float]):
        self.is_on = self.loc[0] <= mouse_loc[0] <= self.loc[0] + self.dim[0] and self.loc[1] <= mouse_loc[1] <= self.loc[1] + \
                self.dim[1]
        if self.is_on:
            # create a new draggable operator
            newOperator = AdditionNode(0, (500, 400))
            newOperator.add_input_port((0, 0))
            newOperator.add_input_port((0, 100))
            newOperator.add_output_port((100, 50))
            s = newOperator.draw(self.screen)
            add_shape(s[0], s[1], newOperator)


