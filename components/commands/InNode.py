from typing import List


class InNode:
    def advance(self):
        """
        Moves operands to their ports.
        NOTE: Call this only ONCE.
        """
        for pair in self.ports:
            pair[1].add_params(pair[0])
        self.ports = []  # ensures its not called again? remove if needed.

    def __init__(self, ports: List[tuple]):
        """
        Initializes InNode.
        :param ports: List of tuples in the form (operand, next_node).
        """
        self.ports = ports
