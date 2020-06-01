class BSTNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

def find(root,key):
    while root != None:
        if root.key == key
            return root
        elif root.key < key:
            root = root.right
        else 
            root = root.left
    return None


def insert(root,key,value):
    while root != None:
        if root.key == key:
            return root
        elif root.key < key:
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