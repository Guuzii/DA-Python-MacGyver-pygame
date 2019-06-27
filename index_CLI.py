"""
    PROJET 3 - DA PYTHON (OpenClassrooms.com)
    Etudiant: Erwan MORIO
    
    The Same game, but in console mode (no pygame interface)

    See index.py
"""

from component import labyrinth, player

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# CONSOLE VERSION

def game_loop():

    run_loop = True
    game = labyrinth.Labyrinth()
    game.create_map("ressources/maps/map1.txt")
    player_ig = player.Player(game)
    action: str = ""

    print("\nMacGyver se trouve à l'entrée du labyrinthe en : x={}, y={}".format(player_ig.position.X, player_ig.position.Y))

    while run_loop:

        print("\nObjet(s) présent(s) sur la map : ")
        for item in game.items:
            print("'{}' en position : x={}, y={}".format(item.name, item.position.X, item.position.Y))
        
        print("\nDans quelle direction voulez vous aller ?")
        action = input("\nHaut (z) \nBas (s) \nGauche (q) \nDroite (d) \n :").casefold()

        moved = None

        if action == "z":
            moved = player_ig.move("move_up")
        elif action == "s":
            moved = player_ig.move("move_down")
        elif action == "q":
            moved = player_ig.move("move_left")
        elif action == "d":
            moved = player_ig.move("move_right")
        else:
            print("\nCaractère saisie non valide !")

        if moved != None and not moved:
            print("Vous ne pouvez pas vous déplacer dans cette direction car il y a un mur")
            print("\nPosition de MacGyver : x={} y={}".format(
                player_ig.position.X, player_ig.position.Y))
        else:
            print("\nPosition de MacGyver : x={} y={}".format(
                player_ig.position.X, player_ig.position.Y))

        message = player_ig.can_exit()

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
            print("\nSaisie incorrect. Merci de saisir un caractére correspondant à une option.")
            continue

if __name__ == "__main__":
    main()