"""
    Player Object module
"""

import pygame

from . import labyrinth
from . import cell


class Player:
    """
        Player Object

        Initialize a player object

        Parameters:
          - labyrinth (labyrinth.Labyrinth): the labyrinth object the player will be linked to
        
        Attributes:
          - position (position.Position): the position object corresponding to the coordinate of the player
          - items (any[]): the list of items the player have
          - labyrinth (labyrinth.Labyrinth): the labyrinth the player is linked to
    """

    def __init__(self, labyrinth: labyrinth.Labyrinth):
        self.position = labyrinth.entrance.position
        self.items = []
        self.labyrinth = labyrinth

        self.labyrinth.player = self


    def move(self, instruction):
        '''
            Call the method specified in argument from position object to get futur position
            If futur position is a path, update player position and call pick_item()

            Parameters:
              - instruction (str): then name of the position object's method to call

            Returns:
              - True: the player can move to the new coordinate
              - False: the player can't move to the new coordinate
        '''
        
        new_position = getattr(self.position, instruction)()
        new_cell = cell.Cell(new_position)

        if new_cell in self.labyrinth.cells:
            self.position = new_position
            self.pick_item(new_cell)
            return True
        else:
            return False


    def pick_item(self, test_cell):
        '''
            Iterate through the labyrinth's items list to find the same cell object than in arguments.
            Check if the found cell has the same position than the player and an item.
            If the found cell object got an item, append it to the player's list

            Parameters:
              - test_cell (cell.Cell): the cell object the player is moving to
        '''

        for cell in self.labyrinth.cells:

            if cell == test_cell and cell.position == self.position and cell.item is not None:
                cell.item.isPicked = True
                self.items.append(cell.item)
                cell.item = None
                break


    def can_exit(self):
        '''
            If player is at the exit, check for his items and return true if end of game condition

            Returns:
              - "victory" (bool: True): player position = exit position and he have all items
              - "defeat" (bool: True): player position = exit position and he doesn't have all items
              - False: player position != exit position
        '''

        if self.position == self.labyrinth.exit.position:
            if len(self.items) == len(self.labyrinth.items):
                return "victory"
            else:
                return "defeat"
        else:
            return False
