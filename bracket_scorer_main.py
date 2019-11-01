# Bracket Scorer
# By Simon Laurin simonlaurin@yahoo.com
# http://
# Released under a tbd license

import random, pygame, sys
from pygame.locals import *

FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 800  # size of window's width in pixels
WINDOWHEIGHT = 480  # size of windows' height in pixels
REVEALSPEED = 8  # speed boxes' sliding reveals and covers
BOXSIZE = 40  # size of box height & width in pixels
GAPSIZE = 10  # size of gap between boxes in pixels
BOARDWIDTH = 10  # number of columns of icons
BOARDHEIGHT = 7  # number of rows of icons
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
LEFTMARGIN = 20
RIGHTMARGIN = 20

PLAYERBOXHeight = 30
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
    # Quarter Final - left
    pygame.draw.rect(screen, PLAYERBOXColor, (LEFTMARGIN, PLAYERBOXGap,
                                              PLAYERBOXLength, PLAYERBOXHeight))
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
    # screen.blit(textPlayer1,((colScore+colMark/2-textPlayer1.get_width()/2), 9)) # Remove y+9 (for testing)
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

    #DISPLAYSURF.fill(BGCOLOR)


    while True:  # main game loop

        #DISPLAYSURF.fill(BGCOLOR)  # drawing the window

        initBracket(DISPLAYSURF)

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