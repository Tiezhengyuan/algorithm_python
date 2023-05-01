'''
graph as matrix
'''

class Vertex:
    def __init__(self, val):
        self.val=val


class Edge:
    def __init__(self, vertex1, vertex2):
        self.v1=vertex1
        self.v2=vertex2
        # 1: v1->v2, 2: v2->v1, 3:both
        self.direction = None


class Graph:
    def __init__(self):
        self.conn = None