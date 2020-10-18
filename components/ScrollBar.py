from typing import Tuple

import pygame
from components.Draggable import Draggable


class ScrollBar(Draggable):
    def __init__(self, screen, filename, loc, operators):
        super().__init__(screen, filename, loc)
        self.operators = operators

    def update_loc(self, mouse_loc: Tuple[float, float]):
        """
        Updates location of the object if it's being held
        :param mouse_loc: (x, y) coordinate of the cursor's location.
        """
        if self.held:
            y_before = self.loc[1]
            self.loc = (self.loc[0], mouse_loc[1] - self.offset[1])
            y_after = self.loc[1]
            for operator in self.operators:
                operator.change_loc(y_after - y_before)

