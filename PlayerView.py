# -*- coding: utf-8 -*- # -tc- inutile!

"""-tc- Ajouter une docstring"""

import Player # -tc- importer pygame avant Player (attention, les noms de 
              # -tc- de modules doivent s'écrire en minuscules)

import pygame


class PlayerView():
    """-tc- Ajouter une docstring"""

    def __init__(self, player: Player.Player):
        """-tc- Ajouter une docstring"""
        self.player_img = player.map.pygame_object.load_image(
            "MacGyver.png", -1)
        self.player_render = pygame.transform.scale(self.player_img, (30, 30))
