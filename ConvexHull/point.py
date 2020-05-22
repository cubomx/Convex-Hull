

class Point:
    EPSILON = -0.1

    def __init__(self, x, y):
        self.coords = (x, y)

    def show_coords(self):
        print(self.coords[0] + self.coords[1])

    def __eq__(self, other):
        if self.coords[0] == other.coords[0]:
            if self.coords[1] == other.coords[1]:
                return True
        return False


class Event():
    def __init__(self, x, y, segment):
        self.coords = [x, y]
        self.__segment = segment
        self.intersects = set()

    def insert_segment(self, segment, itIntersect=False):
        if itIntersect:
            self.intersects.add(segment)
        self.__segment.append(segment)

    def get_seg(self, index):
        if index == -1:
            return self.__segment
        return self.__segment[index]

    def start(self):
        starting = set()
        for seg in self.__segment:
            if seg.point1.coords[0] == self.coords[0]:
                if seg.point1.coords[1] == self.coords[1]:
                    starting.add(seg)
        return starting

    def ends(self):
        ending = set()
        for seg in self.__segment:
            if seg.point2.coords[0] == self.coords[0]:
                if seg.point2.coords[1] == self.coords[1]:
                    ending.add(seg)
        return ending

    def intersection(self):
        return self.intersects