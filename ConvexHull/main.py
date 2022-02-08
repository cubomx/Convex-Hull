from point import Point as pt
from segment import Segment
from vector import Vector
from random import randint
import sys, pygame, time
''' Get the area of any convex polygon '''


def area(convex_elements):
    sum_a, sum_b = 0.0, 0.0
    for index, vertex in enumerate(convex_elements):
        if index + 1 < len(convex_elements):
            sum_a += vertex.coords[0] * convex_elements[index + 1].coords[1]
            sum_b += vertex.coords[1] * convex_elements[index + 1].coords[0]
    return (sum_a - sum_b) / 2


''' Get the point with the minor y, and the minor x'''


def lowest_point(pts):
    lowest = pts[0]
    for index, point in enumerate(pts):
        if index != 0:
            if point.coords[1] == lowest.coords[1]:
                if point.coords[0] < lowest.coords[0]:
                    lowest = point
            if point.coords[1] < lowest.coords[1]:
                lowest = point
    return lowest


''' Create all the segments with all the points available'''


def get_segments(pts):
    segs = []
    for pt_a in pts:
        for pt_b in pts:
            if pt_a != pt_b:
                segs.append(Segment(pt_a, pt_b))
    return segs


''' Check if point is to the left/right of an segment '''


def is_convex(vec, point, point1):
    if point != point1:
        seg = Vector(point1, point)
        res = Vector.cross_product(vec, seg)
        if res < point.EPSILON:
            return False
    return True


def scan_angles(pts, lowest):
    angles = list()
    for point in pts:
        other = pt(0, 0)
        vec = Vector(other, point)
        angles.append((vec, Vector.get_angle(lowest, vec.vector)))
    angles = sorted(angles, reverse=False, key=lambda x: x[1])
    return angles


''' Lowest way to get the polygon that covers all the points'''

def main():
    points = list()  # list of all points
    for i in range(0, 50):
        x, y = randint(10.0, 490.0), randint(10.0, 490.0)
        points.append(pt(x, y))

    pygame.init()

    size = width, height = 500, 500
    white = 255, 255, 255
    blue = 0, 0, 255
    red = 255, 0, 0
    yellow = 255, 255, 0
    green = 0, 255, 0
    screen = pygame.display.set_mode(size)
    lowest = lowest_point(points)
    angles = scan_angles(points, lowest)
    convex_h = []
    convex_h.append(lowest)
    convex_h.append(angles.pop(0)[0].vector)
    convex_h.append(angles.pop(0)[0].vector)
    actual = angles.pop(0)[0].vector
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(white)

        while True:
            pygame.draw.line(screen, yellow, (convex_h[-1].coords[0], convex_h[-1].coords[1]), (actual.coords[0], actual.coords[1]))
            vec_1 = Vector(convex_h[-2], convex_h[-1])
            if not is_convex(vec_1, actual, convex_h[-2]):
                convex_h.pop()
            else:
                convex_h.append(actual)
                if len(angles) > 0:
                    actual = angles.pop(0)[0].vector
                else:
                    break
            break
        if len(angles) == 0 and actual == convex_h[-1] == actual:
            convex_h.append(lowest)
        if convex_h != None:
            for index, point in enumerate(convex_h):
                if index + 1 < len(convex_h):
                    point1, point2 = point, convex_h[index + 1]
                    pygame.draw.line(screen, red, (abs(point1.coords[0]), abs(point1.coords[1])),
                                     (abs(point2.coords[0]), abs(point2.coords[1])), 1)
                else:
                    point2 = convex_h[0]
                    pygame.draw.line(screen, red, (abs(point.coords[0]), abs(point.coords[1])),
                                     (point2.coords[0], point2.coords[1]), 1)
        for point in points:
            pygame.draw.circle(screen, blue, (point.coords[0], point.coords[1]), 4, 0)
        time.sleep(.5)
        pygame.display.update()


if __name__ == '__main__':
   main()