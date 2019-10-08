# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        
        finalans = ListNode(0)
        ans = finalans
        
        while l1 != None and l2 != None:
            if carry + l1.val + l2.val > 9:
                if carry != 0:
                    ans.next = ListNode(carry + l1.val + l2.val - 10)
                    carry = (carry +l1.val + l2.val)//10
                else:
                    ans.next = ListNode(l1.val + l2.val - 10)
                    carry = (l1.val + l2.val)//10
            else:
                if carry != 0:
                    if carry + l1.val + l2.val > 9:
                        ans.next = ListNode(carry + l1.val +l2.val - 10)
                        carry = (carry + l1.val + l2.val)//10
                    else:
                        ans.next = ListNode(l1.val + l2.val + carry)
                        carry = 0
                else:
                    ans.next = ListNode(l1.val + l2.val)
            
            l1 = l1.next
            l2 = l2.next
            ans = ans.next
            
        while l1 != None:
            if carry != 0:
                if carry + l1.val > 9:
                    ans.next = ListNode(carry + l1.val - 10)
                    carry = (carry + l1.val)//10
                else:
                    ans.next = ListNode(l1.val + carry)
                    carry = 0
            else:
                ans.next = ListNode(l1.val)
            l1 = l1.next
            ans = ans.next
            
        while l2 != None:
            if carry != 0:
                if carry + l2.val > 9:
                    ans.next = ListNode(carry + l2.val - 10)
                    carry = (carry + l2.val)//10
                else:
                    ans.next = ListNode(l2.val + carry)
                    carry = 0
            else:
                ans.next = ListNode(l2.val)
            l2 = l2.next
            ans = ans.next
        
        if carry:
            ans.next = ListNode(carry)
        
        return finalans.next
            
        