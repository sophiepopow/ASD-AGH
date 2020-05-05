#Dane jest n zmiennych x1, …, xn, o nieznanych wartościach.
#Mamy jednak podaną serię równości i różności, postaci: xi=xj, xi!=xj.
#Podaj jak najszybszy algorytm, który sprawdzi, czy podana tak seria nie jest sprzeczna.

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

def isSeriesCorrect(equal, notEqual):

    #lets assume that we are given array of tuples that are equal and second array of tuples that are not equal

    for (x,y) in equal:
        Union(x,y)
    
    for (x,y) in notEqual:
        if findSet(x) == findSet(y):
            return false

    return true

equal = [(x1,x2), (x2,x4)]
notEqual = [(x1,x3), (x3,x4)]