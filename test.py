from avl_node import insert_avl
from lib import get_min_node_value

print("=== AVL Tree Example ===")
root = None
values_to_insert = [10, 20, 5, 8, 3, 4, 1]
for value in values_to_insert:
    root = insert_avl(root, value)
    print(f"Inserted {value} into AVL Tree.")
    print(root)
    print("Min node value:", get_min_node_value(root))
