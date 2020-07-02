from queue import PriorityQueue

def dijkstra(G,start):
    d = [float("inf")]*len(G)
    d[start] = 0
    Q = PriorityQueue()
    parent = [None]*len(G)
    Q.put((0,start))

    while not Q.empty():
        x = Q.get()
        vertex = x[1]
    
        for v, weight in G[vertex]:
            if d[v] > d[vertex] + weight:
                d[v] = d[vertex] + weight
                parent[v] = vertex
                Q.put((d[v], v))

        

G = [[(1,3), (4,3)], [(2,1)], [(3,3), (5,1)], [(1,3)], [(5,2)], [(0,6), (3,1)]]
print(len(G))