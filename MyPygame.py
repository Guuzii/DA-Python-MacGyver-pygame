# -*- coding: utf-8 -*-

import os
import sys
import pygame


class Pygame:

    def __init__(self, screen_dimension: tuple = (640, 480)):
        pygame.init()
        pygame.time.Clock().tick(30)
        self.screen = pygame.display.set_mode(screen_dimension)
        pygame.display.set_caption("MacGyver Escapes")

    def load_image(self, name, colorkey=None):
        '''
            Load the image with from the local ressources/images directory and return a new surface from it.
            Arguments :
                - name = the name of the image file to load
                - colorkey = the color to set transparent. RGB format or -1 for top left corner color
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

    def get_image_at(self, sheet: str, rectangle: pygame.Rect, colorkey=None):
        '''
            Get a portion of an image and return a new surface with it.

            Arguments :
                - sheet = the image to crop
                - rectangle = the postion and the dimension on the crop to do
                - colorkey = the color to set transparent. RGB format or -1 for top left corner color
        '''
        # Loads image from x,y,x+offset,y+offset (rectangle argument)
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size)

        image.blit(sheet, (0, 0), rect)

        # Set transparancy of the color in argument
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))

            image.set_colorkey(colorkey, pygame.RLEACCEL)

        return image
