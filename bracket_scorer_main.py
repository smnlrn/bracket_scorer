# Bracket Scorer
# By Simon Laurin simonlaurin@yahoo.com
# http://
# Released under a tbd license

import random, pygame, sys
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

PLAYERBOXHeight = 30 # REFERENCE 7 letters font size 30
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

# Player box center coordinates
G1P1cxy = (LEFTMARGIN + PLAYERBOXLength * 1 / 2, TOPMARGIN + PLAYERBOXHeight / 2)
G1P2cxy = (LEFTMARGIN + PLAYERBOXLength * 1 / 2, TOPMARGIN + PLAYERBOXGap * 2 + PLAYERBOXHeight * 5 / 2)

G2P1cxy = (LEFTMARGIN + PLAYERBOXLength * 1 / 2, TOPMARGIN + PLAYERBOXGap * 4 + PLAYERBOXHeight * 7 / 2)
G2P2cxy = (LEFTMARGIN + PLAYERBOXLength * 1 / 2, TOPMARGIN + PLAYERBOXGap * 6 + PLAYERBOXHeight * 11 / 2)

G3P1cxy = (WINDOWWIDTH - RIGHTMARGIN - PLAYERBOXLength / 2, TOPMARGIN + PLAYERBOXHeight / 2)
G3P2cxy = (WINDOWWIDTH - RIGHTMARGIN - PLAYERBOXLength / 2, TOPMARGIN + PLAYERBOXGap * 2 + PLAYERBOXHeight * 5 / 2)

G4P1cxy = (WINDOWWIDTH - RIGHTMARGIN - PLAYERBOXLength / 2, TOPMARGIN + PLAYERBOXGap * 4 + PLAYERBOXHeight * 7 / 2)
G4P2cxy = (WINDOWWIDTH - RIGHTMARGIN - PLAYERBOXLength / 2, TOPMARGIN + PLAYERBOXGap * 6 + PLAYERBOXHeight * 11 / 2)

G5P1cxy = (LEFTMARGIN + PLAYERBOXLength * 7 / 6, TOPMARGIN + PLAYERBOXGap * 1 + PLAYERBOXHeight * 3 / 2)
G5P2cxy = (LEFTMARGIN + PLAYERBOXLength * 7 / 6, TOPMARGIN + PLAYERBOXGap * 5 + PLAYERBOXHeight * 9 / 2)

G6P1cxy = (WINDOWWIDTH - RIGHTMARGIN - PLAYERBOXLength * 7 / 6, TOPMARGIN + PLAYERBOXGap * 1 + PLAYERBOXHeight * 3 / 2)
G6P2cxy = (WINDOWWIDTH - RIGHTMARGIN - PLAYERBOXLength * 7 / 6, TOPMARGIN + PLAYERBOXGap * 5 + PLAYERBOXHeight * 9 / 2)

G7P1cxy = (LEFTMARGIN + PLAYERBOXLength * 11 / 6, TOPMARGIN + PLAYERBOXGap * 3 + PLAYERBOXHeight * 3 / 1)
G7P2cxy = (WINDOWWIDTH - RIGHTMARGIN - PLAYERBOXLength * 11 / 6, TOPMARGIN + PLAYERBOXGap * 3 + PLAYERBOXHeight * 3 / 1)


def initPlayers(fieldSize):
    # Get players name

    # Random seed / no seed

    # Put names on Display

    # Return seeded players
    return ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Bye",]



def initBracket(screen):
    #screen.fill(GRAY)
    # Initialize the joysticks
    pygame.joystick.init()
    # column Grid
    # pygame.draw.line(screen, BLACK, (20, 100), (150,100), 3)
    # pygame.draw.line(screen, BLACK, (650, 100), (780,100), 3)
    # pygame.draw.line(screen, BLACK, (200, 100), (330,100), 3)
    # pygame.draw.line(screen, BLACK, (440, 100), (570,100), 3)
    # playerBox = pygame.rect(20, 100, 110,100)

    background_image = pygame.image.load("Grey-Rock-Structure.jpg").convert()
    screen.blit(background_image, (0, 0))
    player_box = pygame.image.load("PlayerBox.png").convert()


    # Quarter Final - left
    # pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN, PLAYERBOXGap,
    #                                           PLAYERBOXLength, PLAYERBOXHeight))
    screen.blit(player_box, (LEFTMARGIN, PLAYERBOXGap))

    pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN, PLAYERBOXGap*3+PLAYERBOXHeight*2,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN, PLAYERBOXGap*5+PLAYERBOXHeight*3,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN, PLAYERBOXGap*7+PLAYERBOXHeight*5,
                                              PLAYERBOXLength, PLAYERBOXHeight))

    # Quarter Final - right
    pygame.draw.rect(screen, PLAYERBOXColor, (WINDOWWIDTH-RIGHTMARGIN-PLAYERBOXLength, PLAYERBOXGap,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (WINDOWWIDTH-RIGHTMARGIN-PLAYERBOXLength, PLAYERBOXGap*3+PLAYERBOXHeight*2,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (WINDOWWIDTH-RIGHTMARGIN-PLAYERBOXLength, PLAYERBOXGap*5+PLAYERBOXHeight*3,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (WINDOWWIDTH-RIGHTMARGIN-PLAYERBOXLength, PLAYERBOXGap*7+PLAYERBOXHeight*5,
                                              PLAYERBOXLength, PLAYERBOXHeight))

    # SemiFinals
    pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN+PLAYERBOXLength*2/3,
                                              PLAYERBOXGap*2+PLAYERBOXHeight,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN+PLAYERBOXLength*2/3,
                                              PLAYERBOXGap*6+PLAYERBOXHeight*4,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (WINDOWWIDTH-RIGHTMARGIN-PLAYERBOXLength*5/3,
                                              PLAYERBOXGap*2+PLAYERBOXHeight,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (WINDOWWIDTH-RIGHTMARGIN-PLAYERBOXLength*5/3,
                                              PLAYERBOXGap*6+PLAYERBOXHeight*4,
                                              PLAYERBOXLength, PLAYERBOXHeight))

    # Finals
    pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN+PLAYERBOXLength*4/3,
                                              PLAYERBOXGap*4+PLAYERBOXHeight*2.5,
                                              PLAYERBOXLength, PLAYERBOXHeight))
    pygame.draw.rect(screen, PLAYERBOXColor, (WINDOWWIDTH-RIGHTMARGIN-PLAYERBOXLength*7/3,
                                              PLAYERBOXGap*4+PLAYERBOXHeight*2.5,
                                              PLAYERBOXLength, PLAYERBOXHeight))

    # pygame.draw.line(screen, BLACK, (colScore+colMark, 0), (colScore+colMark, screenHeight), 1)
    # pygame.draw.line(screen, BLACK, (colScore+colMark+colTarget, 0), (colScore+colMark+colTarget, screenHeight), 1)
    # pygame.draw.line(screen, (0,0,0,), (0, rowTop + 2), (screenWidth, rowTop + 2), 1)
    # pygame.draw.line(screen, (0,0,0,), (0, rowTop), (screenWidth, rowTop), 1)
    #
    #
    #     # Target TODO Better center the text with textVar.get_width(), get_heigth() & round()
    # screen.blit(textPlayer1, LEFTMARGIN, PLAYERBOXGap) # Remove y+9 (for testing)fontBig.render(str(scores), True, BLACK)
    # #screen.blit(textPlayer2,((screenWidth-colScore-colMark/2 - textPlayer2.get_width()/2), 9))
    # screen.blit(text20,(round((screenWidth-text20.get_width())/2), rowTop))
    # screen.blit(text19,(round((screenWidth-text19.get_width())/2), rowTop+1*rowHeight))
    # screen.blit(text18,(round((screenWidth-text18.get_width())/2), rowTop+2*rowHeight))
    # screen.blit(text17,(round((screenWidth-text17.get_width())/2), rowTop+3*rowHeight))
    # screen.blit(text16,(round((screenWidth-text16.get_width())/2), rowTop+4*rowHeight))
    # screen.blit(text15,(round((screenWidth-text15.get_width())/2), rowTop+5*rowHeight))
    # screen.blit(text14,(round((screenWidth-text14.get_width())/2), rowTop+6*rowHeight))
    # screen.blit(textDouble,(round((screenWidth-textDouble.get_width())/2), rowTop+7*rowHeight))
    # screen.blit(textTriple,(round((screenWidth-textTriple.get_width())/2), rowTop+8*rowHeight))
    # screen.blit(textBull,(round((screenWidth-textBull.get_width())/2), rowTop+9*rowHeight))
    # screen.blit(font.render(str(currentRound), True, (0, 0, 0)), (round((screenWidth-font.render(str(currentRound), True, (0, 0, 0)).get_width())/2), 9))
    #


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Simple Elimination Tournament')

    fontBracket = pygame.font.SysFont("monaco", 30)
    textPlayer1 = fontBracket.render("joueur 1", True, WHITE)
    rectPlayer1 = textPlayer1.get_rect(center=G1P1cxy)
    textPlayer2 = fontBracket.render("joueur 2", True, WHITE)
    rectPlayer2 = textPlayer2.get_rect(center=G1P2cxy)
    textPlayer3 = fontBracket.render("joueur 3", True, WHITE)
    rectPlayer3 = textPlayer3.get_rect(center=G2P1cxy)
    textPlayer4 = fontBracket.render("joueur 4", True, WHITE)
    rectPlayer4 = textPlayer4.get_rect(center=G2P2cxy)
    textPlayer5 = fontBracket.render("joueur 5", True, WHITE)
    rectPlayer5 = textPlayer5.get_rect(center=G3P1cxy)
    textPlayer6 = fontBracket.render("joueur 6", True, WHITE)
    rectPlayer6 = textPlayer6.get_rect(center=G3P2cxy)
    textPlayer7 = fontBracket.render("joueur 7", True, WHITE)
    rectPlayer7 = textPlayer7.get_rect(center=G4P1cxy)
    textPlayer8 = fontBracket.render("joueur 8", True, WHITE)
    rectPlayer8 = textPlayer8.get_rect(center=G4P2cxy)

    rectWinner1 = textPlayer1.get_rect(center=G5P1cxy)
    rectWinner2 = textPlayer1.get_rect(center=G5P2cxy)
    rectWinner3 = textPlayer1.get_rect(center=G6P1cxy)
    rectWinner4 = textPlayer1.get_rect(center=G6P2cxy)
    rectWinner5 = textPlayer1.get_rect(center=G7P1cxy)
    rectWinner6 = textPlayer1.get_rect(center=G7P2cxy)

    initBracket(DISPLAYSURF)
    playerList = initPlayers(8)

    DISPLAYSURF.blit(textPlayer1, rectPlayer1)
    DISPLAYSURF.blit(textPlayer2, rectPlayer2)
    DISPLAYSURF.blit(textPlayer3, rectPlayer3)
    DISPLAYSURF.blit(textPlayer4, rectPlayer4)
    DISPLAYSURF.blit(textPlayer5, rectPlayer5)
    DISPLAYSURF.blit(textPlayer6, rectPlayer6)
    DISPLAYSURF.blit(textPlayer7, rectPlayer7)
    DISPLAYSURF.blit(textPlayer8, rectPlayer8)

    DISPLAYSURF.blit(textPlayer1, rectWinner1)
    DISPLAYSURF.blit(textPlayer3, rectWinner2)
    DISPLAYSURF.blit(textPlayer5, rectWinner3)
    DISPLAYSURF.blit(textPlayer7, rectWinner4)
    DISPLAYSURF.blit(textPlayer1, rectWinner5)
    DISPLAYSURF.blit(textPlayer7, rectWinner6)



    while True:  # main game loop

        #DISPLAYSURF.fill(BGCOLOR)  # drawing the window


        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # elif event.type == MOUSEMOTION:
            #     # mousex, mousey = event.pos
            # elif event.type == MOUSEBUTTONUP:
            #     # mousex, mousey = event.pos
            #     # mouseClicked = True

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