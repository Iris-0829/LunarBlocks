import pygame
from components.operator import Operator
class Addition(Operator):
    def __init__(self, side: int, startPointx: int, startPointy: int):
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
        
    
    def doOperation(num1 : int, num2: int) -> int:
        """
        ------------------------------------------------------------------
        doOperation: Add given numbers
        ------------------------------------------------------------------
         Parameters:
            num1: first number to be added
            num2: second number to be added
        Returns:
            sum of num1 and num2.
        """        
        return num1 + num2
    def draw(self, screen):
        """
        ------------------------------------------------------------------
        draw: Draws the Addition Operator
        ------------------------------------------------------------------
        """  
        points = []
        points = [(self.startPointx, self.startPointy),
                        (self.startPointx, self.startPointy + self.side),
                        (self.startPointx + self.side, self.startPointy + self.side/2)]
        red = (255, 0, 0)                
        pygame.draw.polygon(screen, red, points)
        
    
