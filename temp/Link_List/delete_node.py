class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def print_Linklist(head):
	temp=head
	while temp.next!=None:
		print(temp.data,end=' ')
		temp=temp.next

def delete_node(head,n):
	temp=head
	prev=temp
	while temp.next!=None and temp.data!=n:
		prev=temp
		temp=temp.next

	prev.next=temp.next


if __name__ == '__main__':
	head=Node(1)
	head.next=Node(2)
	head.next.next=Node(3)
	head.next.next.next=Node(4)
	head.next.next.next.next=Node(5)
	head.next.next.next.next.next=Node(6)
	print_Linklist(head)
	# delete node 3
	delete_node(head,3)
	print('')
	print_Linklist(head)

