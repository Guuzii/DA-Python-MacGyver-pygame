# -*- coding: utf-8 -*-

"""-tc- docstring"""

import MyPygame
import pygame # -tc- attention à l'ordre des imports


class EndView:
    """-tc- docstring"""

    def __init__(self, pygame_object: MyPygame.Pygame, victory: bool):
        """-tc- docstring"""
        self.end_render = pygame.Surface(
            pygame_object.screen.get_size()).convert()
        self.end_render.fill((15, 15, 15))

        self.font = pygame.font.Font(None, 28)
        if victory:
            self.text = self.font.render(
                'Vous vous étes échapé, Victoire !', 1, (0, 153, 0))
        else:
            self.text = self.font.render(
                'Le gardien vous attrape, Défaite !', 1, (153, 0, 0))
        self.textPos = self.text.get_rect()
        self.textPos.centerx = self.end_render.get_rect().centerx
        self.textPos.centery = self.end_render.get_rect().centery

        self.end_render.blit(self.text, self.textPos)
