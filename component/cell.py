"""
    Cell Object module
"""

import pygame

from . import position
from . import myPygame


class Cell:
    """
        Cell Object

        Initialize a cell object

        Parameters:
          - position (position.Position): the position object corresponding to the coordinate of the cell
          - pygame_object (myPygame.Pygame): the pygame object to use for render
        
        Attributes:
          - image (pygame.Surface): the surface representing the cell in case of pygame render
          - position (position.Position): argument position
          - item (item.Item): the item positioned on the cell, default=None
          - is_entrance (bool): if the cell is the entrance of the labyrinth, default=False
          - is_exit (bool): if the cell is the exist of the labyrinth, default=False
    """

    def __init__(self, position: position.Position, pygame_object: myPygame.Pygame = None):
        if pygame_object is not None:
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((32, 32))
            self.image.convert()
            self.image.fill((250, 250, 250))
        self.position = position
        self.item = None
        self.is_entrance = False
        self.is_exit = False

    def __eq__(self, other_cell):
        if self.position == other_cell.position:
            return True

        return False

    def __hash__(self):
        return hash(self.position)
