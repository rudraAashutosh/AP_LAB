def check(root):
    if(root.left==None and root.right==None):
        return True
    lef = 0 if root.left==None else root.left.val
    rig = 0 if root.right==None else root.right.val
    if(root.val != (lef+rig)):
        return False
    return check(root.left) and check(root.right)