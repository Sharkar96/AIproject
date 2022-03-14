import graph
import treeManipulation as t


# The main loop to construct junction trees as one pleases
def mainLoop():
    while True:
        pressedKey = input("insert the number of nodes: ")
        try:
            numberOfNodes = int(pressedKey)
            g = graph.Graph(numberOfNodes)
            break
        except ValueError:
            print("please enter an integer")
    while True:
        pressedKey = input(
            "Adds a new edge with this notation: 'a,b' to make connection between vertex 'a' and 'b' or '$' to show the junction tree ")
        if pressedKey == '$':
            t.junctionTreeFinder(g)
            break
        else:
            splitString = pressedKey.split(sep=',')
            g.addEdge(splitString[0], splitString[1])


# example graph figure 4.12
def graphExample412():
    g = graph.Graph(8)
    g.addEdge('a', 'c')
    g.addEdge('b', 'c')
    g.addEdge('d', 'e')
    g.addEdge('c', 'e')
    g.addEdge('c', 'f')
    g.addEdge('e', 'g')
    g.addEdge('e', 'h')
    return g


# example graph figure 4.17

def graphExample417():
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
    return g


# example graph figure 4.15
def graphExample415():
    g = graph.Graph(6)
    g.addEdge('a', 'b')
    g.addEdge('a', 'c')
    g.addEdge('b', 'd')
    g.addEdge('d', 'f')
    g.addEdge('c', 'e')
    g.addEdge('e', 'f')
    return g


def main():
    keyPressed = input(
        "insert figure number to use a premade tree (notation: 4.11 -> 411)\n available eaxmples: 412, 415, 417 \n or press '0' to go in free insert mode: ")

    if keyPressed == '0':
        mainLoop()
    elif keyPressed == '412':
        g = graphExample412()
        t.junctionTreeFinder(g)
    elif keyPressed == '415':
        g = graphExample415()
        t.junctionTreeFinder(g)
    elif keyPressed == '417':
        g = graphExample417()
        t.junctionTreeFinder(g)
    else:
        print("please insert one of the specified inputs")


if __name__ == '__main__':
    main()
