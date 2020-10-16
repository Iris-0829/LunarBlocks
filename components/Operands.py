import pygame
from typing import Tuple


class Operand(pygame.sprite.Sprite):

    def update(self):
        """
        Draws image of self.
        """
        # draw image if applicable
        if self.screen is not None:
            self.img = pygame.transform.scale(self.img, self.dim)
            self.screen.blit(self.img, self.loc)

    def __init__(self, screen, filename: str, dim: Tuple[float, float], loc: Tuple[float, float],
                 color: Tuple[int, int, int]):

        super().__init__()
        self.screen = screen
        self.dim = dim
        self.loc = loc
        self.color = color
        self.filename = filename

        # load image if scene does exist
        if self.screen is not None:
            self.img = pygame.image.load(self.filename)
        else:
            self.img = None

        self.update()
