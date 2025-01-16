def create_node(value):
    return {"value": value, "left": None, "right": None}


def insert_into_bst(root, value):
    if root is None:
        return create_node(value)
    
    if value < root["value"]:
        root["left"] = insert_into_bst(root["left"], value)
    else:
        root["right"] = insert_into_bst(root["right"], value)
    
    return root


def construct_bst(arr):
    root = None
    for value in arr:
        root = insert_into_bst(root, value)
    return root


def inorder(root, k, result):
    if root is None or result[0] >= k:
        return None

    value = inorder(root["right"], k, result)
    if value is not None:
        return value


    result[0] += 1
    if result[0] == k:
        return root["value"]


    return inorder(root["left"], k, result)


def k_largest_element(root, k):
    result = [0]
    return inorder(root, k, result)


arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst_root = construct_bst(arr)
k = 3

print(f"The {k}-th largest element in the BST is:")
largest = k_largest_element(bst_root, k)
print(largest)