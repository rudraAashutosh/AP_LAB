# Q-3. Given a binary tree and an integer k, the task is to count the number of paths in the tree such that the 
# sum of the nodes in each path equals k. A path can start from any node and end at any node and must be downward only
count = 0
target = 1
def findsum(node,curr_sum):
    if(curr_sum==target):
        count +=1
        if(node is None):
            return 0
        findsum(node.left,node.val)
        findsum(node.right,node.val)  
        return 
    else:
        if(node is None):
            return 0
        findsum(node.left,curr_sum+node.val)
        findsum(node.left,node.val)
        findsum(node.right,curr_sum+node.val)
        findsum(node.right,node.val)

def main():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def count_paths_with_sum(root, target_sum):
        global count, target
        count = 0
        target = target_sum
        findsum(root, 0)
        return count

    # Example usage:
    if __name__ == "__main__":
        # Construct the binary tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        target_sum = 7
        result = count_paths_with_sum(root, target_sum)
        print(f"Number of paths with sum {target_sum}: {result}")
        
if __name__ == "__main__":
    main()
