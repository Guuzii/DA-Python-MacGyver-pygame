"""
    Labyrinth Object module
"""

import random

from . import myPygame
from . import position
from . import cell
from . import item


class Labyrinth:
    """
        Labyrinth Object

        Initialize a labyrinth object

        Parameters:
          - pygame_object (myPygame.Pygame): the object representing the pygame instance
        
        Attributes:
          - pygame_object (myPygame.Pygame): argument pygame_object
          - cells (any[]): a list of the different path cells
          - items (any[]): a list of the items positioned on the labyrinth
          - entrance (cell.Cell): the cell representing the entrance of the labyrinth
          - exit (cell.Cell): the cell representing the exit of the labyrinth
          - player (player.Player): the player object linked to the labyrinth
    """

    def __init__(self, pygame_object: myPygame.Pygame=None):
        self.pygame_object = pygame_object
        self.cells = []
        self.items = []
        self.entrance = None
        self.exit = None
        self.player = None

    def create_map(self, file):
        '''
            Open and read a file to create a labyrinth

            Open the .text file passed in argument, read it and create a list of "path" cells depending on the charaters readed 
            Instanciate the items and give them random positions

            Maze in the text file must use the following characters :
              - (#) for walls
              - (-) for paths
              - (E) for entrance
              - (S) for exit

            Parameters:
              - file (str): path to the .txt file to read            
        '''
        with open(file, "r") as file:
            data = file.readlines()

            for y, line in enumerate(data):

                for x, character in enumerate(line.strip()):
                    # set the position with the actual coordinates of the character readed
                    new_position = position.Position(x, y)

                    if character in "ES-":  # the cell is a path, entrance or exit
                        new_cell = cell.Cell(new_position, self.pygame_object)

                        if character == "E":
                            self.entrance = new_cell
                            new_cell.is_entrance = True
                        elif character == "S":
                            self.exit = new_cell
                            new_cell.is_exit = True

                        self.cells.append(new_cell)

        # create items manually and give them coordinates with place_items()
        self.items.append(item.Item("seringue", self.pygame_object))
        self.items.append(item.Item("aiguille", self.pygame_object))
        self.items.append(item.Item("produit X", self.pygame_object))
        self.place_items()

    def place_items(self):
        '''
            Set positions of the elements contained in items[] list randomly and set the corresponding cell.item attribute
        '''
        random_positions = self.get_random_pos()

        for x, item in enumerate(self.items):

            position = random_positions[x]
            item.position = position

            for cell in self.cells:

                if cell.position == item.position:
                    cell.item = item
                    break

    def get_random_pos(self):
        '''
           Randomly pick n elements of cells[] list where n is the number of items available, then return a list of there positions.
        '''
        items_number = len(self.items)
        cells = random.sample(set(self.cells) - {self.entrance, self.exit}, items_number)
        positions = [cell.position for cell in cells]

        return positions
