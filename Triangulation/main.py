from ConvexHull.point import *
from Utilities.draw import *

def find_first_left (points):
    point_left = None
    for pt in points:
        if point_left is None:
            point_left = pt
        else:
            if point_left.coords[0] > pt.coords[0]:
                point_left = pt
            elif point_left.coords[0] == pt.coords[0]:
                if point_left.coords[1] > pt.coords[1]:
                    point_left = pt

    return point_left

class Diagonal:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def create_triangles(point_left, points):
    diagonals = []
    index = 0
    for idx, i in enumerate(points):
        if point_left == i:
            index = idx



    for x in range(index+2, len(points)):
        diagonals.append(Diagonal(point_left, points[x]))

    for y in range(0, index-1):
        diagonals.append(Diagonal(point_left, points[y]))

    return diagonals

def main ():
    ''' With convex hull algorithm'''
    #convex = createConvex()
    convex = [Point(205, 14), Point(421, 39), Point(489, 59),
              Point(433, 273), Point(377, 408), Point(301, 479),
              Point(47, 488), Point(14, 207), Point(51, 103), Point(95, 39)]
    for i in convex:
        print(i.coords)
    window = init((500, 500))
    pointleft = find_first_left(convex)

    diagonals = create_triangles(pointleft, convex)
    showPoints(window, convex, diagonals)
    print("hello")


if __name__ == "__main__":
    main()