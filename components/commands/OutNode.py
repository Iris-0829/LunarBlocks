from components.commands.Node import Node
from typing import Tuple
import pygame


class OutNode(Node):

    def add_port(self, relative_loc: Tuple[float, float]):
        self.ports.append(relative_loc)

    def execute(self):
        """
        Returns received output.
        """
        return self.params

    def add_params(self, operand):
        """
        Add a parameter to the output node.
        """
        self.params.append(operand)

    def selected(self):
        out_select_img = pygame.image.load("./assets/square_out_select.png")
        out_select_rect = out_select_img.get_rect().move(*self.loc)
        return out_select_rect, out_select_img

    def __init__(self, loc: Tuple[float, float], num_output_ports: int):
        self.params = []
        self.ports = []
        self.num_output_ports = num_output_ports
        self.draggable = False
        super().__init__(loc, './assets/square_out.png')
