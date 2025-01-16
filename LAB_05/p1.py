class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def mirror(root):
    stack = [root]
    while stack:
        ele = stack.pop()
        if ele:
            temp = ele.right
            ele.right = ele.left
            ele.left = temp
            stack.append(ele.left)
            stack.append(ele.right)


root = Node(10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 20)

print("Inorder traversal of the original tree:")
inorder(root)
print()

mirror(root)

print("Inorder traversal of the mirrored tree:")
inorder(root)
print()