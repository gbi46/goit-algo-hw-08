from avl_node import insert_avl
from binary_node import BinaryNode, insert_bst
from lib import get_min_node_value

from colorama import init, Fore
init(autoreset=True)

def print_task_header(task_number: int):
    print(Fore.GREEN + "=========================")

    for i in range(6):
        if i == 3:
            print(Fore.GREEN + "=" + Fore.YELLOW + " " * 8 + f"Task {task_number}" + Fore.GREEN + " " * 9 + "=")
        else:
            print(Fore.GREEN + "=                       =")
    print(Fore.GREEN + "=========================")

print_task_header(1)
print(Fore.CYAN + "=== AVL Tree Example ===")
root = None
values_to_insert = [10, 20, 5, 8, 3, 4, 1]
for value in values_to_insert:
    root = insert_avl(root, value)
    print(f"Inserted {value} into AVL Tree.")
    print(root)
    print("Min node value:", get_min_node_value(root))

print(Fore.CYAN + "=== Binary Search Tree Example ===")
root = BinaryNode(50)
nodes_to_insert = [30, 20, 40, 70, 60, 80]
for key in nodes_to_insert:
    insert_bst(root, key)
    print(f"Inserted {key} into BST.")
    print(root)
    print("Min node value:", get_min_node_value(root))
