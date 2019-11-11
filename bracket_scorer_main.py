# Bracket Scorer
# By Simon Laurin simonlaurin@yahoo.com
# http://
# Released under a tbd license

import random, pygame, sys
import pandas as pd
from pygame.locals import *

FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 800  # size of window's width in pixels
WINDOWHEIGHT = 480  # size of windows' height in pixels

#REVEALSPEED = 8  # speed boxes' sliding reveals and covers
#BOXSIZE = 40  # size of box height & width in pixels
#GAPSIZE = 10  # size of gap between boxes in pixels
#BOARDWIDTH = 10  # number of columns of icons
#BOARDHEIGHT = 7  # number of rows of icons
#assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
#XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
#YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
LEFTMARGIN = 20
RIGHTMARGIN = 20
TOPMARGIN = 10

PLAYERBOXHeight = 30 #
PLAYERBOXLength = 150
PLAYERBOXGap = 10


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

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
PLAYERBOXColor = BLUE
HIGHLIGHTCOLOR = BLUE

# Player box center coordinates (add 3px to vertical center for uppercase letters)
G1P1cxy = (95, 23)
G1P2cxy = (290, 23)
G1S1cxy = (173, 23)
G1S2cxy = (217, 23)

G2P1cxy = (510, 23)
G2P2cxy = (705, 23)
G2S1cxy = (588, 23)
G2S2cxy = (632, 23)

G3P1cxy = (95, 463)
G3P2cxy = (290, 463)
G3S1cxy = (173, 463)
G3S2cxy = (217, 463)

G4P1cxy = (510, 463)
G4P2cxy = (705, 463)
G4S1cxy = (588, 463)
G4S2cxy = (632, 463)

G5P1cxy = (192, 88)
G5P2cxy = (608, 88)
G5S1cxy = (270, 88)
G5S2cxy = (535, 88)

G6P1cxy = (192, 397)
G6P2cxy = (608, 397)
G6S1cxy = (270, 397)
G6S2cxy = (535, 397)

G7P1cxy = (400, 123)
G7P2cxy = (400, 363)
G7S1cxy = (478, 123)
G7S2cxy = (478, 363)

MGP1cxy = (192, 185)
MGP2cxy = (607, 185)
MGS1cxy = (300, 275)
MGS2cxy = (505, 275)

def initPlayers(fieldSize):
    # Get players name

    # Random seed / no seed
    rnd = 0
    # Put names on Display

    # Return seeded players ["Player 1", "Player 8", "Player 4", "Player 5", "Player 3", "Player 6", "Player 2", "Player 7"]
    plist = ["PLAYER 1", "PLAYER 8", "PLAYER 4", "PLAYER 5", "PLAYER 3", "PLAYER 6", "PLAYER 2", "PLAYER 7"]
    print ("Original list : ",  plist)
    if rnd == 1:
        random.shuffle(plist)  # shuffle method
        print("List after first shuffle  : ", plist)
    wlist = ["WINNER G1", "WINNER G2", "WINNER G3", "WINNER G4", "WINNER G5", "WINNER G6"]
    plist.extend(wlist)
    return plist

def initBracket(screen):
    #screen.fill(GRAY)
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

    playerList = initPlayers(8)


    fontMainName = pygame.font.SysFont("Prestij Demo", 48, bold=True)
    fontMainScore = pygame.font.SysFont("Prestij Demo", 72, bold=True)
    fontBracket = pygame.font.SysFont("Prestij Demo", 18, bold=True)
    textPlayer1 = fontBracket.render(playerList[0], True, WHITE)
    textPlayer2 = fontBracket.render(playerList[1], True, WHITE)
    textPlayer3 = fontBracket.render(playerList[2], True, WHITE)
    textPlayer4 = fontBracket.render(playerList[3], True, WHITE)
    textPlayer5 = fontBracket.render(playerList[4], True, WHITE)
    textPlayer6 = fontBracket.render(playerList[5], True, WHITE)
    textPlayer7 = fontBracket.render(playerList[6], True, WHITE)
    textPlayer8 = fontBracket.render(playerList[7], True, WHITE)

    rectWinner1 = textPlayer1.get_rect(center=G5P1cxy)
    rectWinner2 = textPlayer3.get_rect(center=G5P2cxy)
    rectWinner3 = textPlayer1.get_rect(center=G6P1cxy)
    rectWinner4 = textPlayer1.get_rect(center=G6P2cxy)
    rectWinner5 = textPlayer1.get_rect(center=G7P1cxy)
    rectWinner6 = textPlayer1.get_rect(center=G7P2cxy)


    DISPLAYSURF.blit(textPlayer1, rectWinner1)
    DISPLAYSURF.blit(textPlayer3, rectWinner2)
    DISPLAYSURF.blit(textPlayer5, rectWinner3)
    DISPLAYSURF.blit(textPlayer7, rectWinner4)
    DISPLAYSURF.blit(textPlayer1, rectWinner5)
    DISPLAYSURF.blit(textPlayer7, rectWinner6)

    currentgame = 1
    scores = [0] * 14


    while True:  # main game loop

        initBracket(DISPLAYSURF)

        DISPLAYSURF.blit(textPlayer1, textPlayer1.get_rect(center=G1P1cxy))
        DISPLAYSURF.blit(textPlayer2, textPlayer2.get_rect(center=G1P2cxy))
        DISPLAYSURF.blit(textPlayer3, textPlayer3.get_rect(center=G2P1cxy))
        DISPLAYSURF.blit(textPlayer4, textPlayer4.get_rect(center=G2P2cxy))
        DISPLAYSURF.blit(textPlayer5, textPlayer5.get_rect(center=G3P1cxy))
        DISPLAYSURF.blit(textPlayer6, textPlayer6.get_rect(center=G3P2cxy))
        DISPLAYSURF.blit(textPlayer7, textPlayer7.get_rect(center=G4P1cxy))
        DISPLAYSURF.blit(textPlayer8, textPlayer8.get_rect(center=G4P2cxy))

        pygame.draw.rect(DISPLAYSURF, RED, (360, 135 + 24 * currentgame, 85, 24), 1)

        # Current Game Display
        DISPLAYSURF.blit(fontMainName.render(playerList[currentgame*2-2], True, WHITE),
                         fontMainName.render(playerList[currentgame*2-2], True, WHITE).get_rect(center=MGP1cxy))
        DISPLAYSURF.blit(fontMainName.render(playerList[currentgame*2-1], True, WHITE),
                         fontMainName.render(playerList[currentgame*2-1], True, WHITE).get_rect(center=MGP2cxy))
        DISPLAYSURF.blit(fontMainScore.render(str(scores[currentgame*2-2]), True, WHITE),
                         fontMainScore.render(str(scores[currentgame*2-2]), True, WHITE).get_rect(center=MGS1cxy))
        DISPLAYSURF.blit(fontMainScore.render(str(scores[currentgame*2-1]), True, WHITE),
                         fontMainScore.render(str(scores[currentgame*2-1]), True, WHITE).get_rect(center=MGS2cxy))

        # Tournament scores
        DISPLAYSURF.blit(fontBracket.render(str(scores[0]), True, RED),
                         fontBracket.render(str(scores[0]), True, RED).get_rect(center=G1S1cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[1]), True, RED),
                         fontBracket.render(str(scores[1]), True, RED).get_rect(center=G1S2cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[2]), True, RED),
                         fontBracket.render(str(scores[2]), True, RED).get_rect(center=G2S1cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[3]), True, RED),
                         fontBracket.render(str(scores[3]), True, RED).get_rect(center=G2S2cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[4]), True, RED),
                         fontBracket.render(str(scores[4]), True, RED).get_rect(center=G3S1cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[5]), True, RED),
                         fontBracket.render(str(scores[5]), True, RED).get_rect(center=G3S2cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[6]), True, RED),
                         fontBracket.render(str(scores[6]), True, RED).get_rect(center=G4S1cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[7]), True, RED),
                         fontBracket.render(str(scores[7]), True, RED).get_rect(center=G4S2cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[8]), True, RED),
                         fontBracket.render(str(scores[8]), True, RED).get_rect(center=G5S1cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[9]), True, RED),
                         fontBracket.render(str(scores[9]), True, RED).get_rect(center=G5S2cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[10]), True, RED),
                         fontBracket.render(str(scores[10]), True, RED).get_rect(center=G6S1cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[11]), True, RED),
                         fontBracket.render(str(scores[11]), True, RED).get_rect(center=G6S2cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[12]), True, RED),
                         fontBracket.render(str(scores[12]), True, RED).get_rect(center=G7S1cxy))
        DISPLAYSURF.blit(fontBracket.render(str(scores[13]), True, RED),
                         fontBracket.render(str(scores[13]), True, RED).get_rect(center=G7S2cxy))


        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # elif event.type == MOUSEMOTION:
            #     # mousex, mousey = event.pos
            # elif event.type == MOUSEBUTTONUP:
            #     # mousex, mousey = event.pos
            #     # mouseClicked = True


            if event.type == KEYUP and event.key == K_DOWN:
                # pygame.draw.rect(DISPLAYSURF, BLACK, (360, 135 + 24 * currentgame, 85, 24), 1)
                if currentgame == 7:
                    currentgame = 1
                else:
                    currentgame += 1
                pygame.draw.rect(DISPLAYSURF, RED, (360, 135 + 24*currentgame, 85, 24), 1)

            if event.type == KEYUP and event.key == K_UP:
                # pygame.draw.rect(DISPLAYSURF, BLACK, (360, 135 + 24 * currentgame, 85, 24), 1)
                if currentgame == 1:
                    currentgame = 7
                else:
                    currentgame -= 1
                pygame.draw.rect(DISPLAYSURF, BLUE, (360, 135 + 24*currentgame, 85, 24), 1)

            if event.type == KEYUP and event.key == K_LEFT:
                scores[currentgame*2-2] += 1

            if event.type == KEYUP and event.key == K_RIGHT:
                scores[currentgame*2-1] += 1




        # boxx, boxy = getBoxAtPixel(mousex, mousey)
        # if boxx != None and boxy != None:
        #     # The mouse is currently over a box.
        #     if not revealedBoxes[boxx][boxy]:
        #         drawHighlightBox(boxx, boxy)
        #     if not revealedBoxes[boxx][boxy] and mouseClicked:
        #         revealBoxesAnimation(mainBoard, [(boxx, boxy)])
        #         revealedBoxes[boxx][boxy] = True  # set the box as "revealed"
        #         if firstSelection == None:  # the current box was the first box clicked
        #             firstSelection = (boxx, boxy)
        #         else:  # the current box was the second box clicked
        #             # Check if there is a match between the two icons.
        #             icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
        #             icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)
        #
        #             if icon1shape != icon2shape or icon1color != icon2color:
        #                 # Icons don't match. Re-cover up both selections.
        #                 pygame.time.wait(1000)  # 1000 milliseconds = 1 sec
        #                 coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
        #                 revealedBoxes[firstSelection[0]][firstSelection[1]] = False
        #                 revealedBoxes[boxx][boxy] = False
        #             elif hasWon(revealedBoxes):  # check if all pairs found
        #                 gameWonAnimation(mainBoard)
        #                 pygame.time.wait(2000)
        #
        #                 # Reset the board
        #                 mainBoard = getRandomizedBoard()
        #                 revealedBoxes = generateRevealedBoxesData(False)
        #
        #                 # Show the fully unrevealed board for a second.
        #                 drawBoard(mainBoard, revealedBoxes)
        #                 pygame.display.update()
        #                 pygame.time.wait(1000)
        #
        #                 # Replay the start game animation.
        #                 startGameAnimation(mainBoard)
        #             firstSelection = None  # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()