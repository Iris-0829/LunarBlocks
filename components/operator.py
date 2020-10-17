import pygame
from pygame.locals import *
import abc
'''
How to use, 
Make operator Addition by using constructor as such Ifstatement(150,100, 500,500)
here 150 would be rectangle width, 100 would be rectangle height length, 
500 will be starting x position
and 500 will be starting y position

The doOperation Method will draw the shape at the tip of the either bottom
right corner if they are equal and bottom right if they are not, 
use it as such doOperator(shape1, shape2)


The draw method will return loaded img for the operator, The user can blit it onto
screen as such screen.blit(Adder.draw(), Adder.startPointx, Adder.startPointy

'''
class Operator(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta
    def __init__(self, side : int, startPointx : int, startPointy : int):
        " Constructor for Operator"
        self.side = side
        self.startPointx = startPointx
        self.startPointy = startPointy
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