"""
    Position Object module
"""

class Position:
    """
        Position Object

        Initialize a position object

        Parameters:
          - posX (int): the X index (horizontal coordinate) of the position
          - posY (int): the y index (vertical coordinate) of the position
        
        Attributes:
          - X (int): argument posX
          - Y (int): argument posY
    """

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
        """Return a new position with Y = Y-1"""
        return Position(self.X, self.Y - 1)


    def move_down(self):
        """Return a new position with Y = Y+1"""
        return Position(self.X, self.Y + 1)


    def move_left(self):
        """Return a new position with X = X-1"""
        return Position(self.X - 1, self.Y)
        

    def move_right(self):
        """Return a new position with X = X+1"""
        return Position(self.X + 1, self.Y)
