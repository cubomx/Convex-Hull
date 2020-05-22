from ConvexHull.point import Event as Pt
from ConvexHull.point import Point
class Segment:
    def __init__(self, point1, point2):


        self.point1 = point1
        self.point2 = point2
        if self.order():
            aux = self.point1
            self.point1 = self.point2
            self.point2 = aux
        self.actual = self.point1


    def order(self):
        if self.point1.coords[1] > self.point2.coords[1]:
            return True
        elif self.point1.coords[1] == self.point2.coords[1]:
            if self.point1.coords[0] > self.point2.coords[0]:
                return True
        return False


    def getSlope(self):
        return (self.point2.coords[1] - self.point1.coords[1]) / (self.point2.coords[0] - self.point1.coords[0])

    def getX(self, y):
        x = y - self.point1.coords[1] / self.getSlope() + self.point1.coords[0]
        self.actual = Pt(x, y, [])

    def getIntersection(self, seg2):
        m1 = self.getSlope()
        m2 = seg2.getSlope()
        div = (m1 * -1) - (m2 * -1)
        return False
        xi = ((m1 * self.point1.coords[0]) - self.point1.coords[1]) * (-1) - ((m2 * seg2.point1.coords[0]) - seg2.point1.coords[1]) * (-1)
        xi = xi / (div)
        yi = (m1) * (m2 * seg2.point1.coords[0] - seg2.point1.coords[1]) - ((m2) * (m1 * self.point1.coords[0]) - self.point1.coords[1])
        yi = yi / ((m1 * -1) - (m2 * -1))
        return Pt(xi, yi, [])