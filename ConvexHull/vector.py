from point import Point
from math import atan2


class Vector:
    def __init__(self, point1, point2):
        self.vector = None
        if not point2:
            self.vector = point1
        else:
            self.vector = Point(point2.coords[0] - point1.coords[0] , point2.coords[1] - point1.coords[1])

    def cross_product(vec_1, vec_2):
        return vec_1.vector.coords[0] * vec_2.vector.coords[1] - vec_2.vector.coords[0] * vec_1.vector.coords[1]

    def get_angle(vec_1, vec_2):
        y = vec_2.coords[1] - vec_1.coords[1]
        x = vec_2.coords[0] - vec_1.coords[0]
        return atan2(y, x)
