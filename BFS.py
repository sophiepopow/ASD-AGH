
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def put(self, v):
        N = Node(v)
        if self.front is None:
            self.front = N
            self.back = N
            self.front.next = None
        else:
            self.back.next = N
            self.back = N        
    def get(self):
        tmp = self.front
        if not self.isEmpty():
            self.front = self.front.next  
        return tmp 
    def isEmpty(self):
        return self.front is None
    

def BFS(G,s):
    Q = Queue()
    results = [None]*len(G)
    visited = [False]*len(G)

    results[s]=(None,0)
    visited[s] = True

    Q.put(s)

    while not Q.isEmpty():
        u = Q.get().val

        for i in range(len(G)):
            if G[u][i] == 1 and visited[i] == False:
                visited[i] = True
                results[i] = ((u,results[u][1]+1))

                Q.put(i)

    return results

G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print( BFS(G,0) )