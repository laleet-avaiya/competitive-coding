# Is Binary Tree Heap
# https://practice.geeksforgeeks.org/problems/is-binary-tree-heap/1

def isHeap(tree):
    #Code Here
    if(tree==None):
        return True
    if(tree.left!=None and tree.data<tree.left.data):
       return False
    if(tree.right!=None and tree.data<tree.right.data):
       return False
    return isHeap(tree.left) and isHeap(tree.right)