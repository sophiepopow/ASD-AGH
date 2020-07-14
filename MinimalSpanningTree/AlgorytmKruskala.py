class Node:
    def __init__(self,id):
        self.id = id
        self.parent = self
        self.rank = 0

def findSet(x):
    if x is not x.parent:
        x.parent = findSet(x.parent)
    return x.parent

def Union(x,y):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(G,V):
    G.sort(key = lambda x:x[2])
    Verticies = []
    A = []

    for i in range(V):
        Verticies.append(Node(i))

    for edge in G:
        if findSet(Verticies[edge[0]]) is not findSet(Verticies[edge[1]]):
            A.append(edge)
            Union(Verticies[edge[0]], Verticies[edge[1]])
    return A

G = [(0,1,2), (0,6,1), (0,5,6), (1,2,3), (2,3,1), (2,6,2), (3,4,7), (4,5,8), (4,6,5)]
Gl = [[(1,2),(6,1),(5,6)], [(0,2), (2,3)], [(1,3),(6,2)], [(2,1), (4,7)], [(3,7), (5,8), (6,5)], [(0,6),(4,8)], [(0,1), (2,2), (4,5)]]
V = 7

print(Kruskal(G,V))
