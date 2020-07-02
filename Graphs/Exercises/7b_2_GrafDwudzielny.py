#Sprawdzanie czy graf nieskierowany jest dwudzielny (czyli czy da się podzielić jego wierzchołki na dwa zbiory, takie że krawędzie łączą jedynie wierzchołki z różnych zbiorów).

def DFSHelper(G,i,colors,parentColor,visited):
    for j in range(len(G[i])):
        if G[i][j] and visited[j] == False:
            visited[j] = True
            if colors[j] and colors[j] == colors[i]:
                return False
            colors[j] = not colors[i]
            if not DFSHelper(G, j, colors, colors[j], visited)
                return False
    return True

def DFSWithColors(G):
    colors = [None]*len(G) 
    visited = [False]* len(G)
    visited[0]= True

    for i in range(len(G)):
        if not visited[i]:
            visited[i]= True
            colors[i] = True
            if not DFSHelper(G,i,colors, colors[i], visited):
                return False
    return True
