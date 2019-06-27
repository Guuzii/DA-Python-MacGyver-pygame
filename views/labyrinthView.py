"""
    LabyrinthView pygame.Surface module
"""

import pygame

from component import position
from component import cell
from component import labyrinth


class LabyrinthView:
    """
        LabyrinthView pygame.Surface

        Initialize a surface representing the labyrinth in the game

        Parameters:
          - labyrinth (labyrinth.Labyrinth): the labyrinth object for which we doing the render

        Attributes:
          - labyrinth_render (pygame.Surface): the final render of the labyrinth
          - guardian_img (pygame.Surface): the surface representing the guardian at the exit
          - wall_img (pygame.Surface): the surface representing the walls of the labyrinth
          - path_img (pygame.Surface): the surface representing the paths of the labyrinth
    """

    def __init__(self, labyrinth: labyrinth.Labyrinth):
        sprites_sheet = labyrinth.pygame_object.load_image("floor-tiles-20x20.png")

        self.labyrinth_render = pygame.Surface(
            labyrinth.pygame_object.screen.get_size()).convert()
        self.labyrinth_render.fill((25, 25, 25))

        self.guardian_img = labyrinth.pygame_object.load_image("Gardien.png", -1)
        self.guardian_img_30x30 = pygame.transform.scale(self.guardian_img, (30, 30))

        self.wall_img = labyrinth.pygame_object.get_image_at(sprites_sheet, (320, 0, 20, 20))
        self.wall_img_32x32 = pygame.transform.scale(self.wall_img, (32, 32))

        self.path_img = labyrinth.pygame_object.get_image_at(sprites_sheet, (340, 60, 20, 20))
        self.path_img_32x32 = pygame.transform.scale(self.path_img, (32, 32))

        x = 0
        y = 0

        while y < 15:

            if x > 14:
                x = 0

            while x < 15:

                new_position = position.Position(x, y)
                test_cell = cell.Cell(new_position)

                if test_cell in labyrinth.cells:
                    if test_cell == labyrinth.exit:
                        self.labyrinth_render.blit(
                            self.guardian_img_30x30, (x * 32, y * 32))
                    else:
                        self.labyrinth_render.blit(
                            self.path_img_32x32, (x * 32, y * 32))
                else:
                    self.labyrinth_render.blit(self.wall_img_32x32, (x * 32, y * 32))

                x += 1

            y += 1
