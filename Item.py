# -*- coding: utf-8 -*-


class Item:

    def __init__(self, name, position=None):
        self.name = name
        self.position = position
        self.isPicked = False
