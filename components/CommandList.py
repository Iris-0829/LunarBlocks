class CommandList:
    """
    ------------------------------------------------------------------
    components.CommandList: Stores all commands in sequential order
    ------------------------------------------------------------------
    """
    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: Initializes CommandList with a list
        ------------------------------------------------------------------
        """
        self.command_list = []
        self.addCommand()

    def addCommand(self, operator: object):
        """
        ------------------------------------------------------------------
        addCommand: Add operators to command_list
        ------------------------------------------------------------------
        """
        if operator not in self.command_list:
            self.command_list.append(operator)


