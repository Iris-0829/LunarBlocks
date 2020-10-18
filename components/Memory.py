"""
Delete?
"""

class Memory:
    """
    ------------------------------------------------------------------
    components.Memory: Store variables and values
    ------------------------------------------------------------------
    """

    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: Initializes Memory with a dictionary in {id: [shape,img,operator]}
        ------------------------------------------------------------------
        """
        self.var_dict = {}

    def removeObject(self, id: int):
        """
        ------------------------------------------------------------------
        removeObject: remove the variable with id if it exists in var_dict
        ------------------------------------------------------------------
        Parameters:
            id: Unique string of variable
        Returns:
            None
        ------------------------------------------------------------------
        """
        if id in self.var_dict:
            del self.var_dict[id]

    def assign(self, id1: int, id2: int):
        """
        ------------------------------------------------------------------
        assign: Assigns contents of variable at id1 to the variable at id2
        ------------------------------------------------------------------
        Parameters:
            id1: id of the variable that assigns content
            id2: id of the variable that is assigned
        Returns:
            None
        ------------------------------------------------------------------
        """
        if id1 not in self.var_dict:
            return

        var1 = self.var_dict[id1]
        newObj = var1.clone()
        self.var_dict[id2] = newObj


