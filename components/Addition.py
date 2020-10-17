import pygame
from components.operator import Operator
from components.Shape import Shape

class Addition(Operator):
    def __init__(self, side : int, startPointx: int, startPointy: int):
        """
        ------------------------------------------------------------------
        __init__: Constructs the Addition object
        ------------------------------------------------------------------
         Parameters:
            num1: first number to be added
            num2: second number to be added
        Returns:
            sum of num1 and num2.
        """    
        super().__init__(side, startPointx, startPointy)
        
    
    def doOperation(shape1 : Shape, shape2: Shape) -> Shape:
        """
        ------------------------------------------------------------------
        doOperation: Add given numbers
        ------------------------------------------------------------------
         Parameters:
            Shape1: first number to be added
            Shape2: second number to be added
        Returns:
            sum of num1 and num2.
        """  
        retTuple = (startPointx + side, startPointy + (side/ 2)) 
        retShape = Shape(screen, shape1.filename, (Shape1.add(shape2).dim,
                            retTuple, shape1.color)
        retShape.update()
        return returnShape
    def draw(self, screen):
        """
        ------------------------------------------------------------------
        draw: Draws the Addition Operator
        ------------------------------------------------------------------
        """  
        display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        additionImg = pygame.image.load("assests/triangle.svg")   
        display.blit(additionImg, (startPointx, startPointy))
        
        
    
