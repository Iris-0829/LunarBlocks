from components.operands import Operand
from typing import TypeVar, Generic

shape = TypeVar('shape')


class Shape(Operand, Generic[shape]):

    def clone(self) -> shape:
        """
        Returns a cloned version of itself.
        :returns: Cloned shape.
        """
        return Shape(self.width, self.height, self.x, self.y, self.color)

    def equals(self, s: shape) -> bool:
        return self.width == s.width and self.height == s.height and self.color == s.color

    def add(self, s: shape) -> shape:
        """
        Adds the width and height to the original shape.
        :param s: Input shape.
        :returns: Cloned shape with the new dimensions.
        """
        res = self.clone()
        res.width += s.width
        res.height += s.height
        return res

    def __init__(self, width: float, height: float, x: float, y: float, color: str):
        super().__init__(width, height, x, y, color)
