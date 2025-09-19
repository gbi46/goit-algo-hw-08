from avl_node import insert_avl

print("=== AVL Tree Example ===")
root = None
values_to_insert = [10, 20, 30, 40, 50, 25]
for value in values_to_insert:
    root = insert_avl(root, value)
    print(f"Inserted {value} into AVL Tree.")
    print(root)
