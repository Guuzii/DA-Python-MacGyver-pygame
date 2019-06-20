# -*- coding: utf-8 -*- -tc- inutile!

# -tc- import pygame ici

import Menu # -tc- éviter les majuscules dans les modules!
import EndView
import Map
import MapView
import Player
import PlayerView
import ItemView
import MyPygame

import pygame

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# PYGAME VERSION

# -tc- une longue fonction comme celle-là peut être découpée en plusieurs
# -tc- utiliser une classe avec plusieurs méthodes peut être intéressant
def game_loop(pygame_object):
    """-tc- ajouter une docstring"""

    run_loop = True
    my_pygame = pygame_object
    game = Map.Map(my_pygame)
    game.create_map("ressources/maps/map1.txt")
    map_view = MapView.MapView(game)
    player = Player.Player(game)
    player_view = PlayerView.PlayerView(player)

    while run_loop:

        my_pygame.screen.blit(map_view.map_render, (0, 0))

        for item in game.items:

            item_view = ItemView.ItemView(item, my_pygame, map_view)
            my_pygame.screen.blit(item_view.item_render,
                                  (item.position.X * 32, item.position.Y * 32))

        my_pygame.screen.blit(player_view.player_render,
                              (player.position.X * 32, player.position.Y * 32))

        for event in pygame.event.get():

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                run_loop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move("move_up")
                elif event.key == pygame.K_DOWN:
                    player.move("move_down")
                elif event.key == pygame.K_LEFT:
                    player.move("move_left")
                elif event.key == pygame.K_RIGHT:
                    player.move("move_right")

        message = player.can_exit()

        if message:
            if message == "victory":
                end_view = EndView.EndView(my_pygame, True)
            else:
                end_view = EndView.EndView(my_pygame, False)

            print(message)

            loop = True

            while loop:

                my_pygame.screen.blit(end_view.end_render, (0, 0))

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        loop = False

                pygame.display.flip()

            run_loop = False

        pygame.display.flip()


def main():
    """-tc- ajouter docstring"""

    run_main_loop = True
    my_pygame = MyPygame.Pygame((480, 480))
    menu = Menu.Menu(my_pygame)

    while run_main_loop:

        my_pygame.screen.blit(menu.menu_render, (0, 0))

        for event in pygame.event.get():

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                run_main_loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_loop(my_pygame)

        pygame.display.flip()


if __name__ == "__main__":
    main()


# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# CONSOLE VERSION

'''def game_loop():

    run_loop = True
    game = Map.Map()
    game.create_map("ressources/maps/map1.txt")
    player = Player.Player(game)
    action: str = ""

    print("\nMacGyver se trouve à l'entrée du labyrinthe en : x={}, y={}".format(player.position.X, player.position.Y))

    while run_loop:

        print("\nObjet(s) présent(s) sur la map : ")
        for item in game.items:
            print("'{}' en position : x={}, y={}".format(item.name, item.position.X, item.position.Y))
        
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
            print("\nPosition de MacGyver : x={} y={}".format(
                player.position.X, player.position.Y))
        else:
            print("\nPosition de MacGyver : x={} y={}".format(
                player.position.X, player.position.Y))

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
            print("\nSaisie incorrect. Merci de saisir un caractére correspondant à une option.")
            continue

if __name__ == "__main__":
    main()'''
