from typing import List
from components.commands.InNode import InNode
from components.commands.OutNode import OutNode


class CommandManager:
    def __init__(self, ports: List[tuple], op_nodes: list, out_node: OutNode) -> None:
        """
        Initializes CommandManager.
        :param ports: List of tuples in the form (operand, next_node).
        :param op_nodes: List of all known operator nodes in the stage.
        :param out_node: Node where all operands should meet.
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

    def auto(self) -> list:
        """
        Automatically executes methods.
        :returns: List of output produced from the Output Node.
        """
        self.reset()
        self.start()
        can_move = True
        while can_move:
            can_move = self.execute(draw_mode=False)
        out = self.get_output()
        self.reset()
        return out

    def execute(self, draw_mode=True) -> bool:
        """
        Executes an operation, if applicable.
        :returns: True if any of the operators have been executed. False otherwise.
        """
        for op in self.op_nodes:
            # op.execute()
            res = op.execute()
            if res == 0:
                # draw op.output (use draw_mode to determine whether to do this or not).
                op.advance()
                return True
        return False

    def get_output(self) -> list:
        """
        Returns output as a list.
        :returns: The Output Node's output.
        """
        return self.out_node.execute()
