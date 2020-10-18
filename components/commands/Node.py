import pygame
from typing import Tuple


class Node:

    def draw(self):
        """
        Returns a tuple of a rectangle and image.
        :return: Returns a tuple of (Rect, Image)
        """
        sub_img = pygame.image.load(self.filename_img)
        sub_img_rect = sub_img.get_rect().move(*self.loc)
        return sub_img_rect, sub_img

    def __init__(self, loc: Tuple[float, float], filename_img: str):
        self.filename_img = filename_img
        self.loc = loc
