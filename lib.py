def safe_node_value(node):
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
