import random
import pygame
from pygame.locals import *

pygame.init()
    
fenetre = pygame.display.set_mode((640, 480))


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
        return Position(self.X, self.Y - 1)

    def move_bottom(self):        
        return Position(self.X, self.Y + 1)

    def move_left(self):        
        return Position(self.X - 1, self.Y)

    def move_right(self):        
        return Position(self.X + 1, self.Y)


class Cell:

    def __init__(self, position, is_entrance=False, is_exit=False):
        self.position = position
        self.item = None
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
        self.items = []
        self.map = map
        self.map.player = self    

    def move(self, keyboardKey):

        new_position = getattr(self.position, keyboardKey)()
        new_cell = Cell(new_position)

        if new_cell in self.map.cells:
            self.position = new_position
            self.pick_item(new_cell)
            return True
        else:
            return False

    def pick_item(self, test_cell):

        for cell in self.map.cells:
            if cell == test_cell and cell.position == self.position and cell.item != None:
                print("Vous trouvez un objet au sol : {}. \nVous le prenez.".format(cell.item.name))
                self.items.append(cell.item)
                cell.item = None

                print("\nVous avez maintenant {} objet(s) en votre possesion :".format(len(self.items)))
                for item in self.items:
                    print(item.name)

                break

    def can_exit(self):
        if self.position == self.map.exit.position:
            if len(self.items) == len(self.map.items):                
                return "Vous arrivez à vous échapper. Victoire !"
            else:                
                return "Défaite, il vous manquais {} items à récuperer pour pouvoir vous échapper".format(len(self.map.items) - len(self.items))
        else:
            return False
            

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

            for y, line in enumerate(data):

                for x, character in enumerate(line.strip()):
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
        # and set the attributes item and player of the corresponding cells
        for x, item in enumerate(self.items):
            position = random_positions[x]
            item.position = position

            for cell in self.cells:

                if cell.position == item.position:
                    cell.item = item
                    break

        for cell in self.cells:
            if cell.item != None:
                print(cell.item.name)
                print("pos cell x={}, y ={}".format(cell.position.X, cell.position.Y))

    def get_random_pos(self):
        items_number = len(self.items)
        cells = random.sample(
            set(self.cells) - {self.entrance, self.exit}, items_number)
        positions = [cell.position for cell in cells]

        return positions  


# exception à appeler pour la fin de jeu
# class VictoryException(Exception):
#     pass

# class GameOverException(Exception):
#     pass

def game_loop():    

    run_loop = True
    game = Map()
    game.create_map()
    player = Player(game)
    game.place_items()
    action: str = ""

    print(game.exit.position.X, game.exit.position.Y)
    print("\nMacGyver se trouve à l'entrée du labyrinthe en : x={}, y={}".format(
        player.position.X, player.position.Y))

    while run_loop:

        print("\nDans quelle direction voulez vous aller ?")
        action = input("\nHaut (z) \nBas (s) \nGauche (q) \nDroite (d) \n :").casefold()

        moved = None

        if action == "z":
            moved = player.move("move_top")
        elif action == "s":
            moved = player.move("move_bottom")
        elif action == "q":
            moved = player.move("move_left")
        elif action == "d":
            moved = player.move("move_right")
        else:
            print("\nCaractère saisie non valide !")
        
        if moved != None and not moved:
            print("Vous ne pouvez pas vous déplacer dans cette direction car il y a un mur")
            print("\nPosition de MacGyver : x={} y={}".format(player.position.X, player.position.Y)) 
        else:
            print("\nPosition de MacGyver : x={} y={}".format(player.position.X, player.position.Y))
                
        message = player.can_exit()

        if message:
            print(message)
            run_loop = False

def main():

    run_main_loop = True    

    while run_main_loop:
        print("\nMENU PRINCIPAL \n\nVeuillez choisir une option \n")
        start_game: str = input("Saisissez (n) pour une nouvelle partie ou (q) pour quitter le programme : ").casefold()

        if start_game == "n" or start_game == "q":
            if start_game == "n":
                print("\nlancement nouvelle partie")
                game_loop()
            else:
                run_main_loop = False
        else:
            print(
                "\nSaisie incorrect. Merci de saisir un caractére correspondant à une option.")
            continue


if __name__ == "__main__":
    main()
