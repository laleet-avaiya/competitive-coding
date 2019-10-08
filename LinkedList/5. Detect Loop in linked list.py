5. Detect Loop in linked list 
https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1


def detectLoop(head):
    # code here
    ans=[]
    temp=head
    while temp!=None:
        if temp in ans:
            return True
        ans.append(temp)
        temp=temp.next
    
    return False  