import pygame, sys

from ConvexHull.point import Point as pt
from ConvexHull.segment import Segment
from ConvexHull.vector import Vector
from random import randint

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


''' Faster way to get the convex hull by ordering by the angles from the pivot '''


def graham_scan(pts):
    lowest = lowest_point(pts)
    angles = scan_angles(pts, lowest)

    convex_el = list()
    convex_el.append(lowest)
    convex_el.append(angles.pop(0)[0].vector)
    convex_el.append(angles.pop(0)[0].vector)
    actual = angles.pop(0)[0].vector
    while True:
        vec_1 = Vector(convex_el[-2], convex_el[-1])
        if not is_convex(vec_1, actual, convex_el[-2]):
            convex_el.pop()
        else:
            convex_el.append(actual)
            if len(angles) > 0:
                actual = angles.pop(0)[0].vector
            else:
                break
    return convex_el


''' Lowest way to get the polygon that covers all the points'''


def convex_hull(segs, pts):
    convex_elems = set()
    for segment in segs:
        point1, point2 = segment.point1, segment.point2
        valid = True
        other = Vector(point1, point2)
        for point in pts:
            if not is_convex(other, point, point1):  # Know if all points are to the right of that segment
                valid = False
        if valid:
            convex_elems.add(segment)
    return convex_elems


points = list()  # list of all points
'''for i in range(quantity):
    
    for pos in range(0, len(line) - 1, 2):
        points.append(pt(line[pos], line[pos + 1])'''

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

segments = get_segments(points)
convex, convex_h = None, None
# convex = convex_hull(segments, points)

convex_h = graham_scan(points)
convex_h.append(lowest_point(points))
print(format(area(convex_h), '.2f'))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(white)
    if convex_h != None:
        for index, point in enumerate(convex_h):
            if index + 1 < len(convex_h):
                point1, point2 = point, convex_h[index + 1]
                pygame.draw.line(screen, red, (int(point1.coords[0]), int(point1.coords[1])),
                                 (int(point2.coords[0]), int(point2.coords[1])), 1)
            else:
                point2 = convex_h[0]
                pygame.draw.line(screen, red, (int(point.coords[0]), int(point.coords[1])),
                                 (int(point2.coords[0]), int(point2.coords[1])), 1)
    else:
        for convex_pts in convex:
            point1, point2 = convex_pts.point1, convex_pts.point2
            pygame.draw.line(screen, red, (point1.coords[0], point1.coords[1]), (point2.coords[0], point2.coords[1]), 1)

    for point in points:
        pygame.draw.circle(screen, green, (int(point.coords[0]), int(point.coords[1])), 4, 0)

    pygame.display.flip()
