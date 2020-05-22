import pygame, sys
''' COLORS '''
white = 255, 255, 255
blue = 0, 0, 255
red = 255, 0, 0
yellow = 255, 255, 0
green = 0, 255, 0

def init(size):
    pygame.init()

    size = width, height = 500, 500

    screen = pygame.display.set_mode(size)

    return screen

def showPoints(screen, convex_h, diagonals):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        if convex_h != None:
            for index, point in enumerate(convex_h):
                pygame.draw.circle(screen, green, (int(point.coords[0]), int(point.coords[1])), 4, 1)
                if index + 1 < len(convex_h):
                    point1, point2 = point, convex_h[index + 1]
                    pygame.draw.line(screen, red, (int(point1.coords[0]), int(point1.coords[1])),
                                     (int(point2.coords[0]), int(point2.coords[1])), 1)

                else:
                    point2 = convex_h[0]
                    pygame.draw.line(screen, red, (int(point.coords[0]), int(point.coords[1])),
                                     (int(point2.coords[0]), int(point2.coords[1])), 1)
            for diag in diagonals:
                pygame.draw.line(screen, blue, (int(diag.start.coords[0]), int(diag.start.coords[1])),
                                 (int(diag.end.coords[0]), int(diag.end.coords[1])), 1)


        pygame.display.flip()