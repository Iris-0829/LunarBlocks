from components.commands.OperatorNode import OperatorNode
from components.Shape import Shape


class AdditionNode(OperatorNode):

    def execute(self):
        """
        Executes the operation with the given parameters.
        :return: 0 if output is produced, 1 otherwise (lack of parameters).
        """
        # default for now is Shape; might need to extend to Operands later?
        def action(s1: Shape, s2: Shape):
            return s1.add(s2)

        try:
            self.output = action(*tuple(self.params))
            return 0  # passed!

        # lacks parameters, needs to wait for others
        except TypeError:
            return 1  # error!

    def __init__(self, next_node):
        super().__init__(next_node, 2)  # needs 2 operands
