# -*- coding: utf-8 -*-


class Position:

    def __init__(self, posX, posY):
        self.X = posX
        self.Y = posY

    def __eq__(self, other_position):
        if self.X == other_position.X and self.Y == other_position.Y:
            return True

        return False

    def __hash__(self):
        return hash((self.X, self.Y))

    def move_up(self):
        return Position(self.X, self.Y - 1)

    def move_down(self):
        return Position(self.X, self.Y + 1)

    def move_left(self):
        return Position(self.X - 1, self.Y)

    def move_right(self):
        return Position(self.X + 1, self.Y)
