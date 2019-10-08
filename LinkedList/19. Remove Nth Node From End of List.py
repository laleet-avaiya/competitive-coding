# 19. Remove Nth Node From End of List
# 04 June 2019
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        size = 0
        while temp != None:
            temp = temp.next
            size += 1
        
        if size == 1 and n==1:
            head = None
            return head
        
        if size-n ==0:
            return head.next
        
        # print(size)
        temp = head
        for i in range(size-n-1):
            temp =temp.next
        
        if temp.next:
            temp.next=temp.next.next
        else:
            temp.next = None
        
        return head
        