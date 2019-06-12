class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

def iterativePreorder(root):
	if not root:
		return 
	else:
		s=[]
		s.append(root)
		while len(s) != 0:
			node = s.pop()
			
			print(node.data)

			if node.right:
				s.append(node.right)
			
			if node.left:
				s.append(node.left)

def preorder(root):
	if root:
		print(root.data)
		preorder(root.left)
		preorder(root.right)

def inStack(root):
	if not root:
		return
	else:
		s=[]
		while True:
			while root != None:
				s.append(root)
				root=root.left

			if len(s)==0:
				return

			a = s.pop()
			print(a.data)
			root = a.right



def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.data)


def levelorder(root):
	if not root:
		return
	else:
		q=[]
		q.append(root)
		while len(q)!=0:
			node =q.pop(0)
			print(node.data)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)


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

	levelorder(root)