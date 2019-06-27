"""
    Interface pygame.Surface module
"""

import pygame

from component import labyrinth

class Interface:
    """
        Interface pygame.Surface

        Initialize a surface representing the ingame interface (items picked up)

        Parameters:
          - labyrinth (labyrinth.Labyrinth): the labyrinth the interface will be linked to

        Attributes:
          - interface_render (pygame.Surface): the render of the interface surface
    """

    def __init__(self, labyrinth: labyrinth.Labyrinth):
        self.interface_render = pygame.Surface((labyrinth.pygame_object.screen.get_width(), (labyrinth.pygame_object.screen.get_height() - 480))).convert()
        self.interface_render.fill((0, 0, 0))


        
