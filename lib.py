from colorama import init, Fore
from heapq import heapify, heappop, heappush
from typing import List, Tuple

init(autoreset=True)

def print_task_header(task_number: int):
    print(Fore.GREEN + "=========================")

    for i in range(6):
        if i == 3:
            print(Fore.GREEN + "=" + Fore.YELLOW + " " * 8 + f"Task {task_number}" + Fore.GREEN + " " * 9 + "=")
        else:
            print(Fore.GREEN + "=                       =")
    print(Fore.GREEN + "=========================")

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

def min_cost_cables(lengths: List[int]) -> int:
    """
    Compute the minimal total cost of connecting all cables pairwise using a min-heap.
    Each merge of two cables costs the sum of their lengths; the merged cable is reinserted.

    Args:
        lengths: List of cable lengths (non-negative integers).

    Returns:
        Minimal possible total cost to connect all cables into one.
        Returns 0 if there are 0 or 1 cables.
    """
    if len(lengths) <= 1:
        return 0

    # Build a min-heap of lengths
    heap = list(lengths)
    heapify(heap)

    total = 0
    # Keep merging the two smallest until one cable remains
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        cost = a + b
        total += cost
        heappush(heap, cost)

    return total
