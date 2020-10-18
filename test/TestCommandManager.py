from components.commands.CommandManager import CommandManager
from components.commands.AdditionNode import AdditionNode
from components.Shape import Shape
from components.commands.OutNode import OutNode

out = OutNode()
a1 = AdditionNode(next_node=out, loc=(0, 0))
a2 = AdditionNode(next_node=a1, loc=(0, 0))
s1 = Shape(None, '', 1, (5, 5), (0, 0, 0))
s2 = Shape(None, '', 2, (5, 5), (0, 0, 0))
s3 = Shape(None, '', 3, (5, 5), (0, 0, 0))

a = [a1, a2]
ports = [(s1, a2), (s2, a2), (s3, a1)]
cm = CommandManager(ports=ports, op_nodes=a, out_node=out)
cm.start()
cm.execute()
cm.execute()
print(out.execute()[0].scale)
cm.reset()
cm.start()
cm.execute()
cm.execute()
print(out.execute()[0].scale)
print(cm.auto()[0].scale)
