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
def findJunctionGraph(moral: g.Graph):
    # I may modify the algorithm in the future trying different permutation of eliminationOrder until it finds the one that adds the less fill-ins
    cliques = []
    # FIRST we triangulate the graph

    # makes copies of the graph
    triangulatedGraph = moral.copy()
    eliminationGraph = moral.copy()

    # finds an elimination order
    eliminationOrder = moral.vertices

    for i in eliminationOrder:
        family = eliminationGraph.adjlist[i]

        # make every neighbour pairwise linked
        for j in range(len(family)):
            for k in range(j + 1, len(family)):
                triangulatedGraph.addBidirectionalEdge(family[j], family[k])
                eliminationGraph.addBidirectionalEdge(family[j], family[k])

        # finds cliques
        clique = set()
        clique.add(i)
        connectedNodes = eliminationGraph.adjlist.get(i)
        for j in connectedNodes:
            clique.add(j)
        cliques.append(clique)

        # eliminate the node
        eliminationGraph.eliminateVertexAndConnections(i)
    # now the graph is triangulated
    triangulatedGraph.display_AdjList()

    return cliques


# takes a list of cliques removes the non maximal cliques
def minimizeCliques(cliques: list):
    uselessCliques = []
    for i in range(len(cliques)):
        for j in range(len(cliques)):
            if i != j and cliques[j].issubset(cliques[i]):
                uselessCliques.append(cliques[j])

    for i in uselessCliques:
        if cliques.__contains__(i):
            cliques.remove(i)

    return cliques
