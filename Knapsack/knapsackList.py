def knapsack(W, P, maxW,Q):
    F = [None]*len(W)
    Q = [0]*(maxW + 1)
    # Q - array that holds information about which product was taken

    for i in range(len(W)):
        F[i] = [0] * (maxW + 1)

    for w in range(W[0], maxW + 1):
        F[0][w] = P[0]

    for i in range(1, len(W)):
        for w in range(1, maxW + 1):
            F[i][w] = F[i-1][w]
            tmp = F[i][w]
            if W[i] <= w:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]]+P[i])
            if F[i][w] != tmp:
                Q[i] = i
            else:
                Q[i] = Q[i-1] 
    l = []
    i = len(maxW)
    while i >= 0:
       if Q[i] == 0:
            return l

        l.append(Q[i])
        i -= W[Q[i]]  
    return l

