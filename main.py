import graph
import treeManipulation as t


def main():
    print("original graph: ")
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

    g.display_AdjList()
    moralGraph = t.moralizer(g)
    print("moralized graph: ")
    moralGraph.display_AdjList()

    print("triangulated graph")
    t.triangulation(moralGraph)


if __name__ == '__main__':
    main()

#example graph figure 4.12
g = graph.Graph(8)
g.addEdge('a','c')
g.addEdge('b','c')
g.addEdge('d','e')
g.addEdge('c','e')
g.addEdge('c','f')
g.addEdge('e','g')
g.addEdge('e','h')

vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
jensenGraph = [[0, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
