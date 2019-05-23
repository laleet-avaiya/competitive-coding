class Node():
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList():
	"""docstring for LinkedList"""
	head = Node(None)
	
	def insert(self,data):
		temp = self.head
		if temp==None:
			self.head = Node(data)
			return
		else:
			while temp.next!=None:
				temp=temp.next
		temp.next=Node(data)
		
l = LinkedList()
l.insert(5)
print(l.head.data)
