from typing import Tuple, Dict, List
from components.Addition import Addition
from components.Shape import Shape


def add(s1: Shape, s2: Shape):
    return s1.add(s2)


class CommandManager:
    def __init__(self, adj_list: list, start: int, end: int) -> None:
        # adj_list format for every element:
        # (operator: Operator, params: []], next: {True: int, False: int} or int)
        self.adj_list = adj_list
        self.start = start
        self.end = end
        self.curr = self.start

    def advance(self, out: List):


    def execute(self, operator_name: str, params: List):
        try:
            if operator_name == 'add':
                return add(*tuple(params))

        # lacks parameters, needs to wait for others
        except TypeError:
            return None
