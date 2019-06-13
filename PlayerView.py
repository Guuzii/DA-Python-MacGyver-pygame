# -*- coding: utf-8 -*-

import Player

import pygame


class PlayerView():

    def __init__(self, player: Player.Player):
        self.player_img = player.map.pygame_object.load_image(
            "MacGyver.png", -1)
        self.player_render = pygame.transform.scale(self.player_img, (30, 30))
