def get_min_node_value(node):
    """
    Return the value stored in a node (supports BST with 'val' or AVL with 'key').
    Returns None if the given node itself is None.
    """
    if node is None:
        return None
    
    current = node
    while current.left:
        current = current.left
    if hasattr(current, "val"):
        return current.val
    if hasattr(current, "key"):
        return current.key
    return None
