from avl_node import insert_avl
from binary_node import BinaryNode, insert_bst
from lib import get_min_node_value, min_cost_cables, print_task_header, sum_tree
from colorama import init, Fore

init(autoreset=True)

print_task_header(1)
print(Fore.CYAN + "=== AVL Tree Example ===")
root_avl = None
values_to_insert = [10, 20, 5, 8, 3, 4, 2]
for value in values_to_insert:
    root_avl = insert_avl(root_avl, value)
    print(f"Inserted {value} into AVL Tree.")
    print(root_avl)
    print("Min node value:", get_min_node_value(root_avl))

print(Fore.CYAN + "=== Binary Search Tree Example ===")
root_bst = BinaryNode(50)
nodes_to_insert = [30, 20, 40, 70, 58, 80]
for key in nodes_to_insert:
    insert_bst(root_bst, key)
    print(f"Inserted {key} into BST.")
    print(root_bst)
    print("Min node value:", get_min_node_value(root_bst))

print_task_header(2)
print(Fore.CYAN + "=== Sum of all values in AVL Tree ===")
avl_sum = sum_tree(root_avl)
print("Sum of all values in AVL Tree:", avl_sum)

print(Fore.CYAN + "=== Sum of all values in BST ===")
bst_sum = sum_tree(root_bst)
print("Sum of all values in BST:", bst_sum)

print_task_header(3)
print(Fore.CYAN + "=== Minimum cost to connect cables ===")
cases = [
    [],
    [5],
    [1, 2],
    [4, 3, 2, 6],
    [8, 4, 6, 12],
    [5, 5, 5, 5, 5],
]

for arr in cases:
    cost = min_cost_cables(arr)
    print(f"Cables = {arr} -> minimal cost = {cost}")
