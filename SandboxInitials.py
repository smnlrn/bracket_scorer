
import pygame
# from High_Score_Module import highscore
pygame.init()
FPS = 10  # frames per second, the general speed of the program
FPSCLOCK = pygame.time.Clock()
X = 800
Y = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (239, 118, 34)

font = pygame.font.SysFont("Arcade Alternate", 16)
fontbig = pygame.font.SysFont("Arcade Alternate", 36)
screen = pygame.display.set_mode((X, Y))
screen.fill(WHITE)
letterGap = 40
letterMarginLeft = 400
letterMarginTop = 300
squareSide = 20
squareAlignement = 5

switch = 0
my_score = 125

numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
letters = [["A", "B", "C", "D", "E", "F", "G", "H"], ["I", "J", "K", "L", "M", "N", "O", "P"],
           ["Q", "R", "S", "T", "U", "V", "W", "X"], ["Y", "Z", "-", ".", "<", ">", " ", "&"]]

Players = []

#
# class Player:
#     def __init__(self, name, sets, handicap, status, games_played):
#         self.name = name
#         self.sets = sets
#         self.handicap = handicap
#         self.status = status
#         self.gamesPlayed = games_played


def drawletters(screenin, alpha):
    for i in range(len(alpha)):
        for j in range(len(alpha[i])):
            letter = font.render(alpha[i][j], True, BLACK)
            screenin.blit(letter, (j*letterGap + letterMarginLeft, i*letterGap + letterMarginTop))


def drawnumbers(screenin, num):
    for i in range(len(num)):
        number = font.render(num[i], True, BLACK)
        screenin.blit(number, (20, i*letterGap + 20))


txt_surf = font.render("Press spacebar to select, press enter to continue...", True, BLACK)
txt_rect = txt_surf.get_rect(center=(X//2, Y - 20))
screen.blit(txt_surf, txt_rect)

x = 0
xmax = len(letters[0]) - 1
y = 0
ymax = len(letters) - 1
rectposxmin = letterMarginLeft - squareAlignement
rectposxmax = letterMarginLeft + letterGap * xmax - squareAlignement
rectposymin = letterMarginTop - squareAlignement
rectposymax = letterMarginTop + letterGap * ymax - squareAlignement
rectposxstep = letterGap
rectposystep = letterGap
rectposx = rectposxmin
rectposy = rectposymin
pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, squareSide, squareSide], 2)
initials = [" ", " ", " "]
ii = 0


def letterpicker(event, rectposx, rectposy, x, y):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        rectposx += rectposxstep
        x += 1
        if rectposx > rectposxmax:
            rectposx = rectposxmin
            x = 0
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        rectposx -= rectposxstep
        x -= 1
        if rectposx < rectposxmin:
            rectposx = rectposxmax
            x = xmax
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        rectposy += rectposystep
        y += 1
        if rectposy > rectposymax:
            rectposy = rectposymin
            y = 0
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        rectposy -= rectposystep
        y -= 1
        if rectposy < rectposymin:
            rectposy = rectposymax
            y = ymax
        # pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
    return (rectposx, rectposy, x, y)


done = True
while done:  # wait for user to acknowledge and return
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
            print("Initials: ", initials[0]+initials[1]+initials[2])
            Players.append(initials[0]+initials[1]+initials[2])
            print("Player:", Players[0])
            done = False
        screen.fill(WHITE)
        rectposx, rectposy, x, y = letterpicker(event, rectposx, rectposy, x, y)
        pygame.draw.rect(screen, ORANGE, [rectposx, rectposy, 20, 20], 2)
        drawletters(screen, letters)
        drawnumbers(screen, numbers)
        screen.blit(fontbig.render(initials[0], True, ORANGE), (200, 300))
        screen.blit(fontbig.render(initials[1], True, ORANGE), (230, 300))
        screen.blit(fontbig.render(initials[2], True, ORANGE), (260, 300))
        screen.blit(txt_surf, txt_rect)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # print(letters[y][x])
            initials[ii] = letters[y][x]
            ii += 1
            if ii > 2:
                ii = 0

    FPSCLOCK.tick(FPS)

    # The Cursor may flip to the next letter before the current letter changes...
    if switch > 10:
        switch = 0
    elif switch > 5:
        pygame.draw.line(screen, ORANGE, (200 + ii * 30, 333), (220 + ii * 30, 333), 3)
        switch += 1
    else:
        pygame.draw.line(screen, WHITE, (200 + ii * 30, 333), (220 + ii * 30, 333), 3)
        switch += 1

    pygame.display.flip()


pygame.quit()
