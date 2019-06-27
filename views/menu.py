"""
    Menu pygame.Surface module
"""

import pygame

from component import myPygame


class Menu:
    """
        Menu pygame.Surface

        Initialize a surface representing the menu at the start of the game

        Parameters:
          - pygame_object (myPygame.Pygame): the object representing the pygame instance 

        Attributes:
          - menu_render (pygame.Surface): the render of the menu Surface
    """

    def __init__(self, pygame_object: myPygame.Pygame):
        self.menu_render = pygame.Surface(
            pygame_object.screen.get_size()).convert()
        self.menu_render.fill((15, 15, 15))

        self.font = pygame.font.Font(None, 28)
        self.text = self.font.render(
            '"espace"= Nouvelle partie, "échap"= Quitter', 1, (250, 250, 250))
        self.textPos = self.text.get_rect()
        self.textPos.centerx = self.menu_render.get_rect().centerx
        self.textPos.centery = self.menu_render.get_rect().centery

        self.menu_render.blit(self.text, self.textPos)
