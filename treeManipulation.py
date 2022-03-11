import graph as g
from itertools import combinations


# get a DAG and returned it's moralized counterpart
def moralizer(DAG: g.Graph):
    workingGraph = DAG.copy()
    # adds a link between any pair of variables with a common child
    for i in workingGraph.vertices:
        p = workingGraph.findParents(i)
        if len(p) > 1:
            for j in range(len(p)):
                for k in range(j + 1, len(p)):
                    workingGraph.addEdge(p[j], p[k])

    # drops the directions from every arc
    bidirectionalierList = []
    for i in workingGraph.adjlist:
        for j in workingGraph.adjlist[i]:
            bidirectionalierList.append([j, i])

    for i in bidirectionalierList:
        workingGraph.addEdge(i[0], i[1])

    return workingGraph


# takes a DAG  and finds the triangulated graph
def triangulation(moral: g.Graph):
    triangulatedGraph = moral.copy()
    eliminationGraph = moral.copy()

    eliminationOrder = moral.vertices

    for i in eliminationOrder:
        family = eliminationGraph.adjlist[i]

        # make every neighbour pairwise linked
        for j in range(len(family)):
            for k in range(j + 1, len(family)):
                triangulatedGraph.addBidirectionalEdge(family[j], family[k])
                eliminationGraph.addBidirectionalEdge(family[j], family[k])

        #eliminate the node
        eliminationGraph.eliminateVertexAndConnections(i)

    eliminationGraph.display_AdjList()
    triangulatedGraph.display_AdjList()