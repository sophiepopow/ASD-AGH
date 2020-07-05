def BFSWeightedGraph(graph,s):
    Q = []
    results = [None]*len(graph)
    visited = [False]*len(graph)
    results[s]=(None,0)
    visited[s] = False
    Q.append((s,0,None))

    while Q:
        first = Q.pop(0)
        current = first[0]
        parent = first[2]
        weight = first[1]

        if weight != 0:
            fakeVertex = (current, weight-1,parent)
            Q.append(fakeVertex)
        else:
            for neighbour in range(len(graph)):
                if graph[current][neighbour] and not visited[neighbour]:
                    val = graph[current][neighbour]
                    fakeVertex = (neighbour,val-1,current)
                    Q.append(fakeVertex)

            if parent is not None:
                if not visited[current]:
                    paernt_shortest_path_weight = results[parent][1]
                    current_path_from_parent_weight =  graph[parent][current]
                    results[current] = (parent, paernt_shortest_path_weight + current_path_from_parent_weight)
            visited[current] = True

    return results

graph = [[None, 3, 4, None, None, None],
        [3, None, 1, 2, None, None],
        [4, 1, None, 2, None, 1],
        [None, 2, 2, None, 3, None],
        [None, None, None, 3, None, 2],
        [None, None, 1, None, 2, None ]]

graphList = [[(1,3), (4,3)], [(2,1)], [(3,3), (5,1)], [(1,3)], [(5,2)], [(0,6), (3,1)]]
print(BFSWeightedGraph(graph,0))