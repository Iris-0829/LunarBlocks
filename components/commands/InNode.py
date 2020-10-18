from typing import List, Tuple
from components.commands.Node import Node
import pygame


class InNode(Node):

    def clone(self):
        return InNode(self.ports, self.loc, self.num_input_ports)

    def change_operands(self, operands: list):
        new_ports = []
        for i in range(len(operands)):
            new_ports.append((operands[i], self.ports[i][1]))
        self.ports = new_ports

    def change_ports(self, port_nodes: list):
        new_ports = []
        for i in range(len(port_nodes)):
            new_ports.append((self.ports[i][0], port_nodes[i]))
        self.ports = new_ports

    def advance(self):
        """
        Moves operands to their ports.
        NOTE: Call this only ONCE.
        """
        for pair in self.ports:
            pair[1].add_params(pair[0])
        self.ports = []  # ensures its not called again? remove if needed.
    
    def selected(self):
        in_select_img = pygame.image.load("./assets/square_in.png")
        in_select_rect = in_select_img.get_rect().move(*self.loc)
        return in_select_rect, in_select_img

    def __init__(self, ports: List[tuple], loc: Tuple[float, float], num_input_ports: int):
        """
        Initializes InNode.
        :param ports: List of tuples in the form (operand, next_node).
        """
        self.ports = ports
        self.num_input_ports = num_input_ports
        self.draggable = False
        super().__init__(loc, './assets/square_in.png')
