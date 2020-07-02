# Sprawdzanie czy graf nieskierowany posiada cykl.

def DFSHelper(G,i,visited, branch):
    
    for j in range(len(G[i])):
        if branch[j]:
            return False

        if G[i][j] and visited[j] == False:
            visited[j] = True
            branch[j] = True

            if not DFSHelper(G, j, visited, branch):
                return False
            branch[j] = False
    return True

def DFSCycle(G):
    visited = [False]* len(G)
    visited[0]= True

    for i in range(len(G)):
        if not visited[i]:
            visited[i]= True
            branch = [False]* len(G)
            if not DFSHelper(G,i, visited, branch):
                return False
    return True


def DFSCycle2(G):
	visited = [False] * len(G)
	def Traverse(par =-1,i=0):
		visited[i] = True
		for neighbour in G[i]:
				if neighbour == par:
					continue
				if visited[neighbour]:
					return True
				Traverse(i,neighbour)
		visited[i] = False
		return False
	return Traverse()
