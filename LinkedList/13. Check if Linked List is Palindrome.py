# 13. Check if Linked List is Palindrome
# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1

def isPalindrome(head):
    # Code here
    ans=[]
    
    temp=head
    while temp!=None:
        ans.append(temp)
        temp=temp.next
    
    temp=head
    for i in range(len(ans)):
        if ans.pop().data!=temp.data:
            return 0
        temp=temp.next
    return 1