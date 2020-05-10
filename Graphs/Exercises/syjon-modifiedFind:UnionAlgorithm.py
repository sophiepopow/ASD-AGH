
# sortowanie krawedzi malejaco
def sortingEdges(G):
    #(krawedz, (x,y))
    Edges = []
    n = len(G)
    #Graf nieksierowany!
    for x in range(n):
        for y in range(x+1):
            vertex = (x,y)
            Edges.add((G[x][y],vertex))

    Edges = sorted(Edges, key=lambda x: x[0], reverse=True)
    return Edges

#find union
# wykorzystujac find union sprawdzamy czy dana krawedz nie laczy zbiorow z 2 czerownymi
class Node:
    def __init__(self,id,color):
        self.id = id
        self.parent = parent
        self.rank = rank 
        self.color = color
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

            
def timeToDestroy(G):
    Edges = sortingEdges(G)
    time = 0

    for i in range(len(Edges)):
        if not Union(Edges[i][1]):
            time += Edges[i][0]

    return time


