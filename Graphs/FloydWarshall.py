def FloydWarshall(V,E):
    dp = [[ [] for i in range(V)] for j in range(V)]
    for i in range(V):
        if i == j:
            dp[i][j] = 0
        elif (i,j) in E:
            dp[i][j] = w(i,j)
        else:
            dp[i][j] = float("+inf")

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])