import pygame
from components.operator import Operator
from components.Shape import Shape
from components.Operand import Operand
from typing import TypeVar, Generic, Tuple
'''
How to use, 
Make operator Addition by using constructor as such Addition(100,500,500)
here 100 would be trianlge side length, 500 will be starting x position
and 500 will be starting y position

The doOperation Method will draw the shape at the tip of the triangle of the
operator, use it as such Ifstatement.doOperator(shape1, shape2)


The draw method will return loaded img for the operator, The user can blit it onto
screen as such screen.blit(Adder.draw(), Adder.startPointx, Adder.startPointy

'''

"""
Delete?
"""

class Addition(Operator):
    def __init__(self, side: int, x: int, y: int):
        """
        ------------------------------------------------------------------
        __init__: Constructs the Addition object
        ------------------------------------------------------------------
         Parameters:
            side: side of triangle
            x: locations for x
            y: location for y
        Returns:
            nothing
        """
        super().__init__(side, x, y)

    def doOperation(self, shape1: Shape, shape2: Shape) -> Shape:
        """
        ------------------------------------------------------------------
        doOperation: Add given Shapes
        ------------------------------------------------------------------
         Parameters:
            Shape1: first number to be added
            Shape2: second number to be added
        Returns:
            sum of Shape1 and Shape2.
        """

        retTuple = (self.startPointx + self.side, self.startPointy)
        retShape = Shape(shape1.screen, shape1.filename, (shape1.add(shape2)).scale,
                           retTuple, shape1.color)
        retShape.update()
        return retShape

    def draw(self):
        """
        ------------------------------------------------------------------
        draw: Draws the Addition Operator
        ------------------------------------------------------------------
        """
        add_img = pygame.image.load("./assets/triangle.png")
        return add_img
    
    def selected(self):
        add_select_img = pygame.image.load("./assets/triangle_select.png")
        return add_select_img