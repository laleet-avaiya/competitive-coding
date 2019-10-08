class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def printNode(node):
    print(node.data)

def insert_Node(root,node):
    if root is None:
        root=node
        return
    else:
        if node.data<root.data:
            if root.left is None:
                root.left=node
            else:
                insert_Node(root.left,node)
        if node.data>root.data:
            if root.right is None:
                root.right=node
            else:
                insert_Node(root.right,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')

def levelorder(root):
    q=[]
    q.append(root)

    while len(q)!=0:

        temp=q.pop(0)
        print(temp.data,end=' ')

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def preorder_without_recursion(root):
    q=[]
    if root:
        q.append(root)
        while len(q)!=0:
            temp=q.pop(0)
            print(temp.data,end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
    else:
        return

def inorder_without_recursion(root):
    s=[]
    current=root
    done=0

    while(not done): 
          
        if current is not None: 
            s.append(current) 
            current = current.left  
  
        else: 
            if(len(s) >0 ): 
                current = s.pop() 
                print(current.data,end=" ")
                current = current.right  
  
            else: 
                done = 1



def reverseLevelOrder(root):
    q=[]
    s=[]
    q.append(root)

    while len(q)!=0:

        temp=q.pop(0)
        s.append(temp.data)
        # print(temp.data,end=' ')

       
        if temp.right:
            q.append(temp.right)

        if temp.left:
            q.append(temp.left)

    while len(s)>0:
        print(s.pop(),end=' ')


def nth_node_of_inorder(root,n):
    s=[]
    current=root
    done=0
    count=0
    fount=0

    while(not done): 
          
        if current is not None: 
            s.append(current) 
            current = current.left  
  
        else: 
            if(len(s) >0 ): 
                current = s.pop()
                if count==n:
                    print(current.data,end=" ")
                    fount=1
                    break
                count+=1
                current = current.right  
  
            else: 
                done = 1
    if fount==0:
        print("Given Node number Not Found")
    

def printLevelOrderbyLine(root):
    q=[]
    q.append(root)

    while len(q)!=0:
        nodecount=len(q)
        while nodecount>0:

            temp=q.pop(0)
            print(temp.data,end=' ')

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            nodecount-=1
        print()


root=Node(5)
insert_Node(root,Node(4))
insert_Node(root,Node(6))
insert_Node(root,Node(10))
insert_Node(root,Node(1))

# Tree

#         5
#     4       6
# 1             10

print("Tree Traversal With Recursion:\n")

print("---DFS OF BST---\n ")
print("In Order:")
inorder(root)
print("\nPre Order:")
preorder(root)
print("\nPost Order:")
postorder(root)
print()

print("\n---BFS OF BST---")
print("\n level Order:")
levelorder(root)
print()


print("\nTree Traversal Without Recursion:\n")


print("---DFS OF BST---\n ")
print("In Order:")
inorder_without_recursion(root)
print("\nPre Order:")
preorder_without_recursion(root)
print("\nPost Order:")
postorder(root)
print()


print("\n Revese level Order:")
reverseLevelOrder(root)


print("\n \nFind n-th node of inorder traversal:")
nth_node_of_inorder(root,0)


print("\n \nPrint level order traversal line by line:")
printLevelOrderbyLine(root)