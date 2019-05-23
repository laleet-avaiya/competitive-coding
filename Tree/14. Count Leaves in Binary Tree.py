# Count Leaves in Binary Tree
# https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1

def countLeaves(root):
    # Code here
    s=[]
    ans = 0
    s.append(root)
    while len(s)!=0:
        node = s.pop()
        if node.left == None and node.right == None:
            ans += 1
        if node.left:
            s.append(node.left)
        if node.right:
            s.append(node.right)
            
    return ans
