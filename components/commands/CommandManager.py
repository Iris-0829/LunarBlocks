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
        self.in_node = InNode(ports)
        self.op_nodes = op_nodes
        self.in_node.advance()
        self.out_node = out_node

    def execute(self):
        for op in self.op_nodes:
            # op.execute()
            res = op.execute()
            if res == 0:
                # draw op.output
                op.advance()
                break  # prevents displaying more than one I/O at a time.

    def get_output(self):
        self.out_node.execute()
