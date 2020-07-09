#(Indeksowane drzewa BST) Rozważmy drzewa BST, które dodatkowo w każdym węź- le zawierają pole z liczbą węzłów w danym poddrzewie. Proszę opisać jak w takim drzewie wykonywać następujące operacje:
# 1. znalezienie i-go co do wielkości elementu,
# 2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł
# Proszę zaimplementować obie operacje.

class BSTreeNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.parent = None
        self.left = None
        self.right = None
        self.leftSize = None
        self.rightSize = None

    def findIthNode(root, i):

        if i == root.leftSize+1:
            return root
        elif i <= root.leftSize:
            findIthNode(root.left, i)
        else:
            findIthNode(root.right, i-root.leftSize-1)

    def nodeSize(root, i):
        x = 1
        while root is not None:
            if root.value == i:
                return x+root.leftSize
            elif i > root.value:
                x += root.leftSize+1
                root = root.right
            else:
                root = root.left
        return None