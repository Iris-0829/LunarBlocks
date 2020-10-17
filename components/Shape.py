from components.Operand import Operand
from typing import TypeVar, Generic, Tuple

shape = TypeVar('shape')


class Shape(Operand, Generic[shape]):

    def clone(self) -> shape:
        """
        Returns a cloned version of itself.
        :returns: Cloned shape.
        """
        return Shape(self.screen, self.filename, self.scale, self.loc, self.color)

    def equals(self, s: shape) -> bool:
        """
        :returns: True if height, width, color and filename image are the same. False otherwise.
        """
        return self.scale == s.scale and self.color == s.color and self.filename == s.filename

    def add(self, s: shape) -> shape:
        """
        Adds the width and height to the original shape.
        :param s: Input shape.
        :returns: Cloned shape with the new dimensions.
        """
        res = self.clone()
        res.scale += s.scale
        return res

    def __init__(self, screen, filename: str, scale: float, loc: Tuple[float, float],
                 color: Tuple[int, int, int]) -> None:
        super().__init__(screen, filename, scale, loc, color)
