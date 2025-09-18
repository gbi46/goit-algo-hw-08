def get_node_value(node):
    """
    Return the value stored in a node (supports BST with 'val' or AVL with 'key').
    Returns None if the given node itself is None.
    """
    if node is None:
        return None
    if hasattr(node, "val"):
        return node.val
    if hasattr(node, "key"):
        return node.key
    return None

def get_find_min_node(root):
    """
    Return the left-most (minimum) node in a BST/AVL, or None if tree is empty.
    Works with nodes that expose `left` and store the payload either in
    `val` (BST) or `key` (AVL).
    """
    if root is None:
        return None

    current = root
    while getattr(current, "left", None) is not None:
        current = current.left
    return current
