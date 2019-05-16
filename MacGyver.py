import random


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
        

    def move_top(self):
        self.Y -= 1

    def move_bot(self):
        self.Y += 1

    def move_left(self):
        self.X -= 1

    def move_right(self):
        self.X += 1


class Cell:

    def __init__(self, position, is_entrance=False, is_exit=False):
        self.position = position
        self.item = None
        self.player = None
        self.is_entrance = is_entrance
        self.is_exit = is_exit

    def __eq__(self, other_cell):
        if self.position == other_cell.position:
            return True
        
        return False

    def __hash__(self):
        return hash(self.position)


class Player:

    def __init__(self, map):
        self.position = map.entrance.position
        map.entrance.player = True
        self.items = []
        self.map = map
        self.map.player = self

    def move(self, direction):
        """
        if direction == toucheClavierFlecheHaut:
            self.position.move_top()
        elif direction == toucheClavierFlecheBas:
            self.position.move_bot()
        elif direction == toucheClavierFlecheGauche:
            self.position.move_left()
        elif direction == toucheClavierFlecheDroite:
            self.position.move_right
        else:
            pass
        """
        pass


class Item:

    def __init__(self, name, position=None):
        self.name = name
        self.position = position


class Map:

    def __init__(self):
        self.cells = []
        self.items = []
        self.entrance = None
        self.exit = None
        self.player = None

    def create_map(self):

        with open("map1.txt", "r") as file:
            data = file.readlines()

            for x, line in enumerate(data):

                for y, character in enumerate(line):
                    # set the position with the actual coordonate of the character readed
                    position = Position(x, y)

                    if character in "ES-":  # the cell is a path, entrance or exit
                        cell = Cell(position)

                        if character == "E":
                            self.entrance = cell
                            cell.is_entrance = True
                        elif character == "S":
                            self.exit = cell
                            cell.is_exit = True

                        self.cells.append(cell)

        # create items manually
        self.items.append(Item("seringue"))
        self.items.append(Item("aiguille"))
        self.items.append(Item("produit X"))

    def place_items(self):
        random_positions = self.get_random_pos()

        # set the positions of the items with the positions we get from get_random_pos()
        # and set the attributes item and player of thr corresponding cells
        for x, item in enumerate(self.items):
            position = random_positions[x]
            item.position = position

            for cell in self.cells:

                if cell == item:
                    cell.item = item.name
                    break
                elif cell.position == self.player.position:
                    cell.player = True
                    break
    
    def get_random_pos(self):    
        items_number = len(self.items)
        cells = random.sample(set(self.cells) - {self.entrance, self.exit} , items_number)
        positions = [cell.position for cell in cells]

        return positions

# exception à appeler pour la fin de jeu
# class VictoryException(Exception):
#     pass

# class GameOverException(Exception):
#     pass

def main():
    # game = Map()

    # game.create_map()

    # player = Player(game)

    # game.place_player_and_items()

    pass


if __name__ == "__main__":
    main()
