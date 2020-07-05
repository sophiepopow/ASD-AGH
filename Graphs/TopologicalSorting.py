#Algorytm z wykorzystaniem DFS

def topologicalDFS(graph, vertex,visited, sortedNodesStack):
    visited[vertex] = True

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            topologicalDFS(graph,neighbour, visited, sortedNodesStack)

    sortedNodesStack.insert(0,vertex)


def topologicalSort(graph):
    sortedNodesStack = []
    visited = [False]*len(graph)

    for vertex in range(len(graph)):
        if not visited[vertex]:
            topologicalDFS(graph, vertex,visited,sortedNodesStack)

    return sortedNodesStack

graph = [[2], [0,2], [], [0,1,4], [1,2], [0,4]]
print(topologicalSort(graph))