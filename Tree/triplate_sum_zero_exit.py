import itertools as it

class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def inorder(root,q):
	if root:
		inorder(root.left,q)
		q.append(root.data)
		inorder(root.right,q)

if __name__ == '__main__':
	root=Node(20)
	root.left=Node(8)
	root.right=Node(22)
	root.left.left=Node(5)
	root.left.right=Node(-20)
	
	root.right.right=Node(0)
	root.left.right.left=Node(1)
	root.left.right.right=Node(14)
	q=[]
	inorder(root,q)
	print(q)
	for i in list(it.permutations(q,3)):
		if sum(i)==0:
			print(True)
			break
	

