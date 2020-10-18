from components.commands.InNode import InNode
from components.commands.OutNode import OutNode


class CommandManager:
    def __init__(self, in_node: InNode, out_node: OutNode, op_nodes: list) -> None:
        """
        Initializes CommandManager.
        :param ports: List of tuples in the form (operand, next_node).
        :param op_nodes: List of all known operator nodes in the stage.
        :param out_node: Node where all operands should meet.
        """

        # input node metadata
        self.ports = in_node.ports
        self.in_node_loc = in_node.loc
        self.in_node_num_input_ports = in_node.num_input_ports

        self.in_node = in_node
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
        self.in_node = InNode(self.ports, self.in_node_loc, self.in_node_num_input_ports)
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
            can_move = self.execute()[0]
        out = self.get_output()
        self.reset()
        return out

    def execute(self):
        """
        Executes an operation, if applicable.
        :returns: True if any of the operators have been executed. False otherwise.
        """
        for op in self.op_nodes:
            # op.execute()
            res = op.execute()
            if res == 0:
                op.advance()
                return True, op.params, op.output
        return False, [], []

    def get_output(self) -> list:
        """
        Returns output as a list.
        :returns: The Output Node's output.
        """
        return self.out_node.execute()
