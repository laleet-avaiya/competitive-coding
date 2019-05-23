# Tree View

# 1. Top View
# 2. Right View
# 3. Bottom View
# 4. Left View

# Node Class

class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


# Top View

def top_view(root):
	dist_from_root=dict()
	top_view_Util(root,0,dist_from_root)
	for i in sorted(dist_from_root):
		print(dist_from_root[i],end=' ')


def top_view_Util(nodes,distance,distance_dict):
	q=[]
	q.append([nodes,distance])
	while len(q)!=0:
		temp=q.pop(0)
		node=temp[0]
		distance=temp[1]

		if distance not in distance_dict:
			distance_dict[distance]=node.data
		if node.left:
			q.append([node.left,distance-1])
		if node.right:
			q.append([node.right,distance+1])




# Right View

def right_view(root):
	pass


def bottom_view(root):
	m = dict()
	bottomview(root,0,m)
	for i in sorted(m):
		print(' '.join(m[i]),end=' ')



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

def left_view(root, level, max_level): 
      
    # Base Case 
    if root is None: 
        return
  
    # If this is the first node of its level 
    if (max_level[0] < level): 
        print("%d" %(root.data),end=' ') 
        max_level[0] = level 
  
    # Recur for left and right subtree 
    left_view(root.left, level+1, max_level) 
    left_view(root.right, level+1, max_level)




if __name__ == '__main__':

		# 		20
		# 	8		22

		# 5		3		25
		# 	10		14

	root=Node(20)
	root.left=Node(8)
	root.right=Node(22)
	root.left.left=Node(5)
	root.left.right=Node(3)
	
	root.right.right=Node(25)
	root.left.right.left=Node(10)
	root.left.right.right=Node(14)

	print("\nTop View of Binary Tree:")
	top_view(root)


	print("\nRight View of Binary Tree:")
	right_view(root)


	print("\nBottom View of Binary Tree:")
	bottom_view(root)


	print("\nLeft View of Binary Tree:")
	left_view(root,1,max_level = [0])

	print("\n")