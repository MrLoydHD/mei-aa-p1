class Vertice:

    def __init__(self, x, y, weight) -> None:
        self.x = x
        self.y = y
        self.weight = weight

    def is_connected(self, edges):
        for edge in edges:
            if edge.contains_vertice(self):
                return True
        return False

    def __repr__(self):
        return "V[X:{0}, Y:{1}, W: {2}]".format(self.x, self.y, self.weight)

    def __eq__(self, other):
        """Overrides the default implementation"""
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return id(self)


class Edge:

    def __init__(self, v1: Vertice, v2: Vertice) -> None:
        self.v1 = v1
        self.v2 = v2

    def contains_vertice(self, vertice):
        return self.v1 == vertice or self.v2 == vertice

    def __repr__(self):
        return "E[V1: {0}, V2: {1}]".format(self.v1, self.v2)

    def __eq__(self, other):
        """Overrides the default implementation"""
        return self.v1 == other.v1 and self.v2 == other.v2 or self.v1 == other.v2 and self.v2 == other.v1

    def __hash__(self):
        return id(self)


class Clique:

    def __init__(self, vertices: list[Vertice], weight: int):
        self.vertices = vertices
        self.weight = weight

    def __repr__(self):
        return "Clique [Weight: {0}, Vertices: {1}]".format(self.weight, self.vertices)

    def __eq__(self, other):
        """Overrides the default implementation"""
        return self.vertices == other.vertices and self.weight == other.weight

    def __hash__(self):
        return id(self)
