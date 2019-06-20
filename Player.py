# -*- coding: utf-8 -*- # -tc- inutile!

"""-tc- Ajouter une docstring"""

import Cell # -tc- importer pygame avant et éviter les maj
import EndView

import pygame


class Player:
    """-tc- Ajouter une docstring"""

    def __init__(self, map):
        """-tc- Ajouter une docstring"""
        self.position = map.entrance.position
        self.items = []
        self.map = map
        self.map.player = self

    def move(self, instruction):
        '''
            Call the method specified in argument from position object to get get futur position.
            If futur position is a path, update player position and call pick_item().
        '''
        new_position = getattr(self.position, instruction)()
        new_cell = Cell.Cell(new_position)

        if new_cell in self.map.cells:
            self.position = new_position
            self.pick_item(new_cell)
            return True
        else:
            return False

    def pick_item(self, test_cell):
        '''
            Look for element in cell[] list same as test_cell in argument.
            Check if the found cell has the same position than the player and an item, and give it to the player if that's the case.
        '''
        for cell in self.map.cells:

            if cell == test_cell and cell.position == self.position and cell.item is not None:
                print("Vous trouvez un objet au sol : {}. \nVous le prenez.".format(
                    cell.item.name))
                cell.item.isPicked = True
                self.items.append(cell.item)
                cell.item = None

                print("\nVous avez maintenant {} objet(s) en votre possesion :".format(
                    len(self.items)))
                for item in self.items:

                    print(item.name)

                break

    def can_exit(self):
        '''
            If player is at the exit, check for his items and return true if end of game condition
        '''
        if self.position == self.map.exit.position:
            if len(self.items) == len(self.map.items):
                return "victory"
            else:
                return "defeat"
        else:
            return False
