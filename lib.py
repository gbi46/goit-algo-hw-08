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

def sum_tree(root):
    """
    Iteratively compute the sum of all values in a BST/AVL.
    Supports nodes that store payload in `key` (AVL) or `val` (BST).
    Returns 0 for an empty tree.
    """
    if root is None:
        return 0

    total = 0
    stack = [root]

    while stack:
        node = stack.pop()

        # Extract value regardless of node type
        if hasattr(node, "key"):
            total += node.key
        elif hasattr(node, "val"):
            total += node.val
        else:
            raise AttributeError("Unsupported node type: missing 'key' or 'val'.")

        # Push children for DFS traversal
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return total
