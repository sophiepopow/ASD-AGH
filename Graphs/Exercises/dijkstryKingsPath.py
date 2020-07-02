
inf = float("inf")

def kings_path(A):
    Q =[]
    n = len(A)
    Visited = [[False for x in range(n)] for y in range(n)]
    Cost = [[inf for x in range(n)] for y in range(n)]

    x = 0
    y = 0
    Visited[x][y] = True
    Cost[x][y] = A[x][y]
    Q.append((x,y))
    
    while Q:

        x,y = Q.pop(0)

        if y+1 < n:
            if not Visited[x][y+1]:
                Q.append((x,y+1))
                Visited[x][y+1] = True
            if Cost[x][y+1] > Cost[x][y] + A[x][y+1]:
                Cost[x][y+1] = Cost[x][y] + A[x][y+1]

        if x+1 < n:
            if not Visited[x+1][y]:
                Q.append((x+1,y))
                Visited[x+1][y] = True
            if Cost[x+1][y] > Cost[x][y] + A[x+1][y]:
                Cost[x+1][y] = Cost[x][y] + A[x+1][y]

        if x-1 >= 0:
            if not Visited[x-1][y]:
                Q.append((x-1,y))
                Visited[x-1][y] = True
            if Cost[x-1][y] > Cost[x][y] + A[x-1][y]:
                Cost[x-1][y] = Cost[x][y] + A[x-1][y]

        if y-1 >= 0:
            if not Visited[x][y-1]:
                Q.append((x,y-1))
                Visited[x][y-1] = True
            if Cost[x][y-1] > Cost[x][y] + A[x][y-1]:
                Cost[x][y-1] = Cost[x][y] + A[x][y-1]

    print(Cost)
    return Cost[n-1][n-1]

A = [[1,1,2], [5,1,3], [4,1,1]]
print( kings_path( A ) ) # wypisze 5
