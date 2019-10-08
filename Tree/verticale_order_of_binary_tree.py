# Print Binary Tree Vertical order

class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def print_verticle_tree(node,hd,m):
    if node is None:
        return

    
    if hd in m:
        m[hd].append(str(node.data))
    else:
        m[hd]=[str(node.data)]

    print_verticle_tree(node.left,hd-1,m)
    print_verticle_tree(node.right,hd+1,m)


if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    root.right.left.right = Node(8) 
    root.right.right.right = Node(9)

    m = dict() 
    print_verticle_tree(root,0,m)
    print(m)
    for i in sorted(m):
        print(' '.join(m[i]))