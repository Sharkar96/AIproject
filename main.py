import graph
import treeManipulation as t
import MSTkruskal as a


def main():
    print("original graph: ")
    g = graph.Graph(6)
    g.addEdge('a', 'b')
    g.addEdge('a', 'c')
    g.addEdge('b', 'd')
    g.addEdge('d', 'f')
    g.addEdge('c', 'e')
    g.addEdge('e', 'f')

    g.display_AdjList()
    moralGraph = t.moralizer(g)
    print("moralized graph: ")
    moralGraph.display_AdjList()

    print("find Junction graph")
    cliques = t.findJunctionGraph(moralGraph)

    print("these are the cliques")
    print(cliques)

    print("remove useless nodes")
    cliques = t.minimizeCliques(cliques)
    print(cliques)

    print("let's construct a graph to perform the MST")
    MSTgraph = a.GraphForKruskal(cliques)
    MSTgraph.printMatrix()


if __name__ == '__main__':
    main()

# example graph figure 4.12
g = graph.Graph(8)
g.addEdge('a', 'c')
g.addEdge('b', 'c')
g.addEdge('d', 'e')
g.addEdge('c', 'e')
g.addEdge('c', 'f')
g.addEdge('e', 'g')
g.addEdge('e', 'h')

# example graph figure 4.17

g = graph.Graph(9)
g.addEdge('a', 'b')
g.addEdge('a', 'c')
g.addEdge('a', 'd')
g.addEdge('b', 'e')
g.addEdge('c', 'f')
g.addEdge('d', 'g')
g.addEdge('e', 'h')
g.addEdge('f', 'h')
g.addEdge('f', 'i')
g.addEdge('g', 'i')

# example graph figure 4.15
g = graph.Graph(6)
g.addEdge('a', 'b')
g.addEdge('a', 'c')
g.addEdge('b', 'd')
g.addEdge('d', 'f')
g.addEdge('c', 'e')
g.addEdge('e', 'f')
