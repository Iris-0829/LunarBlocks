import pygame
from typing import Tuple


class Draggable:

    def in_range(self, mouse_loc):
        """
        Checks if the mouse is currently on top of the object.
        :param mouse_loc: (x, y) coordinate of the cursor's location.
        """
        return (self.loc[0] <= mouse_loc[0] <= self.loc[0] + self.dim[0] and
                self.loc[1] <= mouse_loc[1] <= self.loc[1] + self.dim[1])

    def is_holding(self, mouse_loc: Tuple[float, float]):
        """
        Checks if the mouse is currently holding the object.
        :param mouse_loc: (x, y) coordinate of the cursor's location.
        """
        if self.in_range(mouse_loc):
            self.offset = (mouse_loc[0] - self.loc[0], mouse_loc[1] - self.loc[1])
            self.held = True

    def release(self):
        """
        Releases the object (prevents object from being held).
        """
        self.held = False

    def update_loc(self, mouse_loc: Tuple[float, float]):
        """
        Updates location of the object if it's being held
        :param mouse_loc: (x, y) coordinate of the cursor's location.
        """
        if self.held:
            self.loc = (mouse_loc[0] - self.offset[0], mouse_loc[1] - self.offset[1])

    def display(self):
        """
        Displays image with its current coordinates.
        """
        self.stage.blit(self.img, self.loc)

    def __init__(self, stage, filename: str, loc: Tuple[float, float]):
        # image reference is by its topleft vertex
        self.img = pygame.image.load(filename)
        self.dim = self.img.get_size()
        self.loc = loc
        self.offset = (0, 0)

        self.stage = stage
        self.held = False
