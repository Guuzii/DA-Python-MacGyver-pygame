"""
    PlayerView pygame.Surface module
"""

import pygame

from component import player

class PlayerView:
    """
        PlayerView pygame.Surface

        Initialize a surface representing the player (MacGyver) in the game

        Parameters:
          - player (player.Player): the player object in the game

        Attributes:
          - player_render (pygame.Surface): the render of the player surface
    """

    def __init__(self, player: player.Player):
        self.player_img = player.labyrinth.pygame_object.load_image("MacGyver.png", -1)
        self.player_render = pygame.transform.scale(self.player_img, (30, 30))
