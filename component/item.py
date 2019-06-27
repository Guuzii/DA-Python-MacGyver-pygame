"""
    Item Object module
"""
from . import position

class Item:
    """
        Item Object

        Initialize an item object with a name and a position

        Parameters:
          - name (str): the name of the item
          - position (position.Position): the position object corresponding to the coordinate of the item
        
        Attributes:
          - name (str): argument name
          - position (position.Position): argument position
          - isPicked (bool): define if the item is picked by the player or not
    """

    def __init__(self, name: str, position: position.Position=None):
        self.name = name
        self.position = position
        self.isPicked = False
