import pygame
from typing import Tuple


class Operand(pygame.sprite.Sprite):

    def update(self):
        """
        Draws image of self.
        """
        # draw image if applicable
        if self.screen is not None:
            self.img = pygame.transform.scale(self.img,
                                              (self.img.get_size()[0] * self.scale,
                                               self.img.get_size()[1] * self.scale))
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