from pprint import pprint

eps = 1 ** -.3


class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, otro):
        if abs(self.x - otro.x) < eps and abs(self.y - otro.y) < eps: return True
        return False

    def __lt__(self, otro):
        if self.y > otro.y: return True
        if self.y < otro.y: return False
        if self.x < otro.x: return True
        return False

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return self.x << 8 + self.y


class Cola:
    def __init__(self):
        self.q = []

    def __setitem__(self, punto, evento):
        self.q.append((punto, evento))
        self.q = sorted(self.q, key=lambda x: x[0])

    def __getitem__(self, punto):
        for i in self.q:
            if i[0] == punto: return i[1]

    def __contains__(self, punto):
        for i in self.q:
            if i[0] == punto: return True
        return False

    def __repr__(self):
        return repr(self.q)

    def __bool__(self):
        return bool(self.q)


class Segmento:
    def __init__(self, p1=Punto(), p2=Punto()):
        self.puntos = sorted([p1, p2])

    def __repr__(self):
        return f"[{self.puntos[0]}, {self.puntos[1]}]"

    def __hash__(self):
        return hash(tuple(self.puntos))


class Evento:
    def __init__(self, c=Punto(0, 0)):
        self.coord = c
        self.I = set()  # Inician en c
        self.T = set()  # Terminan en c
        self.C = set()  # Se intersecan en c

    def __iadd__(self, otro):
        self.I |= otro.I  # union
        self.T |= otro.T  # union
        self.C |= otro.C  # union

    def __hash__(self):
        return hash(self.coord)

    def __repr__(self):
        return f"--{self.coord}:: I:{self.I}, T:{self.T}, C:{self.C}"


class Eventos:
    def __init__(self):
        self.eventos = Cola()

    def add(self, evento=Evento()):
        if evento.coord in self.eventos:
            self.eventos[evento.coord] += evento
        else:
            self.eventos[evento.coord] = evento

    def __bool__(self):
        return bool(self.eventos)

    def __repr__(self):
        return hash(self.eventos)


class Barrido:
    def __init__(self):
        self.segmentos = []


Q = Eventos()
T = Barrido()

s1 = Segmento(Punto(0, 0), Punto(10, 10))
s2 = Segmento(Punto(2, 1), Punto(1, 2))

segmentos = [s1, s2]

print(segmentos)

for s in segmentos:
    p1, p2 = s.puntos

    e = Evento(p1)
    e.I.add(s)
    Q.add(e)

    e = Evento(p2)
    e.T.add(s)
    Q.add(e)

for q in Q.eventos.q:
    print(q[1])

while Q:
    Q
