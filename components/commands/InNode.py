from typing import List, Tuple
from components.commands.Node import Node


class InNode(Node):
    def advance(self):
        """
        Moves operands to their ports.
        NOTE: Call this only ONCE.
        """
        for pair in self.ports:
            pair[1].add_params(pair[0])
        self.ports = []  # ensures its not called again? remove if needed.

    def __init__(self, ports: List[tuple], loc: Tuple[float, float]):
        """
        Initializes InNode.
        :param ports: List of tuples in the form (operand, next_node).
        """
        self.ports = ports
        super().__init__(loc, './assets/triangle.png')
