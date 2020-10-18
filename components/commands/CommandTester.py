from components.commands.CommandManager import CommandManager
from components.commands.OutNode import OutNode
from components.commands.InNode import InNode


def verify(res: list, expected: list):
    """
    Checks if lists are the same.
    :param res: List that is actually produced.
    :param expected: List that is expected.
    :return: True if res == expected.
    """
    if len(res) != len(expected):
        return False
    for i in range(len(res)):
        if not res[i].equals(expected[i]):
            return False
    return True


class CommandTester:
    def __init__(self, in_node: InNode, out_node: OutNode, op_nodes: list):
        """
        Initializes CommandTester.
        :param ports: List of ports that each shape should go in.
        :param out_node: Node where all operands should meet.   
        :param op_nodes: List of all known operator nodes in the stage.
        """
        self.ports = in_node.ports
        self.in_node_loc = in_node.loc

        self.op_nodes = op_nodes
        self.out_node = out_node
        self.in_node = in_node

    def test(self, operands: list) -> CommandManager:
        """
        Returns CommandManager with the following operands for the ports.
        :param operands: List of operands ( len(operands) == len(self.ports) ).
        :return: CommandManager with the following operands.
        """

        # build ports for CommandManager
        local_in_node = self.in_node.clone()
        local_in_node.change_operands(operands)
        return CommandManager(local_in_node, self.out_node, self.op_nodes)

    def test_auto(self, operands: list, expected: list) -> bool:
        """
        Automatically tests CommandManager and compares it against whats produced and expected.
        :param operands: List of operands ( len(operands) == len(self.ports) ).
        :param expected: List of what we expect from the output.
        :return: True if expected = operands.
        """
        cm = self.test(operands)
        out = cm.auto()
        return verify(out, expected)
