# 6. Remove loop in Linked List
# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1


def removeTheLoop(head):
    ##Your code here
    ans=[]
    temp=head
    while temp!=None:
        if temp.next in ans:
            temp.next=None
            return 1
        ans.append(temp)
        temp=temp.next
    
    return 0  
    