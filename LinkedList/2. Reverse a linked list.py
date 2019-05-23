# 2. Reverse a linked list 
# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1

def reverseList(self):
    # Code here
    if self.head is None:
        return None
    
    stack=[]
    
    temp=self.head
    
    while temp != None:
        stack.append(temp.data)
        temp=temp.next
        
    temp=self.head
    while temp != None:
        temp.data = stack.pop()
        temp=temp.next
    return self.head