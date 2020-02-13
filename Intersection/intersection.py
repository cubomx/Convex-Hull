from ConvexHull.point import Point as Pt
from ConvexHull.segment import Segment as Seg
import pygame, sys
from time import sleep


def orderEvents(points):
    events = sorted(points, reverse=False, key=lambda x: x[1])
    for i in range(0, len(points) - 1):
        if points[i][1] == points[i+1][1]:
            if points[i][0] > points[i+1][0]:
                aux = points[i]
                points[i] = points[i+1]
                points[i+1] = aux
    return events


def main():
    segments = list()
    file = open("1.in", "r")
    content = file.read().split("\n")
    for index,  i in enumerate(content):
        if index > 0:
            points = i.split()
            segments.append(Seg(Pt(int(points[0]), int(points[1])) , Pt(int(points[2]), int(points[3]))))

    pygame.init()

    size = (500, 500)
    white = 255, 255, 255
    blue = 0, 0, 255
    red = 255, 0, 0
    yellow = 255, 255, 0
    green = 0, 255, 0
    other = 100, 100, 100
    screen = pygame.display.set_mode(size)
    barrier = Seg(Pt(0, 0), Pt(size[0] - 1, 0))
    point_y = 0
    active_segs = set()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)
        for seg in segments:
            pygame.draw.line(screen, blue, (seg.point1.coords[0], seg.point1.coords[1]),
                             (seg.point2.coords[0], seg.point2.coords[1]))
            valid = False
            y = barrier.point1.coords[1] + point_y

            if seg.point1.coords[1] != y:
                pygame.draw.circle(screen, green, (seg.point1.coords[0], seg.point1.coords[1]), 4, 0)
            else:
                valid = True
                pygame.draw.circle(screen, red, (seg.point1.coords[0], seg.point1.coords[1]), 4, 0)
            if seg.point2.coords[1] != y:
                pygame.draw.circle(screen, green, (seg.point2.coords[0], seg.point2.coords[1]), 4, 0)
            else:
                valid = True
                pygame.draw.circle(screen, red, (seg.point2.coords[0], seg.point2.coords[1]), 4, 0)
            if valid:
                if seg in active_segs:
                    active_segs.remove(seg)
                else:
                    active_segs.add(seg)
        for seg in active_segs:
            pygame.draw.line(screen, other, (seg.point1.coords[0], seg.point1.coords[1]),
                             (seg.point2.coords[0], seg.point2.coords[1]))

        pygame.draw.line(screen, yellow, (barrier.point1.coords[0], y), (barrier.point2.coords[0], y))
        sleep(.5)
        if barrier.point1.coords[1] + point_y + 1 < size[0]:
            point_y += 1
        pygame.display.update()


if __name__ =='__main__':
    main()
