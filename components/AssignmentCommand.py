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
        self.SHAPE_ID = 0

    def add_shape(self, shape: object, shape_img, operator):
        """
        ------------------------------------------------------------------
        add_shape: Given a shape, add it to var_dict with id
        ------------------------------------------------------------------
        """
        self.var_dict[self.SHAPE_ID] = [shape, shape_img, operator]
        self.SHAPE_ID += 1

    def get_shape_id(self, shape: object) -> int:
        """
        ------------------------------------------------------------------
        get_shape_id: Given a shape, return id
        ------------------------------------------------------------------
        """
        for id in self.var_dict:
            if self[id][0] == shape:
                # shape exist in var_dict
                return id
        # shape don't exist in var_dict
        return -1


    def clean_up(self, id: int):
        """
        ------------------------------------------------------------------
        cleanUp: delete the key in memory var_dict
        ------------------------------------------------------------------
        """
        self.removeObject(id)
