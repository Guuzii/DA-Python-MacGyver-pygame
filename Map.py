# -*- coding: utf-8 -*-

import MyPygame
import Position
import Cell
import Item

import random


class Map:

    def __init__(self, pygame_object: MyPygame.Pygame = None):
        self.pygame_object = pygame_object
        self.cells = []
        self.items = []
        self.entrance = None
        self.exit = None
        self.player = None

    def create_map(self, file):
        '''
            Open the .text file passed in argument, read it and create a list of "path" cells depending on the charaters readed. 
            Then instanciate the items and give them random positions.

            Arguments:
                - file = path to the .txt file to read

            Maze in the text file must use the following characters :
                - (#) for walls
                - (-) for paths
                - (E) for entrance
                - (S) for exit
        '''
        with open(file, "r") as file:
            data = file.readlines()

            for y, line in enumerate(data):

                for x, character in enumerate(line.strip()):
                    # set the position with the actual coordinates of the character readed
                    position = Position.Position(x, y)

                    if character in "ES-":  # the cell is a path, entrance or exit
                        cell = Cell.Cell(position, self.pygame_object)

                        if character == "E":
                            self.entrance = cell
                            cell.is_entrance = True
                        elif character == "S":
                            self.exit = cell
                            cell.is_exit = True

                        self.cells.append(cell)

        # create items manually and give them coordinates with place_items()
        self.items.append(Item.Item("seringue", self.pygame_object))
        self.items.append(Item.Item("aiguille", self.pygame_object))
        self.items.append(Item.Item("produit X", self.pygame_object))
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
            Pick elements of cells[] list depending on the number of items available and return a list of there positions.
        '''
        items_number = len(self.items)
        cells = random.sample(
            set(self.cells) - {self.entrance, self.exit}, items_number)
        positions = [cell.position for cell in cells]

        return positions
