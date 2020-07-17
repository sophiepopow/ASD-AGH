from queue import PriorityQueue

def prima(G,V,s, parent):
    infVal = float("inf")
    verticies = PriorityQueue() 
    
    weight  = [infVal] * V
    weight[s] = 0
    visited = [False] * V
    
#    for i in range(V):
#        verticies.put((infVal, i))
    verticies.put((0,s))

    while not verticies.empty():
        u = verticies.get()
        if not visited[u[1]]:
            for v in range(V):
                if G[u[1]][v] is not None and not visited[v]:
                    weight[v] = G[u[1]][v]
                    verticies.put((G[u[1]][v], v))
                    parent[v] = u[1]
            visited[u[1]] = True

    return parent


V = 7
G = [ [0,2, None, None, 6, 1, None],[2,0,3,None,None,None,None],
 [None,3,0,1,None,None,2], [None,None,1,0,7,None,None],
 [None,None,None,7,0,8,5], [6,None,None,None, 8,0,None], [1,None, 2, None,5,None,0]]

G2 = [[None,None,1,10,None],[None,None,4,1,None],[None,4,None,2,1],[1,1,2,None,3],[None,None,1,3,10]]
V2 = 5
parent = [None]*V2
print(prima(G2,V2,2,parent))
