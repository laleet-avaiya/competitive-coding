# Next Greater Node In Linked List
# https://leetcode.com/problems/next-greater-node-in-linked-list/

def nextLargerNodes(self, head: ListNode) -> List[int]:
        a=[]
        
        temp = head
        size = 0
        while temp != None:
            a.append(temp.val)
            temp = temp.next
            size += 1
        
        ans = [0]*size
        s = []
        s.append(a[-1])
        
        for i in range(size-2,-1,-1):

            while len(s)!=0 and s[-1] <= a[i]:
                s.pop()

            if len(s)!=0:
                ans[i] = s[-1]
            else:
                ans[i] = 0

            # print(s)
            s.append(a[i])
            
        return ans