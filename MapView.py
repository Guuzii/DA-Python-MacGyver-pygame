# -*- coding: utf-8 -*- -tc- inutile!

"""-tc- Ajouter une docstring"""

# -tc- importer pygame ici

import Position # -tc- éviter les majuscules dans les noms de modules
import Cell
import Map

import pygame


class MapView():
    """-tc- Ajouter une docstring"""

    def __init__(self, map: Map.Map):
        """-tc- Ajouter une docstring"""
        sprites_sheet = map.pygame_object.load_image("floor-tiles-20x20.png")

        self.map_render = pygame.Surface(
            map.pygame_object.screen.get_size()).convert()
        self.map_render.fill((25, 25, 25))

        self.guardian_img = map.pygame_object.load_image("Gardien.png", -1)
        self.guardian_img_30x30 = pygame.transform.scale(
            self.guardian_img, (30, 30))

        self.wall_img = map.pygame_object.get_image_at(
            sprites_sheet, (320, 0, 20, 20))
        self.wall_img_32x32 = pygame.transform.scale(self.wall_img, (32, 32))

        self.path_img = map.pygame_object.get_image_at(
            sprites_sheet, (340, 60, 20, 20))
        self.path_img_32x32 = pygame.transform.scale(self.path_img, (32, 32))

        x = 0
        y = 0

        # -tc- utiliser une boucle for serait plus pythonique
        while y < 15: # -tc- attention aux nombres magiques comme 15, 14!!!

            if x > 14:
                x = 0

            # -tc- utiliser une boucle for serait plus pythonique
            while x < 15:

                position = Position.Position(x, y)
                test_cell = Cell.Cell(position)

                if test_cell in map.cells:
                    if test_cell == map.exit:
                        self.map_render.blit(
                            # -tc- attention aux nombre magiques comme 32!
                            self.guardian_img_30x30, (x * 32, y * 32))
                    else:
                        self.map_render.blit(
                            self.path_img_32x32, (x * 32, y * 32))
                else:
                    self.map_render.blit(self.wall_img_32x32, (x * 32, y * 32))

                x += 1 # -tc- peut être évité avec une boucle for

            y += 1 # -tc- peut être évité avec une boucle for
