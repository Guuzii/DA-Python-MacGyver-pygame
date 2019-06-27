"""
    PROJET 3 - DA PYTHON (OpenClassrooms.com)
    Etudiant: Erwan MORIO
    
    Pygame minigame where the player have to help the famous character MacGyver to get out of the labyrinth !

    To do so you'll have to make your way through the labyrinth to pick up differents items to be able to escape.

    Here is the controls:
      - Arrow Keys:
        # Up : MacGyver is trying to move up
        # Down : MacGyver is trying to move down
        # Left : MacGyver is trying to move left
        # Right : MacGyver is trying to move right
      
      - Escape : exit the game and return to menu OR close the application

    Have fun !
"""

import pygame

from component import labyrinth, player, myPygame
from views import endView, menu, labyrinthView, playerView, itemView, interface

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


# --------------------------------------------------------------------
# --------------------------------------------------------------------
# PYGAME VERSION

def game_loop(pygame_object):

    # Initialisation of the different components of the game
    run_loop = True
    my_pygame = pygame_object
    game = labyrinth.Labyrinth(my_pygame)
    game.create_map("ressources/maps/map1.txt")
    labyrinth_view = labyrinthView.LabyrinthView(game)
    player_ig = player.Player(game)
    player_view = playerView.PlayerView(player_ig)      

    while run_loop:

        # Rendering the different component of the game by "blitting" on the screen
        my_pygame.screen.blit(labyrinth_view.labyrinth_render, (0, 0))

        for item in game.items:

            item_view = itemView.ItemView(item, my_pygame, labyrinth_view)
            my_pygame.screen.blit(item_view.item_render,
                                  (item.position.X * 32, item.position.Y * 32))

        interface_view = interface.Interface(game)      

        for i, item in enumerate(player_ig.items):

            interface_item = itemView.ItemView(item, my_pygame, labyrinth_view, True)
            interface_view.interface_render.blit(interface_item.item_render, ((i+1) * 36, 10))
        
        my_pygame.screen.blit(interface_view.interface_render, (0, 480))

        my_pygame.screen.blit(player_view.player_render,
                              (player_ig.position.X * 32, player_ig.position.Y * 32))

        # Listening for events on the pygame instance and reacting on some of them
        for event in pygame.event.get():

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                run_loop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_ig.move("move_up")
                elif event.key == pygame.K_DOWN:
                    player_ig.move("move_down")
                elif event.key == pygame.K_LEFT:
                    player_ig.move("move_left")
                elif event.key == pygame.K_RIGHT:
                    player_ig.move("move_right")

        # Calling a method to check if the end game conditions are present
        message = player_ig.can_exit()

        if message:
            if message == "victory":
                end_view = endView.EndView(my_pygame, True)
            else:
                end_view = endView.EndView(my_pygame, False)

            loop = True

            # Display of the End View
            while loop:

                my_pygame.screen.blit(end_view.end_render, (0, 0))

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        loop = False

                pygame.display.flip()

            run_loop = False

        pygame.display.flip()


def main():

    run_main_loop = True
    my_pygame = myPygame.Pygame((480, 530))
    game_menu = menu.Menu(my_pygame)

    while run_main_loop:

        # Rendering the menu on the screen
        my_pygame.screen.blit(game_menu.menu_render, (0, 0))

        # Listening for events on the pygame instance and reacting on some of them
        for event in pygame.event.get():
            
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                run_main_loop = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_loop(my_pygame)

        pygame.display.flip()


if __name__ == "__main__":
    main()