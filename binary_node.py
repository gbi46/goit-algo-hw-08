class BinaryNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret
    
def insert_bst(root, key):
    if root is None:
        return BinaryNode(key)
    else:
        if key < root.val:
            root.left = insert_bst(root.left, key)
        else:
            root.right = insert_bst(root.right, key)
    return root
