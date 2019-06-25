# Boundary Traversal of binary tree
# 21 June 2019
# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1



def inorder(node,s):
    if node is None:
        return
    
    inorder(node.left,s)
    if node.left==None and node.right==None:
        s.append(node.data)
    inorder(node.right,s)
        
def printBoundaryView(root):
    # Code here
    
    s = []
    
    # Add Root
    s.append(root.data)
    
    # Left Left Left if left has no left but right then right
    a = root.left
    while a!=None and (a.left != None or a.right !=None):
        s.append(a.data)
        if a.left !=None:
            a = a.left
        else:
            a = a.right
        
    
    
    # Inorder for Leaf Node
    inorder(root,s)
    
    
    
    # right right if right has no right but left then left
    p=[]
    b = root.right
    while b!=None and (b.right !=None or b.left !=None):
        p.append(b.data)
        if b.right !=None:
            b = b.right
        else:
            b = b.left
        
    p.reverse()
    
    # Print Ans
    for i in (s+p):
        print(i,end=" ")
    # print("")