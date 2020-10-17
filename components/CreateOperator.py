from typing import Tuple
import pygame
from components import Draggable


class CreateOperator:
    def __init__(self, stage, filename: str, loc: Tuple[float, float]):
        self.img = pygame.image.load(filename)
        self.loc = loc
        self.stage = stage

    def display(self):
        # draw img at loc
        self.stage.blit(self.img, self.loc)

    def isHolding(self, mouse_loc: Tuple[float, float]):
        if self.loc[0] <= mouse_loc[0] <= self.loc[0] + self.dim[0] and self.loc[1] <= mouse_loc[1] <= self.loc[1] + \
                self.dim[1]:
            # mouse is in range
            return True

    def createOperator(self, mouse_loc: Tuple[float, float], mouse_button_down):
        # mouse is in range and click the mouse -> create a new draggable operator
        if self.isHolding(mouse_loc) and mouse_button_down:
            newOperator = Draggable(self.stage, self.filename, self.loc)
            newOperator.display()
