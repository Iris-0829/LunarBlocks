import pygame
from components.Shape import Shape

"""
Should delete? after transferring methods over to the SubtractNode.
"""


class Subtraction():
    def __init__(self, side: int, x: int, y: int, draggable = True):
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
        super().__init__(side, x, y, draggable)

    def do_operation(self, num_1: int, num_2: int) -> int:
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
        return num_1 - num_2 if num_1 > num_2 else 0

    def draw(self):
        """
        ------------------------------------------------------------------
        draw: Return tuple of (Rect, Image)
        ------------------------------------------------------------------
        """
        sub_img = pygame.image.load("assets/rectangle.png")
        sub_img_rect = sub_img.get_rect().move(self.x, self.y)
        return (sub_img_rect, sub_img)

    def selected(self):
        sub_select_img = pygame.image.load("assets/rectangle_select.png")
        sub_select_rect = sub_select_img.get_rect().move(self.x, self.y)
        return (sub_select_rect, sub_select_img)
