import unittest
from components.commands.CommandManager import CommandManager
from components.commands.AdditionNode import AdditionNode
from components.Shape import Shape
from components.commands.OutNode import OutNode


class TestCommandManager(unittest.TestCase):

    def setUp(self):
        self.out = OutNode()
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
