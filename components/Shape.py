from components.Operands import Operand
from typing import TypeVar, Generic, Tuple

shape = TypeVar('shape')


class Shape(Operand, Generic[shape]):

    def clone(self) -> shape:
        """
        Returns a cloned version of itself.
        :returns: Cloned shape.
        """
        return Shape(self.screen, self.filename, self.dim, self.loc, self.color)

    def equals(self, s: shape) -> bool:
        """
        :returns: True if height, width, color and filename image are the same. False otherwise.
        """
        return self.dim == s.dim and self.color == s.color and self.filename == s.filename

    def add(self, s: shape) -> shape:
        """
        Adds the width and height to the original shape.
        :param s: Input shape.
        :returns: Cloned shape with the new dimensions.
        """
        res = self.clone()
        res.dim = (res.dim[0] + s.dim[0], res.dim[1] + s.dim[1])
        return res

    def __init__(self, screen, filename: str, dim: Tuple[float, float], loc: Tuple[float, float],
                 color: Tuple[int, int, int]):
        super().__init__(screen, filename, dim, loc, color)
