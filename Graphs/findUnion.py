class Node:
    def __init__(self,id):
        self.id = id
        self.parent = self
        self.rank = 0

    def findSet(x):
        if x! = x.parent:
            x.parent = findSet(x.parent)
        return x.parent

    def Union(x,y):
        x = findSet(x)
        y = findSet(y)

        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            
            if x.rank == y.rank:
                y.rank += 1
