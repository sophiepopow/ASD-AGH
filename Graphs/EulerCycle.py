
def DFSHelper(G, i, result, cycleStart):

    if i == cycleStart:
        cycleStart = -1
        result.append(i)
        return

    for j in range(len(G)):
        if j in G[i]:
            if cycleStart == -1:
                cycleStart = i
            G[i].remove(j)
            G[j].remove(i)
            DFSHelper(G, j,result, cycleStart)

    result.append(i)
    return result

def findCycle(G):
    result = []
    cycleStart = -1
    return DFSHelper(G, 0,result,cycleStart)


# G = [[1, 5], [0, 2, 6, 5], [1, 3, 4, 6], [2, 4], [2, 3, 5, 6], [0, 1, 4, 6], [1, 2, 4, 5]]
G = [[1, 7], [0, 2, 6, 5], [1, 3, 4, 6], [2, 4], [2, 3, 5, 6], [1, 4, 6, 8], [1, 2, 4, 5], [0, 8], [7, 5]]

print(findCycle(G))