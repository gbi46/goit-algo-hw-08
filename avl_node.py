class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret
    
def height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))

def balance(node):
    return height(node.left) - height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)
    return x

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    update_height(z)
    update_height(y)
    return y

def insert_avl(node, key):
    if not node:
        return AVLNode(key)

    if key < node.key:
        node.left = insert_avl(node.left, key)
    elif key > node.key:
        node.right = insert_avl(node.right, key)
    else:
        return node  # duplicates ignored

    update_height(node)
    bal = balance(node)

    # Rebalance
    if bal > 1 and key < node.left.key:   # LL
        return right_rotate(node)
    if bal > 1 and key > node.left.key:   # LR
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if bal < -1 and key > node.right.key: # RR
        return left_rotate(node)
    if bal < -1 and key < node.right.key: # RL
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
