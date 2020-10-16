from components import Memory


class AssignmentCommand(Memory):
    """
    ------------------------------------------------------------------
    components.AssignmentCommand:
    ------------------------------------------------------------------
    """

    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: Initializes AssignmentCommand
        ------------------------------------------------------------------
        """
        Memory.__init__(self)

    def assignIdObj(self, id: str, obj: object):
        """
        ------------------------------------------------------------------
        assignIdObj: Given an object, add it to var_dict with id
        ------------------------------------------------------------------
        """
        self.var_dict[id] = obj

    def cleanUp(self, id: str):
        """
        ------------------------------------------------------------------
        cleanUp: delete the key in memory var_dict
        ------------------------------------------------------------------
        """
        self.removeObject(id)
