
# sortowanie krawedzi malejaco
def sortingEdges(G,nodes):
    #(krawedz, (x,y))
    Edges = []
    n = len(G)
    #Graf nieksierowany!
    for x in range(n):
        for y in range(x+1):
            if G[x][y]:
                vertex = (nodes[x],nodes[y])
                Edges.append((G[x][y],vertex))

    Edges = sorted(Edges, key=lambda x: x[0], reverse=True)
    return Edges

#find union
# wykorzystujac find union sprawdzamy czy dana krawedz nie laczy zbiorow z 2 czerownymi
class Node:
    def __init__(self,id,colorCount):
        self.id = id
        self.parent = self
        self.rank = 0
        self.colorCount = 0
    
def findSet(x):
        if x != x.parent:
            x.parent = findSet(x.parent)
        return x.parent

def Union(x,y):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank:
        if(x.colorCount + y.colorCount < 2):
            y.parent = x
            x.colorCount += y.colorCount
        else: 
            return False

    else:
        if(x.colorCount + y.colorCount < 2):
            x.parent = y
            y.colorCount += x.colorCount

            if x.rank == y.rank:
                y.rank += 1

        else:
            return False
    return True

            
def timeToDestroy(G,nodes):
    Edges = sortingEdges(G,nodes)
    time = 0

    for i in range(len(Edges)):
        if not Union(Edges[i][1][0],Edges[i][1][1]):
            time += Edges[i][0]

    return time


nodes = [ Node(1,1),Node(2,1),Node(3,1),Node(4,0) ]
G = [[None,3,None,100], [3,None,2,4], [None,2,None,1], [100,4,1,None]]
print(timeToDestroy(G, nodes))