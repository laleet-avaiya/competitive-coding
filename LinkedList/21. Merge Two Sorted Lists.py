# 21. Merge Two Sorted Lists
# 04 June 2019
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp1 = l1
        temp2 = l2
        ans = ListNode(0)
        temp = ans
        
        while l1!=None and l2 !=None:
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
                
        while l1!=None:
            temp.next = ListNode(l1.val)
            temp = temp.next
            l1 = l1.next
        
        while l2!=None:
            temp.next = ListNode(l2.val)
            temp = temp.next
            l2 = l2.next

        return ans.next
                
            
            
