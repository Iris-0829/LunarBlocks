import pygame
from typing import Tuple


class Node:

    def add_input_port(self, relative_loc: Tuple[float, float]):
        self.input_ports.append(relative_loc)

    def add_output_port(self, relative_loc: Tuple[float, float]):
        self.output_ports.append(relative_loc)

    def draw_port(self, screen, color: Tuple[int, int, int],
                  relative_loc: Tuple[float, float], radius=5):
        # get new location
        loc = (self.loc[0] + relative_loc[0], self.loc[1] + relative_loc[1])
        pygame.draw.circle(screen, color, loc, radius)

    def draw(self, screen, rotate=0):
        """
        Returns a tuple of a rectangle and image.
        :return: Returns a tuple of (Rect, Image)
        """
        sub_img = pygame.image.load(self.filename_img)
        sub_img = pygame.transform.rotate(sub_img, rotate)
        sub_img_rect = sub_img.get_rect().move(*self.loc)
        

        # draw ports
        for port_rel_loc in self.input_ports + self.output_ports:
            self.draw_port(screen, (255, 182, 193), port_rel_loc)  # make constant?

        return sub_img_rect, sub_img

    def __init__(self, loc: Tuple[float, float], filename_img: str):
        self.filename_img = filename_img
        self.loc = loc
        self.input_ports = []  # this and output_parts will have relative positions
        self.output_ports = []
