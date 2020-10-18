import pygame
from typing import Tuple
import math


class Operand(pygame.sprite.Sprite):

    def update(self):
        """
        Draws image of self.
        """
        # draw image if applicable
        if self.screen is not None:
            scalesqrt = math.sqrt(self.scale)
            self.img = pygame.transform.scale(self.img,
                                              (int((self.img.get_size()[0] * scalesqrt)),
                                               int(self.img.get_size()[1] * scalesqrt)))
            self.screen.blit(self.img, self.loc)

    def __init__(self, screen, filename: str, scale: float, loc: Tuple[float, float],
                 color: Tuple[int, int, int]):
        # TODO: Change dimension to scale factor.

        super().__init__()
        self.screen = screen
        self.loc = loc
        self.color = color
        self.filename = filename
        self.scale = scale
        # load image if scene does exist
        if self.screen is not None:
            self.img = pygame.image.load(self.filename)
        else:
            self.img = None

        self.update()