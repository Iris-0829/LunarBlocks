from components import operator
import List
import Tuple
class Addition(operator):
    def __init__(self, side : int ,startPointx: int, startPointy: int):
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
        return num1 - num2
    def draw():
        """
        ------------------------------------------------------------------
        draw: Draws the Subtraction Operator
        ------------------------------------------------------------------
        """  
        points = []
        points = [(self.startPointx, self.startPointy),
                        (self.startPointx, self.startPointy + side),
                        (self.startPointx + side, self.startPointy + side/2)]
        blue = (0, 0, 255)                
        pygame.draw.polygon(window, blue, points)
        return
        
