class Point:
    EPSILON = -0.1

    def __init__(self, x, y):
        self.coords = [x, y]

    def show_coords(self):
        print(self.coords[0] + self.coords[1])

    def equal_to(self, point2):
        if abs(self.coords[0] - point2.coords[0]) < self.EPSILON and \
                abs(self.coords[1] - point2.coords[1]) < self.EPSILON:
            return True
        return False

class SegmentPoint(Point):
    def __init__(self, x, y, segment):
        self.coords = [x, y]
        self.segment = segment