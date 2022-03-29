import numpy as np


class Separator:
    def __init__(self, label):
        self.label = label

    def print(self):
        setToList = list(self.label)
        setToList.sort()
        stringifiedVertex = ""
        for j in setToList:
            stringifiedVertex += j
        print(stringifiedVertex, end=" ")


class JunctionTree:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencyMatrix = self.constructMatrix(vertices)
        self.adjacencyMatrixWithSeparator = self.constructMatrixWithSeparator(vertices, self.adjacencyMatrix)

    def constructMatrix(self, cliques: list):
        matrix = np.zeros((len(cliques), len(cliques)))
        for i in cliques:
            for j in cliques:
                if i != j:
                    matrix[cliques.index(i), cliques.index(j)] = len(i.intersection(j))
        return matrix

    def constructMatrixWithSeparator(self, vertices: list, adjacencyMatrix):
        w, h = np.shape(adjacencyMatrix)
        matrix = [[0 for x in range(w)] for y in range(h)]
        print(matrix)
        for i in vertices:
            for j in vertices:
                if i != j and i.intersection(j) != set():
                    matrix[vertices.index(i)][vertices.index(j)] = Separator(i.intersection(j))
                else:
                    matrix[vertices.index(i)][vertices.index(j)] = Separator("--")

        return matrix

    def recalculateMatrix(self, matrix):
        self.adjacencyMatrix = matrix
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if matrix[i, j] == 0:
                    self.adjacencyMatrixWithSeparator[i][j] = Separator("--")

    def displayMatrixWithSeparator(self):
        self.displayVertices()
        for i in self.adjacencyMatrixWithSeparator:
            for j in i:
                j.print()
            print()

    def displayVertices(self):
        vertices = self.vertices
        for i in range(len(self.vertices)):
            setToList = list(self.vertices[i])
            setToList.sort()
            stringifiedVertex = ""
            for j in setToList:
                stringifiedVertex += j
            vertices[i] = stringifiedVertex

        print(vertices)

    def printMatrix(self):
        print(self.adjacencyMatrix)
