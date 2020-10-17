import pygame
from components.operator import Operator
from components.Shape import Shape


class Addition(Operator):
    def __init__(self, side: int, x: int, y: int):
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
        self.x = x
        self.y = y
        self.draggable = True
        super().__init__(side, x, y)

    def do_operation(self, shape_1: Shape, shape_2: Shape) -> Shape:
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
        pass
        # TODO: this is giving me lots of errors!

        #retTuple = (startPointx + side, startPointy + (side / 2))
        # retShape = Shape(screen, shape1.filename, (shape1.add(shape2).dim,
        #                    retTuple, shape1.color)
        # retShape.update()
        # return retShape

    def draw(self):
        """
        ------------------------------------------------------------------
        draw: Draws the Addition Operator
        ------------------------------------------------------------------
        """
        add_img = pygame.image.load("assets/square.png")
        add_img_rect = add_img.get_rect().move(self.x, self.y)
        return (add_img_rect, add_img)
    
    def selected(self):
        add_select_img = pygame.image.load("assets/square_select.png")
        add_select_rect = add_select_img.get_rect().move(self.x, self.y)
        return (add_select_rect, add_select_img)
