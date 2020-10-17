import pygame
from components.operator import Operator
from components.Shape import Shape
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
            retTuple = (self.startPointx + self.width, self.startPointy)
            retShape = Shape(self.screen, shape1.filename, self.Shape1.dim,
                                retTuple, shape1.color)
            retShape.update()
            return retShape          
        else:
            retTuple = (self.startPointx + self.width, self.startPointy + self.height)
            retShape = Shape(self.screen, shape1.filename, self.Shape1.dim,
                                retTuple, shape1.color)
            retShape.update()
            return retShape              
        
    def draw(self, screen, filename: str):
        """
        ------------------------------------------------------------------
        draw: Draws the IfStatement Operator
        ------------------------------------------------------------------
        """  
        display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        ifstatementImg = pygame.image.load("assests/rectangle.svg")
        display.blit(ifstatementImg, (self.startPointx, self.startPointy))
        
    
