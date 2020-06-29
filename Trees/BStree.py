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
        while True:
            if root.parent == None:
                return None
            if root.parent.right == None:
                break
            if root.parent.right.key != root.key:
                break
            root = root.parent

        return root.parent

def pred(root):
    if root.left != None:
        root = root.left
        return max(root)
    else:
        while True:
            if root.parent == None:
                return None
            if root.parent.left == None:
                break
            if root.parent.left.key != root.key:
                break
            root = root.parent
        return root.parent

def delete_no_children(node):
    node = None

def deete_one_children(node):
    if node.left != None:
        node.left.parent = node.parent
        node = node.left
    else:
        node.left.parent = node.parent
        node = node.right

def count_child(root):
    c = 0
    if root.left != None:
        c += 1
    if root.right != None:
        c += 1
    
    return c

def delete(root):
    childrens = count_child(root)
    if childrens == 0:
        delete_no_children(root)
        return

    if childrens == 1:
        deete_one_children(root)
        return
    
    # 2 childrens

    succ = succesor(root)

    succ_childrens = count_child(succ)

    tmp_left = succ.left
    tmp_right = succ.right
    tmp_parent = succ.parent

    succ.right = root.right
    succ.left = root.left
    succ.parent = root.parent
    
    

    
    
    

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
print("")
# delete(find(newNode,17))
delete(newNode)
printTree(newNode)


