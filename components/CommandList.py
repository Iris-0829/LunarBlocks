from typing import Tuple, List
from components import operator


class Commands:
    """
    ------------------------------------------------------------------
    components.Commands: Stores all commands in sequential order
    ------------------------------------------------------------------
    """
    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: Initializes Commands with a list of commands and a test set
        ------------------------------------------------------------------
        """
        self.commandList = []
        self.testSet = []

    def addTestCase(self, testInput: Tuple[int, int], testOutput: int):
        # testInput: (0,1)  testOutput: 1
        # self.testSet: [ [(0,1), 1], [(3,5), 8], [(10, 12), 22]]
        testCase = [testInput, testOutput]
        self.testSet.append(testCase)

    def addCommand(self, ope: operator):
        self.commandList.append(operator)

    def runTest(self):
        for test in self.testSet:
            # test: [(0,1), 1]
            # exp = 1
            act = run(test[0])
            exp = test[1]
            if act != exp:
                return False
        return True

    def run(self, testInput: Tuple[int, int]):
        # testInput: (0,1)
        # output should 1




