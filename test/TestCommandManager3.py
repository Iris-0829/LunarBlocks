# from components.commands.CommandManager import CommandManager
from components.commands.CommandTester import CommandTester
from components.commands.AdditionNode import AdditionNode
from components.commands.InequalityNode import InequalityNode
from components.commands.EqualityNode import EqualityNode
from components.Shape import Shape
from components.commands.InNode import InNode
from components.commands.OutNode import OutNode

out = OutNode((0, 0), 1)
a1 = EqualityNode(next_node=out, loc=(0, 0))
a2 = AdditionNode(next_node=a1, loc=(0, 0))
s1 = Shape(None, '', 1, (5, 5), (0, 0, 0))
s2 = Shape(None, '', 2, (5, 5), (0, 0, 0))
s3 = Shape(None, '', 3, (5, 5), (0, 0, 0))

s4 = Shape(None, '', 3, (5, 5), (0, 0, 0))

a = [a1, a2]
ports = [(s1, a2), (s2, a2), (s3, a1)]
p1 = [s1, s2, s3]
p2 = [a2, a2, a1]
in_node = InNode(ports, (0, 0), 3)
ct = CommandTester(in_node, out, a)
print(ct.test_auto(p1, [True]))