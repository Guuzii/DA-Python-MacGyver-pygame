"""
    MyPygame Object module
"""

import os
import sys

import pygame


class Pygame:
    """
        Pygame Object

        Initialize an pygame instance

        Parameters:
          - screen_dimension (tuple): the dimension of the pygame window
        
        Attributes:
          - screen (pygame.Screen): window chere the game will run
    """

    def __init__(self, screen_dimension: tuple = (640, 480)):
        pygame.init()
        pygame.time.Clock().tick(30)
        self.screen = pygame.display.set_mode(screen_dimension)
        pygame.display.set_caption("MacGyver's Journey")


    def load_image(self, name, colorkey=None):
        '''
            Load an image from the local ressources/images directory and return a new surface from it

            Parameters:
              - name (str): the name of the image file to load with its extension (.png, .jpg)
              - colorkey (int/tuple): the color to set transparent. RGB format or -1 for top left corner color

            Returns:
              - image (pygame.Surface): a surface representing the image
        '''

        fullpath = os.path.join('ressources/images', name)

        try:
            image = pygame.image.load(fullpath)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()

        except pygame.error:
            print('Cannot load image: ', name)
            raise SystemExit

        # Set transparancy of the color in argument
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))

            image.set_colorkey(colorkey, pygame.RLEACCEL)

        return image


    def get_image_at(self, img_sheet: pygame.Surface, rectangle: pygame.Rect, colorkey=None):
        '''
            Get a portion of an image and return a new surface with it.

            Parameters :
                - img_sheet (pygame.Surface): the image surface to crop
                - rectangle (pygame.Rect): the postion and the dimension of the crop to do
                - colorkey (int/tuple): the color to set transparent. RGB format or -1 for top left corner color
        '''

        # Get image from x,y,x+offset,y+offset (rectangle argument)
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size)

        image.blit(img_sheet, (0, 0), rect)

        # Set transparancy of the color in argument
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))

            image.set_colorkey(colorkey, pygame.RLEACCEL)

        return image
