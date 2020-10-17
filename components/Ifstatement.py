import pygame
from components.operator import Operator
from components.Shape import Shape
'''
How to use, 
Make operator Addition by using constructor as such Ifstatement(150,100, 500,500)
here 150 would be rectangle width, 100 would be rectangle height length, 
500 will be starting x position
and 500 will be starting y position

The doOperation Method will draw the shape at the tip of the either bottom
right corner if they are equal and bottom right if they are not, 
use it as such Ifstatement.doOperator(shape1, shape2)


The draw method will return loaded img for the operator, The user can blit it onto
screen as such screen.blit(Ifstatement.draw(), Ifstatement.startPointx, Ifstatement.startPointy

'''
class Ifstatement(Operator):
    def __init__(self, width: int, height :int, startPointx: int, startPointy: int):
        """
        ------------------------------------------------------------------
        __init__: Constructs the Ifstatement object
        ------------------------------------------------------------------
        """    
        self.width = width
        self.height = height
        self.startPointx = startPointx
        self.startPointy = startPointy
    
    def doOperation(self, shape1 : Shape, shape2: Shape) -> Shape:
        """
        ------------------------------------------------------------------
        doOperation: Compares
        ------------------------------------------------------------------
         Parameters:
            shape1: first Shape to be compared
            shape2: Second Shape to be compared
        Returns:
            return newshape on top right corner of square if True
            else on the bottom right cornoer
        """  
        if(shape1.equals(shape2)):
            retTuple = (self.startPointx + self.width, self.startPointy - self.height/2)
            retShape = Shape(shape1.screen, shape1.filename, shape1.scale,
                                retTuple, shape1.color)
            retShape.update()
            return retShape          
        else:
            retTuple = (self.startPointx + self.width, self.startPointy + self.width/2)
            retShape = Shape(shape1.screen, shape1.filename, shape1.scale,
                                retTuple, shape1.color)
            retShape.update()
            return retShape              
        
    def draw(self):
        """
        ------------------------------------------------------------------
        draw: Draws the IfStatement Operator
        ------------------------------------------------------------------
        """  
        ifstatementImg = pygame.image.load("./assets/rectangle.png")
        return ifstatementImg
    
    def selected(self):
        """
        ------------------------------------------------------------------
        draw: Draws the IfStatement Operator
        ------------------------------------------------------------------
        """  
        ifstatementImg = pygame.image.load("./assets/rectangle_select.png")
        return ifstatementImg        
    
        
    
