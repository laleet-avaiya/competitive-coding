# 1. Finding middle element in a linked list 
# https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1


# node => data, next

def findMid(head):
    # Code here
    count=0
    temp = head
    
    while temp != None:
        count=count+1
        temp=temp.next
        
    if count%2!=0:
        for i in range(0,(count-1)//2):
            head=head.next
    else:
        for i in range(0,(count-1)//2 + 1):
            head=head.next
            
    return head
