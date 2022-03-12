import itertools
import copy
from string import ascii_lowercase
from collections import defaultdict


# from https://stackoverflow.com/questions/29351492/how-to-make-a-continuous-alphabetic-list-python-from-a-z-then-from-aa-ab-ac-e
def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)


# construct the list of vertices (a to z then aa, ab, ac, and so on)
def constructVertices(nVertices):
    vertices = []
    iter = nVertices
    for s in iter_all_strings():
        vertices.append(s)
        iter -= 1
        if iter == 0:
            break
    return vertices


class Graph:
    def __init__(self, nNodes: int):
        self.adjlist = defaultdict(list)  # defaultdict creates an empty list as default value
        self.nodes = nNodes
        self.vertices = constructVertices(nNodes)

    def copy(self):
        return copy.deepcopy(self)

    def addEdge(self, src: str, dst: str):
        self.adjlist[src].append(dst)
        if self.adjlist[src].count(dst) > 1:
            self.adjlist[src].remove(dst)

    def addBidirectionalEdge(self, src: str, dst: str):
        self.addEdge(src, dst)
        self.addEdge(dst, src)

    def display_AdjList(self):
        for item in self.adjlist.items():
            print(item)

    def eliminateVertexAndConnections(self, vertex: str):
        self.adjlist.pop(vertex)
        for i in self.adjlist:
            if self.adjlist[i].__contains__(vertex):
                self.adjlist[i].remove(vertex)

    # given a vertex finds its parents and return them as list. It's used by the moralize function
    def findParents(self, vertex: str):
        parents = []
        for i in self.adjlist:
            for j in self.adjlist[i]:
                if j == vertex:
                    parents.append(i)
        return parents

    #
