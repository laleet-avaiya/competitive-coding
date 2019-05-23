# 7. Nth node from end of linked list 
# https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

def getNthFromLast(head, n):
    # Code here
    ans=[]
    
    temp=head
    while temp!=None:
        ans.append(temp)
        temp=temp.next
    
    for i in range(n-1):
        if (len(ans)==0):
            return -1
        ans.pop()
    ans_data=ans.pop()
    return ans_data.data