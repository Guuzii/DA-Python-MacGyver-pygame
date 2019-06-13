# -*- coding: utf-8 -*-

import Item
import MapView
import MyPygame

import pygame


class ItemView:

    def __init__(self, item: Item.Item, pygame_object: MyPygame.Pygame, map_view: MapView.MapView):
        path_img = map_view.path_img_32x32

        if item.isPicked:
            self.item_render = path_img
        else:
            if item.name == "seringue":
                self.item_img = pygame_object.load_image("seringue.png", -1)
            elif item.name == "aiguille":
                self.item_img = pygame_object.load_image("aiguille.png", -1)
            elif item.name == "produit X":
                self.item_img = pygame_object.load_image("ether.png", -1)

            self.item_render = pygame.transform.scale(self.item_img, (30, 30))
