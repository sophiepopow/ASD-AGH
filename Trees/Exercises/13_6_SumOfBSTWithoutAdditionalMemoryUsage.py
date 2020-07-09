class BSTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

    def next(root):

        if root.left:
            return root.left
        elif root.right
            return root.right
        else:
            while is not root.right and root.parent:
                root = root.parent
            return root.right:

    def sum(root):
        sum = 0
        while root:
            sum += root.value
            root = next(root)

        return sum