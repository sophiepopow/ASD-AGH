class Node:
    def __init__(self):
        self.distance = float("inf")
        self.previous = None
        
def relax(v,u,weight):
    if v.distance > u.distance + weight:
        v.distance = u.distance + weight
        v.previous = u
        
def BellmanFord(graph,s):
    s.distance = 0
    
    for vertex in range(len(graph)):
        for neighbour,weight in graph[vertex]:
            relax(neighbour,vertex, weight)
            
    for vertex in range(len(graph)):
        for neighbour,weight in graph[vertex]:
            if  neighbour.distance > vertex.distance + weight:
                print("Negative Cycle!")
                
    print("No negative Cycle")
