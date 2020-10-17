import pygame
from pygame.locals import *
import abc


class Operator(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta

    def __init__(self, side: int, x: int, y: int):
        " Constructor for Operator"
        self.side = side
        self.x = x
        self.x = y

    @abc.abstractmethod
    def doOperation(self):
        """Does the operation for the given operator 
           and returns the object"""
        return
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def draw(self):
        """Draws the Operator"""
        return
