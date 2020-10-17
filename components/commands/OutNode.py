class OutNode:

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

    def __init__(self):
        self.params = []
