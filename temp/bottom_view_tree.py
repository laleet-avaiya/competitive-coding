class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def inorder(root):
	if root is None:
		return
	inorder(root.left)
	print(root.data,end=' ')
	inorder(root.right)

def bottomview(root,hd,m):

	q=[]
	q.append([root,hd])

	while len(q)!=0:

		temp=q.pop(0)
		node=temp[0]
		hd=temp[1]

		m[hd]=[str(node.data)]

		if node.left:
			q.append([node.left,hd-1])

		if node.right:
			q.append([node.right,hd+1])

def leftViewUtil(root, level, max_level): 
      
    # Base Case 
    if root is None: 
        return
  
    # If this is the first node of its level 
    if (max_level[0] < level): 
        print("%d" %(root.data),end=' ') 
        max_level[0] = level 
  
    # Recur for left and right subtree 
    leftViewUtil(root.left, level+1, max_level) 
    leftViewUtil(root.right, level+1, max_level)



if __name__ == '__main__':
	root=Node(20)
	root.left=Node(8)
	root.right=Node(22)
	root.left.left=Node(5)
	root.left.right=Node(3)
	
	root.right.right=Node(25)
	root.left.right.left=Node(10)
	root.left.right.right=Node(14)

	m = dict()
	bottomview(root,0,m)
	for i in sorted(m):
		print(' '.join(m[i]),end=' ')

	print('')
	leftViewUtil(root,1,max_level = [0])