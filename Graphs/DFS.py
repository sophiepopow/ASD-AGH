

def DFSHelper(G,i, results, visited):

     
    for j in range(len(G[i])):
        if visited[G[i][j]] == False:
            visited[G[i][j]] = True
            results[G[i][j]] =  i
            DFSHelper(G,G[i][j], results, visited)
    return results

def DFS(G):
    results = [None]*len(G)
    visited = [False]*len(G)
    visited[0] = True
    return DFSHelper(G,0, results, visited)
    
G = [[1,2],[0,2,3],[3,1,0],[1,2]]
print( DFS(G) )