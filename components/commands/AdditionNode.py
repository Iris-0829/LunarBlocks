from components.commands.OperatorNode import OperatorNode
from components.Shape import Shape
from typing import Tuple
import pygame


class AdditionNode(OperatorNode):

    def selected(self):
        """
        Returns a tuple of a rectangle and image in the selected state.
        :return: Returns a tuple of (Rect, Image)
        """
        sub_select_img = pygame.image.load("assets/rectangle_select.png")
        sub_select_rect = sub_select_img.get_rect().move(*self.loc)
        return sub_select_rect, sub_select_img

    def execute(self):
        """
        Executes the operation with the given parameters.
        :return: 0 if output is produced, 1 otherwise (lack of parameters).
        """
        # default for now is Shape; might need to extend to Operands later?
        def action(s1: Shape, s2: Shape):
            return s1.add(s2)

        try:
            self.output = action(*tuple(self.params))
            return 0  # passed!

        # lacks parameters, needs to wait for others
        except TypeError:
            return 1  # error!

    def __init__(self, next_node, loc: Tuple[float, float]):
        super().__init__(next_node, 2, loc, './assets/rectangle.png')  # needs 2 operands
