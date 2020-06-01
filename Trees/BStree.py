class BSTNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

def find(root,key):
    while root != None:
        if root.key == key:
            return root
        elif root.key < key:
            root = root.right
        else:
            root = root.left
    return None

#POPRAWKA
def insert(root,key,value):
    while root != None:
        if root.key < key:
            parent = root
            root = root.right
        else:
            parent = root
            root = root.left

    new = BSTNode()
    new.key = key
    new.value = value

    if key < parent.key:
        parent.left =  new
        new.parent = parent
    else:
        parent.right = new
        new.parent = parent

def min(root):
    while root.left != None:
        root = root.left
    return root

def max(root):
    while root.right != None:
        root = root.right
    return root

def succesor(root):
    if root.right != None:
        root = root.right
        return min(root)
    else:
        if root.parent == None:
            return None
        if root.parent.right == None:
            return root.parent
        while root.parent.right.key == root.key:
            root = root.parent
            if root == None:
                return None
            if root.parent.right == None:
                break

        return root.parent

def pred(root):
    if root.left != None:
        root = root.left
        return max(root)
    else:
        if root.parent == None:
            return None
        if root.parent.left == None:
            return root.parent
        while root.parent.left.key == root.key:
            root = root.parent
            if root == None:
                return None
            if root.parent.left == None:
                break

        return root.parent



def delete(root):
    if not root.right and not root.left:
        parent = root.parent
        if root.key < parent.key:
            parent.left = None
        else:
            parent.right = None
        root = None
    else:
        succ = succesor(root)
        root.key = succ.key
        parent = succ.parent

        if succ.key < parent.key:
            parent.left = None
        else:
            parent.right = None
        succ = None

def printTree(root, message = ""):
    if root == None:
        return 
    k = 0 if root.parent == None else root.parent.key
    print(root.key, k, message)
    printTree(root.left, "left")
    printTree(root.right, "right")


newNode = BSTNode()
newNode.key = 10
newNode.value = 5

insert(newNode, 5, 7)
insert(newNode, 2, 3)
insert(newNode, 4, 8)
insert(newNode, 20, 39)
insert(newNode, 15, 4)
insert(newNode, 25, 3)
insert(newNode, 12, 3)
insert(newNode, 17, 3)
printTree(newNode)

print(succesor(find(newNode, 12)).key)
print(succesor(find(newNode, 10)).key)
print(succesor(find(newNode, 4)).key)
print(succesor(find(newNode, 17)).key)
