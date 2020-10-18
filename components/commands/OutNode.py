from components.commands.Node import Node
from typing import Tuple


class OutNode(Node):

    def execute(self):
        """
        Returns received output.
        """
        return self.params

    def add_params(self, operand):
        """
        Add a parameter to the output node.
        """
        self.params.append(operand)

    def __init__(self, loc: Tuple[float, float]):
        self.params = []
        super().__init__(loc, './assets/triangle.png')
