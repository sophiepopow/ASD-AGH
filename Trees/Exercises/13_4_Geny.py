from enum import Enum

class Name(Enum):
    A = 1
    C = 2
    G = 3
    T = 4
    
class TreeNode:
    def __init__(self,parent, count = 0):
        self.count = 0
        self.kid1 = None
        self.kid2 = None
        self.kid3 = None
        self.kid4 = None
        
class Tree:
    def __init__(self):
        self.root = TreeNode()
        
    def add(self, genomeString):

        curr = self.root

        for nuclobase in genomeString:
            if Name(nuclobase) == 1:
                if not curr.kid1:
                    curr.kid1 = TreeNode()
                curr = curr.kid1
            elif Name(nuclobase) == 2:
                if not curr.kid2:
                    curr.kid2 = TreeNode()
                curr = curr.kid2
            elif Name(nuclobase) == 3:
                if not curr.kid3:
                    curr.kid3 = TreeNode()
                curr = curr.kid3
            else:
                if not curr.kid4:
                    curr.kid4 = TreeNode()
                curr = curr.kid4

        if curr.count == 1:
            return False
        curr.count = 1
        return True
        
    
def isGenomeOk(array):
    tree = Tree()
    for genomeString in input_string:
        if not tree.add(genomeString):
            print("false")
    print('true')
    

    

