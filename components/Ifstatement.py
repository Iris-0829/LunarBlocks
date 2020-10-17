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
    
    def doOperation(shape1 : Shape, shape2: Shape) -> shape:
        """
        ------------------------------------------------------------------
        doOperation: Add given numbers
        ------------------------------------------------------------------
         Parameters:
            shape1: first Shape to be compared
            shape2: Second Shape to be compared
        Returns:
            return newShape 
        """  
        if(shape1.equals(shape2)):
            retTuple = (startPointx + width, startPointy) 
            retShape = Shape(screen, shape1.filename, Shape1.dim,
                                retTuple, shape1.color)
            retShape.update()
            return retShape          
        else:
            retTuple = (startPointx + width, startPointy + height) 
            retShape = Shape(screen, shape1.filename, Shape1.dim,
                                retTuple, shape1.color)
            retShape.update()
            return retShape              
        
    def draw(self, screen, filename: str):
        """
        ------------------------------------------------------------------
        draw: Draws the Addition Operator
        ------------------------------------------------------------------
        """  
        display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        ifstatementImg = pygame.image.load("assests/rectnagle.svg")   
        display.blit(ifstatementImg, (startPointx, startPointy))        
        
    
