class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
		
	def insert(self,data):
		if self.head == None:
			self.head = Node(data)
		else:
			temp = self.head
			while temp.next != None:
				temp=temp.next
			temp.next = Node(data)
		self.size += 1

	def delete(self,data):
		temp = self.head
		prev = temp
		if temp.data == data:
			self.head= head.next
		else:
			while temp != None:
				if temp.data == data:
					prev.next= temp.next
					return
				prev=temp
				temp=temp.next

	def update(self,old,newdata):
		if self.head == old:
			self.head.data = newdata
		else:
			temp = self.head
			while temp != None:
				if temp.data == old:
					temp.data = newdata
					break
				temp = temp.next

	def size(self):
		return self.size;

	def printLinkedList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp=temp.next

if __name__ == '__main__':
	l = LinkedList()

	l.insert(5)
	l.insert(5)
	l.insert(4)
	l.delete(4)
	l.update(5,10)
	l.update(5,15)
	l.printLinkedList()

'''
*-----Hackerrank-----*
Print the Elements of a Linked List
Insert a Node at the Tail of a Linked List
Insert a node at the head of a linked list
Insert a node at a specific position in a linked list
Delete a Node
Reverse a linked list
Print in Reverse
Merge two sorted linked lists
Compare two linked lists
Get Node Value
Delete duplicate-value nodes from a sorted linked list
Cycle Detection
Reverse a doubly linked list
Inserting a Node Into a Sorted Doubly Linked List
Find Merge Point of Two Lists

*-----Geeks------*
Nth node from end of linked list
Remove loop in Linked List
Delete without head pointer
Check if Linked List is Palindrome
Finding middle element in a linked list 
Rotate a Linked List
'''











