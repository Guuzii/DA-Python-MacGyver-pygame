"""
    ItemView pygame.Surface module
"""

import pygame

from component import item
from component import myPygame
from . import labyrinthView


class ItemView:
    """
        ItemView pygame.Surface

        Initialize a surface representing an item in the game

        Parameters:
          - item (item.Item): the item to render
          - pygame_object (myPygame.Pygame): the object representing the pygame instance
          - labyrinth_view (labyrinthView.LabyrinthView) 

        Attributes:
          - interface_render (pygame.Surface): the render of the interface surface
    """

    def __init__(self, item: item.Item, pygame_object: myPygame.Pygame, labyrinth_view: labyrinthView.LabyrinthView, interface=None):
        path_img = labyrinth_view.path_img_32x32

        if item.isPicked and interface is None:
            self.item_render = path_img
        else:
            if item.name == "seringue":
                self.item_img = pygame_object.load_image("seringue.png", -1)
            elif item.name == "aiguille":
                self.item_img = pygame_object.load_image("aiguille.png", -1)
            elif item.name == "produit X":
                self.item_img = pygame_object.load_image("ether.png", -1)

            self.item_render = pygame.transform.scale(self.item_img, (30, 30))
