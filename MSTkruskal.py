import numpy as np
import junctionTree as jt

class Node:
    def __init__(self, head, succ, element):
        self.head = head
        self.succ = succ
        self.element = element


class List:
    def __init__(self, head, tail):
        self.tail = tail
        self.representative = head
        self.nElements = 0

    # gives element as string return Node
    def findNode(self, element):
        found = False
        iter = self.representative
        while True:
            if iter.element == element:
                found = True
                break
            if iter == self.tail:
                break

            iter = iter.succ

        if found:
            return iter

    def print(self):
        iter = self.representative
        elements = str(iter.element)
        while iter != self.tail:
            iter = iter.succ
            elements += " " + str(iter.element)
        return elements


class UnionFind:
    def __init__(self):
        self.collection = []

    # makes singleton sets
    def makeSet(self, element):
        set = List(None, None)
        set.representative = Node(set, None, element)
        set.tail = set.representative
        set.nElements = 1
        self.collection.append(set)

    # more like find representative of the list containing the element provided as string
    def findSet(self, element):
        return self.findNode(element).head.representative

    # gives element in string returns node
    def findNode(self, element):
        for i in range(len(self.collection)):
            node = self.collection[i].findNode(element)
            if node is not None:
                return node

    def union(self, el1, el2):
        set1 = self.findNode(el1).head
        set2 = self.findNode(el2).head
        if set1 != set2:
            if set1.nElements <= set2.nElements:
                # 1 step:
                set2.tail.succ = set1.representative
                # 2 step:
                set2.tail = set1.tail
                # 3 step:
                iterator = set1.representative
                for i in range(set1.nElements):
                    iterator.head = set2
                    iterator = iterator.succ
                # 4 step:
                set2.nElements += set1.nElements
                # 5 step:
                self.collection.remove(set1)
            else:
                self.union(el2, el1)
        else:
            print("they are in the same set")

    def print(self):
        components = ""
        for i in range(len(self.collection)):
            components += "{" + self.collection[i].print() + "}"
        print(components)

def MSTKruskal(graph: jt.JunctionTree):
    uf = UnionFind()
    A = np.zeros(np.shape(graph.adjacencyMatrix))
    for i in range(len(graph.vertices)):
        uf.makeSet(graph.vertices[i])

    # these two represents the indices of the non zero elements
    [i, j] = np.nonzero(graph.adjacencyMatrix)

    weight = np.array(graph.adjacencyMatrix)[i, j]
    # these are the indices that would sort the weight
    sortedWeightIndices = np.argsort(weight)[::-1]

    if len(weight) > 0:
        for k in range(len(weight)):
            # these two represent indices of the minimum non-zero weight in the graph.graph
            minIndicesX = i[sortedWeightIndices[k]]
            minIndicesY = j[sortedWeightIndices[k]]

            if uf.findSet(graph.vertices[minIndicesX]) != uf.findSet(graph.vertices[minIndicesY]):
                A[minIndicesX, minIndicesY] = graph.adjacencyMatrix[minIndicesX, minIndicesY]
                uf.union(graph.vertices[minIndicesX], graph.vertices[minIndicesY])

    # makes the tree a graph (A represents a directed graph, makes it undirected)
    A = A + A.transpose()
    return A