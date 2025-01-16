def mirror(root):
    stack = [root]
    while(stack):
        ele = stack.pop()
        temp = ele.right
        ele.right = ele.left
        ele.left = temp
        if(ele.left):
            stack.append(ele.left)
        if(ele.right):
            stack.append(ele.right)