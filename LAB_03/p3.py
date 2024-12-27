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