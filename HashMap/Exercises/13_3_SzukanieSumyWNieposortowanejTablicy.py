#(szukanie sumy w nieposortowanej tablicy)
#Dana jest nieposortowana tablica A[1 . . . n] oraz liczba x.
#Proszę podać algorytm sprawdzający czy istnieją indeksy i oraz j, takie ze A[i] + A[j] = x.


###_________________HashMap:
class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
    
class HashTable:
    def __init__(self, arrLen):
        self.hashTab = [Node() for i in range(2*arrLen)]
        self.N = 2*arrLen
        
    def hash(self, key):
        v = int('0b10101010', 2)
        for l in key:
            v ^= ord(l) % 255
        
        return v % self.N

    def insert(self, key):
        id = self.hash(key)
        for _ in range(self.N):
            if self.hashTab[id].taken:
                id = (id+1)% self.N
            else:
                self.hashTab[id].key = key
                self.hashTab[id].taken = True
                break

    def find(self, key):
        if key == None:
            return None

        id = self.hash(key)
        for _ in range(self.N):
            if not self.hashTab[id].taken:
                return None
            if self.hashTab[id].key == key:
                return id
            id = (id + 1)% self.N
        return None

##________does Sum Exists func:

def doesSumExists(x,array):
    hashTable = HashTable(len(array))
    for i in range(len(array)):
        hashTable.insert(x-array[i])
    for i in range(len(array)):
        if hashTable.find(array[i]):
            return True
    return False

Array = [2,4,6,1,7,9,0,4]

