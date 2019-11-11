# Bracket Scorer
# By Simon Laurin simonlaurin@yahoo.com
# http://
# Released under a tbd license

import random
import pygame
import sys
from pygame.locals import *

FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 800  # size of window's width in pixels
WINDOWHEIGHT = 480  # size of windows' height in pixels

#            R    G    B
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255, 5)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Player box center coordinates (add 3px to vertical center for uppercase letters)
G1P1CXY = (95, 23)
G1P2CXY = (290, 23)
G1S1CXY = (173, 23)
G1S2CXY = (217, 23)

G2P1CXY = (510, 23)
G2P2CXY = (705, 23)
G2S1CXY = (588, 23)
G2S2CXY = (632, 23)

G3P1CXY = (95, 463)
G3P2CXY = (290, 463)
G3S1CXY = (173, 463)
G3S2CXY = (217, 463)

G4P1CXY = (510, 463)
G4P2CXY = (705, 463)
G4S1CXY = (588, 463)
G4S2CXY = (632, 463)

G5P1CXY = (192, 88)
G5P2CXY = (608, 88)
G5S1CXY = (270, 88)
G5S2CXY = (535, 88)

G6P1CXY = (192, 397)
G6P2CXY = (608, 397)
G6S1CXY = (270, 397)
G6S2CXY = (535, 397)

G7P1CXY = (400, 123)
G7P2CXY = (400, 363)
G7S1CXY = (478, 123)
G7S2CXY = (478, 363)

MGP1CXY = (192, 190)
MGP2CXY = (607, 190)
MGS1CXY = (300, 275)
MGS2CXY = (505, 275)
MGSET1CXY = (340, 235)
MGSET2CXY = (465, 235)


def init_players():
    # Get players name

    # Random seed / no seed
    rnd = 0
    # Put names on Display

    # Return seeded players 1v8 vs 4v5 - 3v6 vs 2v7
    plist = ["PLAYER 1", "PLAYER 8", "PLAYER 4", "PLAYER 5", "PLAYER 3", "PLAYER 6", "PLAYER 2", "PLAYER 7"]
    print("Original list : ",  plist)
    if rnd == 1:
        random.shuffle(plist)  # shuffle method
        print("List after first shuffle  : ", plist)
    wlist = [""] * 6
    plist.extend(wlist)
    return plist, [3] * 14


def init_sets():
    # this will eventually use the Argonne Pool League System...
    return 3


def init_bracket(screen):
    # screen.fill(GRAY)
    # Initialize the joysticks
    pygame.joystick.init()

    background_image = pygame.image.load("TournamentScorerBG.png").convert()
    screen.blit(background_image, (0, 0))
    # player_box = pygame.image.load("PlayerBox.png").convert()


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Simple Elimination Tournament')

    player_list, sets_list = init_players()
    winner_list = [False] * 14

    font_main_name = pygame.font.SysFont("Prestij Demo", 48, bold=True)
    font_mains_score = pygame.font.SysFont("Prestij Demo", 72, bold=True)
    font_bracket = pygame.font.SysFont("Prestij Demo", 18, bold=True)
    text_player1 = font_bracket.render(player_list[0], True, WHITE)
    text_player2 = font_bracket.render(player_list[1], True, WHITE)
    text_player3 = font_bracket.render(player_list[2], True, WHITE)
    text_player4 = font_bracket.render(player_list[3], True, WHITE)
    text_player5 = font_bracket.render(player_list[4], True, WHITE)
    text_player6 = font_bracket.render(player_list[5], True, WHITE)
    text_player7 = font_bracket.render(player_list[6], True, WHITE)
    text_player8 = font_bracket.render(player_list[7], True, WHITE)

    # rect_winner1 = text_player1.get_rect(center=G5P1CXY)
    # rect_winner2 = text_player3.get_rect(center=G5P2CXY)
    # rect_winner3 = text_player1.get_rect(center=G6P1CXY)
    # rect_winner4 = text_player1.get_rect(center=G6P2CXY)
    # rect_winner5 = text_player1.get_rect(center=G7P1CXY)
    # rect_winner6 = text_player1.get_rect(center=G7P2CXY)
    #
    # DISPLAYSURF.blit(text_player1, rect_winner1)
    # DISPLAYSURF.blit(text_player3, rect_winner2)
    # DISPLAYSURF.blit(text_player5, rect_winner3)
    # DISPLAYSURF.blit(text_player7, rect_winner4)
    # DISPLAYSURF.blit(text_player1, rect_winner5)
    # DISPLAYSURF.blit(text_player7, rect_winner6)

    correction = False
    currentgame = 1
    scores = [0] * 14

    while True:  # main game loop

        init_bracket(DISPLAYSURF)

        DISPLAYSURF.blit(text_player1, text_player1.get_rect(center=G1P1CXY))
        DISPLAYSURF.blit(text_player2, text_player2.get_rect(center=G1P2CXY))
        DISPLAYSURF.blit(text_player3, text_player3.get_rect(center=G2P1CXY))
        DISPLAYSURF.blit(text_player4, text_player4.get_rect(center=G2P2CXY))
        DISPLAYSURF.blit(text_player5, text_player5.get_rect(center=G3P1CXY))
        DISPLAYSURF.blit(text_player6, text_player6.get_rect(center=G3P2CXY))
        DISPLAYSURF.blit(text_player7, text_player7.get_rect(center=G4P1CXY))
        DISPLAYSURF.blit(text_player8, text_player8.get_rect(center=G4P2CXY))
        DISPLAYSURF.blit(font_bracket.render(player_list[8], True, WHITE),
                         font_bracket.render(player_list[8], True, WHITE).get_rect(center=G5P1CXY))
        DISPLAYSURF.blit(font_bracket.render(player_list[9], True, WHITE),
                         font_bracket.render(player_list[9], True, WHITE).get_rect(center=G5P2CXY))
        DISPLAYSURF.blit(font_bracket.render(player_list[10], True, WHITE),
                         font_bracket.render(player_list[10], True, WHITE).get_rect(center=G6P1CXY))
        DISPLAYSURF.blit(font_bracket.render(player_list[11], True, WHITE),
                         font_bracket.render(player_list[11], True, WHITE).get_rect(center=G6P2CXY))
        DISPLAYSURF.blit(font_bracket.render(player_list[12], True, WHITE),
                         font_bracket.render(player_list[12], True, WHITE).get_rect(center=G7P1CXY))
        DISPLAYSURF.blit(font_bracket.render(player_list[13], True, WHITE),
                         font_bracket.render(player_list[13], True, WHITE).get_rect(center=G7P2CXY))

        pygame.draw.rect(DISPLAYSURF, RED, (360, 135 + 24 * currentgame, 85, 24), 1)

        # Current Game Display
        DISPLAYSURF.blit(font_main_name.render(player_list[currentgame*2-2], True, WHITE),
                         font_main_name.render(player_list[currentgame*2-2], True, WHITE).get_rect(center=MGP1CXY))
        DISPLAYSURF.blit(font_main_name.render(player_list[currentgame*2-1], True, WHITE),
                         font_main_name.render(player_list[currentgame*2-1], True, WHITE).get_rect(center=MGP2CXY))
        if correction:
            DISPLAYSURF.blit(font_mains_score.render(str(scores[currentgame*2-2]), True, RED),
                             font_mains_score.render(str(scores[currentgame*2-2]), True, RED).get_rect(center=MGS1CXY))
            DISPLAYSURF.blit(font_mains_score.render(str(scores[currentgame*2-1]), True, RED),
                             font_mains_score.render(str(scores[currentgame*2-1]), True, RED).get_rect(center=MGS2CXY))
        else:
            DISPLAYSURF.blit(font_mains_score.render(str(scores[currentgame*2-2]), True, WHITE),
                             font_mains_score.render(str(scores[currentgame*2-2]), True, WHITE).get_rect(center=MGS1CXY))
            DISPLAYSURF.blit(font_mains_score.render(str(scores[currentgame*2-1]), True, WHITE),
                             font_mains_score.render(str(scores[currentgame*2-1]), True, WHITE).get_rect(center=MGS2CXY))

        DISPLAYSURF.blit(font_bracket.render(str(sets_list[currentgame*2-2]), True, RED),
                         font_bracket.render(str(sets_list[currentgame*2-2]), True, RED).get_rect(center=MGSET1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(sets_list[currentgame*2-1]), True, RED),
                         font_bracket.render(str(sets_list[currentgame*2-1]), True, RED).get_rect(center=MGSET2CXY))

        # Tournament scores
        DISPLAYSURF.blit(font_bracket.render(str(scores[0]), True, RED),
                         font_bracket.render(str(scores[0]), True, RED).get_rect(center=G1S1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[1]), True, RED),
                         font_bracket.render(str(scores[1]), True, RED).get_rect(center=G1S2CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[2]), True, RED),
                         font_bracket.render(str(scores[2]), True, RED).get_rect(center=G2S1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[3]), True, RED),
                         font_bracket.render(str(scores[3]), True, RED).get_rect(center=G2S2CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[4]), True, RED),
                         font_bracket.render(str(scores[4]), True, RED).get_rect(center=G3S1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[5]), True, RED),
                         font_bracket.render(str(scores[5]), True, RED).get_rect(center=G3S2CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[6]), True, RED),
                         font_bracket.render(str(scores[6]), True, RED).get_rect(center=G4S1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[7]), True, RED),
                         font_bracket.render(str(scores[7]), True, RED).get_rect(center=G4S2CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[8]), True, RED),
                         font_bracket.render(str(scores[8]), True, RED).get_rect(center=G5S1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[9]), True, RED),
                         font_bracket.render(str(scores[9]), True, RED).get_rect(center=G5S2CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[10]), True, RED),
                         font_bracket.render(str(scores[10]), True, RED).get_rect(center=G6S1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[11]), True, RED),
                         font_bracket.render(str(scores[11]), True, RED).get_rect(center=G6S2CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[12]), True, RED),
                         font_bracket.render(str(scores[12]), True, RED).get_rect(center=G7S1CXY))
        DISPLAYSURF.blit(font_bracket.render(str(scores[13]), True, RED),
                         font_bracket.render(str(scores[13]), True, RED).get_rect(center=G7S2CXY))

        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYUP and event.key == K_DOWN:
                if currentgame == 7:
                    currentgame = 1
                else:
                    currentgame += 1
                pygame.draw.rect(DISPLAYSURF, RED, (360, 135 + 24*currentgame, 85, 24), 1)

            if event.type == KEYUP and event.key == K_UP:
                if currentgame == 1:
                    currentgame = 7
                else:
                    currentgame -= 1
                pygame.draw.rect(DISPLAYSURF, BLUE, (360, 135 + 24*currentgame, 85, 24), 1)

            if event.type == KEYUP and event.key == K_x:
                if correction:
                    correction = False
                else:
                    correction = True

            if event.type == KEYUP and event.key == K_LEFT:
                if correction:
                    scores[currentgame*2-2] -= 1
                    correction = False
                else:
                    scores[currentgame * 2 - 2] += 1

            if event.type == KEYUP and event.key == K_RIGHT:
                if correction:
                    scores[currentgame*2-1] -= 1
                    correction = False
                else:
                    scores[currentgame*2-1] += 1

            # CHECK WINNER TODO: Put inside the left-right keyup if statement and trap final winner index
            if sets_list[currentgame*2-2] == scores[currentgame*2-2]:
                winner_list[currentgame*2-2] = True
                winner_list[currentgame*2-1] = False
                print(player_list[currentgame*2-2], ' wins')
                player_list[currentgame+7] = player_list[currentgame*2-2]

            elif sets_list[currentgame*2-1] == scores[currentgame*2-1]:
                winner_list[currentgame*2-2] = False
                winner_list[currentgame*2-1] = True
                print(player_list[currentgame*2-1], ' wins')
                player_list[currentgame+7] = player_list[currentgame*2-1]

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
