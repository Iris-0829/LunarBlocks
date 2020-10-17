# NOTE: All OperatorNodes should have an execute method which has an action method inside.

class OperatorNode:

    def advance(self) -> None:
        """
        Empties parameters and moves output to the next node.
        """
        # check if it needs parameters
        if self.output is not None and self.next_node is not None and not self.passed:
            # might need to convert to dict for if modules.
            self.next_node.add_params(self.output)
            self.params = []  # reset parameters? not like its going to come back to this again
            self.passed = True

    def add_params(self, operand) -> None:
        """
        Add a parameter to the operator.
        """
        if len(self.params) < self.num_params:
            self.params.append(operand)
        print("Warning: Adding too many parameters here.")

    def __init__(self, next_node, num_params):
        self.params = []
        self.output = None
        self.next_node = next_node
        self.num_params = num_params
        self.passed = False
