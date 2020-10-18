import unittest
from components.commands.CommandManager import CommandManager
from components.commands.CommandTester import CommandTester
from components.commands.AdditionNode import AdditionNode
from components.Shape import Shape
from components.commands.OutNode import OutNode


class TestCommandManager(unittest.TestCase):

    def setUp(self):
        self.out = OutNode((0, 0))
        self.a1 = AdditionNode(next_node=self.out, loc=(0, 0))
        self.a2 = AdditionNode(next_node=self.a1, loc=(0, 0))
        self.s1 = Shape(None, '', 1, (5, 5), (0, 0, 0))
        self.s2 = Shape(None, '', 2, (5, 5), (0, 0, 0))
        self.s3 = Shape(None, '', 3, (5, 5), (0, 0, 0))

        self.a = [self.a1, self.a2]
        self.ports = [(self.s1, self.a2), (self.s2, self.a2), (self.s3, self.a1)]
        self.cm = CommandManager(ports=self.ports, op_nodes=self.a, out_node=self.out)

    def testExe(self):
        self.cm.reset()
        self.cm.start()
        self.cm.execute()
        self.cm.execute()
        self.assertEqual(self.out.execute()[0].scale, 6)

    def testAuto(self):
        out = self.cm.auto()
        self.assertEqual(out[0].scale, 6)


if '__main__' == __name__:
    out = OutNode((0, 0))
    a1 = AdditionNode(next_node=out, loc=(0, 0))
    a2 = AdditionNode(next_node=a1, loc=(0, 0))
    s1 = Shape(None, '', 1, (5, 5), (0, 0, 0))
    s2 = Shape(None, '', 2, (5, 5), (0, 0, 0))
    s3 = Shape(None, '', 3, (5, 5), (0, 0, 0))
    s4 = Shape(None, '', 6, (5, 5), (0, 0, 0))

    a = [a1, a2]
    ports = [(s1, a2), (s2, a2), (s3, a1)]
    p1 = [s1, s2, s3]
    p2 = [a2, a2, a1]
    ct = CommandTester(p2, a, out)
    print(ct.test_auto(p1, [s4]))