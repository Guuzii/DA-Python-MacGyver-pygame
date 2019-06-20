# -*- coding: utf-8 -*- # -tc- inutile!

"""-tc- Ajouter une docstring"""

class Position:
    """-tc- Ajouter une docstring"""

    def __init__(self, posX, posY):
        """-tc- Ajouter une docstring"""
        self.X = posX
        self.Y = posY

    def __eq__(self, other_position):
        """-tc- Ajouter une docstring"""
        if self.X == other_position.X and self.Y == other_position.Y:
            return True

        return False

    def __hash__(self):
        """-tc- Ajouter une docstring"""
        return hash((self.X, self.Y))

    def move_up(self):
        """-tc- Ajouter une docstring"""
        return Position(self.X, self.Y - 1)

    def move_down(self):
        """-tc- Ajouter une docstring"""
        return Position(self.X, self.Y + 1)

    def move_left(self):
        """-tc- Ajouter une docstring"""
        return Position(self.X - 1, self.Y)

    def move_right(self):
        """-tc- Ajouter une docstring"""
        return Position(self.X + 1, self.Y)
