import pygame
from components.Addition import Addition
from components.Operand import Operand
from components.operator import operator
from components.Shape import Shape

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
newshape = Shape(screen, "assest/square.svg", 1, (80,80), (255, 0 ,0))
newshape2 = Shape(screen, "assest/square.svg", 1, (160,160), (255, 0 ,0))
Adder = Addition(100, 200, 200)
Adder.draw()
Adder.doOperation(newshape, newshape2)


    