# 3. Rotate a Linked List 
# https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1


def rotateList(head, k):
    # code here
    
    node_data=[]
    temp=head
    
    while temp!=None:
        node_data.append(temp.data)
        temp = temp.next
    
   
    n=len(node_data)
    while k>0:
        k=k-1
        temp=node_data[0]
    
        for i in range(0,n-1):
            node_data[i]=node_data[i+1]
            
        node_data[n-1]=temp
    i=0
    temp=head
    
    while temp!=None:
        temp.data=node_data[i]
        temp = temp.next
        i=i+1
        
    return (head)