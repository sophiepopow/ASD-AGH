def BFS(M,n,m,T):

    def check(x, y):
    return x >= 0 and y >= 0 and x < n and y < m
    
    
    Visited = [[True]* m for i in range(n)]
    Q = []
    Q.append((0,0))

    while Q:
        el = Q.pop(0)
        x = el[0]
        y = el[1]
        
        if x == n-1 and y == m-1:
            return True
            
            
        if check(x-1,y) and M[x-1][y] >= T:
            if Visited[x-1][y]:
                Visited[x-1][y] = False
                Q.append((x-1,y))
                

        if check(x+1,y) and M[x+1][y] >= T:
            if Visited[x+1][y]:
                Visited[x+1][y] = False
                Q.append((x+1,y))
                

        if check(x,y-1) and M[x][y-1] >= T:
            if Visited[x][y-1]:
                Visited[x][y-1] = False
                Q.append((x,y-1))

        if check(x,y+1) and M[x][y+1] >= T:
            if Visited[x][y+1]:
                Visited[x][y+1] = False
                Q.append((x,y+1))
                
    return False
