dia = 0
def calc_diameter(root):
    if(root==None):
        return 0
    left = calc_diameter(root.left)
    right = calc_diameter(root.right)
    dia = max(1+left+right)
    return max(1+left,1+right)