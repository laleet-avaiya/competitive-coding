# Diameter of Binary Tree 
# https://practice.geeksforgeeks.org/viewSol.php?subId=13580925&pid=700165&user=LaleetAvaiya

def Max(node):
    if node is None:
        return 0
    else:
        return 1 + max(Max(node.left),Max(node.right))
# your task is to complete this function
# function should return the diameter of the tree
def diameter(root):
    # Code here
    return 1 + Max(root.left) + Max(root.right)