# Bracket Scorer
# By Simon Laurin simonlaurin@yahoo.com
# http://github.com/smnlrn
# Released under a tbd license

import random
import pygame
import sys
from pygame.locals import *

FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 800  # size of window's width in pixels
WINDOWHEIGHT = 480  # size of windows' height in pixels

JVT = .9  # Joystick Value Threshold

#       R    G    B
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

# Player Info Page Variables
letterGap = 50
letterMarginLeft = 500
letterMarginTop = 180
squareSide = 40
squareAlignement = 5

switch = 0
letters = [["A", "B", "C", "D", "E", "F"], ["G", "H", "I", "J", "K", "L"], ["M", "N", "O", "P", "Q", "R"],
           ["S", "T", "U", "V", "W", "X"], ["Y", "Z", "-", ".", "<", ">"], [" ", "&", "!", "?", "BYE", ""]]
Players = ["        "] * 8
xmax = len(letters[0]) - 1

ymax = len(letters) - 1
rectposxmin = letterMarginLeft - squareAlignement
rectposxmax = letterMarginLeft + letterGap * xmax - squareAlignement
rectposymin = letterMarginTop - squareAlignement
rectposymax = letterMarginTop + letterGap * ymax - squareAlignement
rectposxstep = letterGap
rectposystep = letterGap


# Player Name, Score box center coordinates (add approx. 3px to vertical center for uppercase letters)
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


def text_objects(text, font):
    textsurface = font.render(text, True, BLACK)
    return textsurface, textsurface.get_rect()


def text_blit(text, font, clr, center):
    textrender = font.render(text, True, clr)
    return textrender, textrender.get_rect(center=center)


def select_player(event, index):
    if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        index += 1
        if index > 7:
            index = 0
    if event.type == pygame.KEYUP and event.key == pygame.K_UP:
        index -= 1
        if index < 0:
            index = 7
    return index


def letterpicker(event, rectposx, rectposy, x, y):
    if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
        rectposx += rectposxstep
        x += 1
        if rectposx > rectposxmax:
            rectposx = rectposxmin
            x = 0
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
        rectposx -= rectposxstep
        x -= 1
        if rectposx < rectposxmin:
            rectposx = rectposxmax
            x = xmax
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        rectposy += rectposystep
        y += 1
        if rectposy > rectposymax:
            rectposy = rectposymin
            y = 0
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    if event.type == pygame.KEYUP and event.key == pygame.K_UP:
        rectposy -= rectposystep
        y -= 1
        if rectposy < rectposymin:
            rectposy = rectposymax
            y = ymax
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    return rectposx, rectposy, x, y


def init_players():
    fontplayer = pygame.font.Font("OCRAStd.otf", 40)
    rectposx = rectposxmin
    rectposy = rectposymin
    player_index = 0
    player_x = 10
    player_y = 50
    player_vgap = 50
    player_square = 30
    name_x = 40
    name_y = 45
    name_gap = 29
    name_square = 39
    x = 0
    # xmax = len(letters[0]) - 1
    y = 0
    # pygame.draw.rect(DISPLAYSURF, ORANGE, [rectposx, rectposy, squareSide, squareSide], 2)
    initials = [" "] * 8
    ii = 0

    init = True
    player_picker = True
    while init:
        background_image_player = pygame.image.load("TournamentScorerBGPlayer.png").convert()
        DISPLAYSURF.blit(background_image_player, (0, 0))
        if player_picker:
            pygame.draw.rect(DISPLAYSURF, RED, [player_x, player_y + player_vgap * player_index,
                                                player_square, player_square], 2)
        else:
            pygame.draw.rect(DISPLAYSURF, RED, [rectposx, rectposy, 50, 50], 2)
            pygame.draw.rect(DISPLAYSURF, RED, [name_x + ii*name_gap, name_y + player_vgap * player_index,
                                                name_square, name_square], 2)

        # drawletters(DISPLAYSURF, letters)
        # drawnumbers(DISPLAYSURF, numbers)
        DISPLAYSURF.blit(fontplayer.render(Players[0], True, ORANGE), (45, 50))
        DISPLAYSURF.blit(fontplayer.render(Players[1], True, ORANGE), (45, 100))
        DISPLAYSURF.blit(fontplayer.render(Players[2], True, ORANGE), (45, 150))
        DISPLAYSURF.blit(fontplayer.render(Players[3], True, ORANGE), (45, 200))
        DISPLAYSURF.blit(fontplayer.render(Players[4], True, ORANGE), (45, 250))
        DISPLAYSURF.blit(fontplayer.render(Players[5], True, ORANGE), (45, 300))
        DISPLAYSURF.blit(fontplayer.render(Players[6], True, ORANGE), (45, 350))
        DISPLAYSURF.blit(fontplayer.render(Players[7], True, ORANGE), (45, 400))
        # DISPLAYSURF.blit(fontbig.render(initials[1], True, ORANGE), (230, 300))
        # DISPLAYSURF.blit(fontbig.render(initials[2], True, ORANGE), (260, 300))
        # DISPLAYSURF.blit(txt_surf, txt_rect)

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                init = False
            if player_picker:
                if event.type == pygame.KEYUP and event.key in [pygame.K_UP, pygame.K_DOWN]:
                    player_index = select_player(event, player_index)
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    player_picker = False
                    initials = list(Players[player_index])
                    ii = 0
            else:
                if event.type == pygame.KEYUP and \
                        event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    rectposx, rectposy, x, y = letterpicker(event, rectposx, rectposy, x, y)
                    print(event)
                    print(rectposx, rectposy, x, y)
                if event.type == pygame.KEYUP and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    print("Initials: ", "".join(initials))
                    Players[player_index] = "".join(initials)
                    print("Player:", Players[player_index])
                    player_picker = True
                    if player_index < 7:
                        player_index += 1
                    else:
                        player_index = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # print(letters[y][x])
                    initials[ii] = letters[y][x]
                    Players[player_index] = "".join(initials)
                    ii += 1
                    if ii > 7:
                        ii = 0

        pygame.display.update()

    # Get players name

    # Random seed / no seed
    rnd = 0
    # Put names on Display

    # Return seeded players 1v8 vs 4v5 - 3v6 vs 2v7
    # plist = ["PLAYER 1", "PLAYER 8", "PLAYER 4", "PLAYER 5", "PLAYER 3", "PLAYER 6", "PLAYER 2", "PLAYER 7"]
    plist = [str(Players[0]).strip(), str(Players[7]).strip(), str(Players[3]).strip(), str(Players[4]).strip(),
             str(Players[2]).strip(), str(Players[5]).strip(), str(Players[1]).strip(), str(Players[6]).strip()]
    print("Original list : ",  plist)
    if rnd == 1:
        random.shuffle(plist)  # shuffle method
        print("List after first shuffle  : ", plist)
    wlist = [""] * 6
    plist.extend(wlist)
    setlist = [3] * 8 + [5] * 4 + [7] * 2
    return plist, setlist


def init_sets():
    # this will eventually use the Argonne Pool League System...
    return 3


def init_bracket(screen):
    background_image = pygame.image.load("TournamentScorerBG.png").convert()
    screen.blit(background_image, (0, 0))


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    # DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # For screen on Raspberry Pi
    pygame.display.set_caption('Simple Elimination Tournament')

    player_list, sets_list = init_players()
    print(player_list)
    winner_list = [False] * 14
    # sysFont did not work on my MBP for some reason...
    font_main_name = pygame.font.Font('freesansbold.ttf', 48)
    font_main_score = pygame.font.Font("freesansbold.ttf", 72)
    font_bracket = pygame.font.Font("freesansbold.ttf", 18)

    correction = False
    currentgame = 1
    scores = [0] * 14

    while True:  # main game loop

        init_bracket(DISPLAYSURF)

        # DISPLAY ALL TOURNAMENT ELEMENTS  (the * splits the returned list into arguments)
        # PLAYER NAMES - BRACKETS
        DISPLAYSURF.blit(*text_blit(player_list[0], font_bracket, WHITE, G1P1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[1], font_bracket, WHITE, G1P2CXY))
        DISPLAYSURF.blit(*text_blit(player_list[2], font_bracket, WHITE, G2P1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[3], font_bracket, WHITE, G2P2CXY))
        DISPLAYSURF.blit(*text_blit(player_list[4], font_bracket, WHITE, G3P1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[5], font_bracket, WHITE, G3P2CXY))
        DISPLAYSURF.blit(*text_blit(player_list[6], font_bracket, WHITE, G4P1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[7], font_bracket, WHITE, G4P2CXY))
        DISPLAYSURF.blit(*text_blit(player_list[8], font_bracket, WHITE, G5P1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[9], font_bracket, WHITE, G5P2CXY))
        DISPLAYSURF.blit(*text_blit(player_list[10], font_bracket, WHITE, G6P1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[11], font_bracket, WHITE, G6P2CXY))
        DISPLAYSURF.blit(*text_blit(player_list[12], font_bracket, WHITE, G7P1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[13], font_bracket, WHITE, G7P2CXY))
        # PLAYER SCORE - BRACKETS
        DISPLAYSURF.blit(*text_blit(str(scores[0]), font_bracket, RED, G1S1CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[1]), font_bracket, RED, G1S2CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[2]), font_bracket, RED, G2S1CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[3]), font_bracket, RED, G2S2CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[4]), font_bracket, RED, G3S1CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[5]), font_bracket, RED, G3S2CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[6]), font_bracket, RED, G4S1CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[7]), font_bracket, RED, G4S2CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[8]), font_bracket, RED, G5S1CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[9]), font_bracket, RED, G5S2CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[10]), font_bracket, RED, G6S1CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[11]), font_bracket, RED, G6S2CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[12]), font_bracket, RED, G7S1CXY))
        DISPLAYSURF.blit(*text_blit(str(scores[13]), font_bracket, RED, G7S2CXY))
        # CURRENT GAME
        DISPLAYSURF.blit(*text_blit(player_list[currentgame*2-2], font_main_name, WHITE, MGP1CXY))
        DISPLAYSURF.blit(*text_blit(player_list[currentgame*2-1], font_main_name, WHITE, MGP2CXY))
        if correction:
            DISPLAYSURF.blit(*text_blit(str(scores[currentgame*2-2]), font_main_score, RED, MGS1CXY))
            DISPLAYSURF.blit(*text_blit(str(scores[currentgame*2-1]), font_main_score, RED, MGS2CXY))
        else:
            DISPLAYSURF.blit(*text_blit(str(scores[currentgame*2-2]), font_main_score, WHITE, MGS1CXY))
            DISPLAYSURF.blit(*text_blit(str(scores[currentgame*2-1]), font_main_score, WHITE, MGS2CXY))
        DISPLAYSURF.blit(*text_blit(str(sets_list[currentgame*2-2]), font_bracket, RED, MGSET1CXY))
        DISPLAYSURF.blit(*text_blit(str(sets_list[currentgame*2-1]), font_bracket, RED, MGSET2CXY))
        # GAME SELECTION RECTANGLE
        pygame.draw.rect(DISPLAYSURF, RED, (360, 135 + 24 * currentgame, 85, 24), 1)

        # TOURNAMENT LOGIC
        # Since all elements are refreshed at every tick, the tournament logic only updates variables
        #   currentgame : game number to be displayed in the main bloc
        #   player_list: for seeded players and winners
        #   scores: score list as they are entered
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or \
                    (event.type == pygame.JOYBUTTONDOWN and joystick.get_button(9)):  # START
                pygame.quit()
                sys.exit()

            if (event.type == KEYUP and event.key == K_DOWN) or \
                    (event.type == pygame.JOYAXISMOTION and joystick.get_axis(1) > JVT):  # DOWN
                if currentgame == 7:
                    currentgame = 1
                else:
                    currentgame += 1

            if (event.type == KEYUP and event.key == K_UP) or \
                    (event.type == pygame.JOYAXISMOTION and joystick.get_axis(1) < -JVT):  # UP
                if currentgame == 1:
                    currentgame = 7
                else:
                    currentgame -= 1

            if (event.type == KEYUP and event.key == K_x) or \
                    (event.type == pygame.JOYBUTTONDOWN and joystick.get_button(8)):  # SELECT
                if correction:
                    correction = False
                else:
                    correction = True
            if (event.type == KEYUP and (event.key == K_LEFT or event.key == K_RIGHT)) or \
                    (event.type == pygame.JOYAXISMOTION and
                        (joystick.get_axis(0) < -JVT or joystick.get_axis(0) > JVT)):  # LEFT & RIGHT
                if (event.type == KEYUP and event.key == K_LEFT) or \
                        (event.type == pygame.JOYAXISMOTION and joystick.get_axis(0) < -JVT):  # LEFT
                    if correction:
                        scores[currentgame*2-2] -= 1
                        correction = False
                    else:
                        scores[currentgame * 2 - 2] += 1

                if (event.type == KEYUP and event.key == K_RIGHT) or \
                        (event.type == pygame.JOYAXISMOTION and joystick.get_axis(0) > JVT):  # RIGHT
                    if correction:
                        scores[currentgame*2-1] -= 1
                        correction = False
                    else:
                        scores[currentgame*2-1] += 1

                # CHECK WINNER
                if sets_list[currentgame*2-2] == scores[currentgame*2-2]:
                    winner_list[currentgame*2-2] = True
                    winner_list[currentgame*2-1] = False
                    print(player_list[currentgame*2-2], ' wins')
                    if currentgame != 7:
                        player_list[currentgame+7] = player_list[currentgame*2-2]
                    # else:
                        # display_winner()

                elif sets_list[currentgame*2-1] == scores[currentgame*2-1]:
                    winner_list[currentgame*2-2] = False
                    winner_list[currentgame*2-1] = True
                    print(player_list[currentgame*2-1], ' wins')
                    if currentgame != 7:
                        player_list[currentgame+7] = player_list[currentgame*2-1]
                    # else:
                        # display_winner()
                else:
                    winner_list[currentgame * 2 - 2] = False
                    winner_list[currentgame * 2 - 1] = False
                    if currentgame != 7:
                        player_list[currentgame+7] = ""

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
