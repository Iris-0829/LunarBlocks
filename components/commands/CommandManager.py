from typing import List
from components.commands.InNode import InNode
from components.commands.OutNode import OutNode


class CommandManager:
    def __init__(self, ports: List[tuple], op_nodes: list, out_node: OutNode) -> None:
        """
        Initializes CommandManager.
        :param ports: List of tuples in the form (operand, next_node).
        :param op_nodes: List of all known operator nodes in the stage.
        """
        self.ports = ports
        self.in_node = InNode(ports)
        self.op_nodes = op_nodes
        self.out_node = out_node

    def start(self):
        """
        Moves shapes in the input node into the operator nodes.
        """
        self.in_node.advance()

    def reset(self):
        """
        Resets all nodes back to what it was.
        """
        self.in_node = InNode(self.ports)
        self.out_node.params = []
        for op in self.op_nodes:
            op.params = []
            op.passed = False
            op.output = None

    def execute(self):
        """
        Executes an operation, if applicable.
        """
        for op in self.op_nodes:
            # op.execute()
            res = op.execute()
            if res == 0:
                # draw op.output
                op.advance()
                break  # prevents displaying more than one I/O at a time.

    def get_output(self) -> list:
        """
        Returns output as a list.
        """
        return self.out_node.execute()
