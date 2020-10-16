from typing import Tuple
from components import operator


class Commands:
    """
    ------------------------------------------------------------------
    components.Commands: Stores all commands in sequential order
    ------------------------------------------------------------------
    """

    def __init__(self, ope: operator):
        """
        ------------------------------------------------------------------
        __init__: Initializes Commands with a list of commands and a test set
        ------------------------------------------------------------------
        """
        self.command = ope
        self.testSet = []

    def addTestCase(self, testInput: Tuple[int, int], testOutput: int):
        """
        ------------------------------------------------------------------
        addTestCase: Add test cases to testSet
        ------------------------------------------------------------------
        Parameters:
            testInput: input of test
            testOutput: expected output
        Returns:
            None
        ------------------------------------------------------------------
        """
        # testInput: (0,1)  testOutput: 1
        # self.testSet: [ [(0,1), 1], [(3,5), 8], [(10, 12), 22]]
        testCase = [testInput, testOutput]
        self.testSet.append(testCase)

    def runTest(self):
        """
        ------------------------------------------------------------------
        runTest: run the test cases in testSet
        ------------------------------------------------------------------
        Returns:
            True if it passes all cases
            False if there's at least one case fails
        ------------------------------------------------------------------
        """
        for test in self.testSet:
            # test: [(0,1), 1]
            # exp = 1
            act = self.command.doOperation(test[0][0], test[0][1])
            exp = test[1]
            if act != exp:
                return False
        return True
