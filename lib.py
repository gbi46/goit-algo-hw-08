def min_value_node(node):
    """
    Given a non-empty binary search tree, return the node with the minimum key.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current

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
