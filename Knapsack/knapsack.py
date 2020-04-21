def knapsack(W, P, maxW,Q):
    F = [None]*len(W)
    
    for i in range(len(W)):
        F[i] = [0] * (maxW + 1)

    for w in range(W[0], maxW + 1):
        F[0][w] = P[0]
    for i in range(1, len(W)):
        for w in range(1, maxW + 1):
            F[i][w] = F[i-1][w]
          
            if W[i] <= w:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]]+P[i])
        

    return F[n-1][maxW]


