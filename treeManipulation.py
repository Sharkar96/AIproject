import graph as g
import random
import MSTkruskal as a
import junctionTree as jt


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
    def _findJunctionGraph(eliminationOrder):
        cliques = []
        fillins = 0
        # FIRST we triangulate the graph
        # makes copies of the graph
        triangulatedGraph = moral.copy()
        eliminationGraph = moral.copy()

        for i in eliminationOrder:
            family = eliminationGraph.adjlist[i]

            # make every neighbour pairwise linked
            for j in range(len(family)):
                for k in range(j + 1, len(family)):
                    fillins += 1
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
        return fillins, triangulatedGraph, cliques

    # finds an elimination order
    permutationUsed = []
    nFillins = []
    # tries 100 different random permutation. For less than 5 nodes many of these will be duplicates
    for i in range(100):
        eliminationOrder = moral.vertices.copy()
        # permutes the default order
        random.shuffle(eliminationOrder)
        #
        # perform the triangulation measuring fillins
        fillins, triangulatedGraph, cliques = _findJunctionGraph(eliminationOrder)
        #
        permutationUsed.append(eliminationOrder)
        nFillins.append(fillins)

    # finds the index of the run that obtained the fewer number of fillins
    minFillinsIndex = nFillins.index(min(nFillins))
    #
    print("the following elimination order has been used")
    print(permutationUsed[minFillinsIndex])
    # use that index to get that permutation
    fillins, triangulatedGraph, cliques = _findJunctionGraph(permutationUsed[minFillinsIndex])
    #
    # now the graph is triangulated
    print("Triangulated graph: ")
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


# takes a DAG then applies the following operations:
# moralization, cliques finding, maxcliques finding, triangulation, max spanning tree
def junctionTreeFinder(graph: g.Graph):
    print("original graph: ")
    graph.display_AdjList()
    moralGraph = moralizer(graph)
    print("moralized graph: ")
    moralGraph.display_AdjList()

    print("find Junction graph")
    cliques = findJunctionGraph(moralGraph)

    print("these are the cliques")
    print(cliques)

    print("remove useless nodes")
    cliques = minimizeCliques(cliques)
    print(cliques)

    print("let's construct a graph to perform the MST")
    MSTgraph = jt.JunctionTree(cliques)
    print("this is the adjacency matrix of the junction graph")
    MSTgraph.printMatrix()

    print("Performs MST")
    MST = a.MSTKruskal(MSTgraph)

    print("This is the resulting MST displayed as adjacency matrix")
    print(MST)

    junctionTree = g.Graph.fromAdjacencyMatrix(vertices=cliques, adjacencyMatrix=MST)

    print("this is the Junction Tree displayed as adjacency list")
    junctionTree.display_AdjList()

    print("this is the Junction Tree displayed as adjacency matrix with separators")
    junctionTree = MSTgraph
    junctionTree.recalculateMatrix(MST)
    junctionTree.displayMatrixWithSeparator()
