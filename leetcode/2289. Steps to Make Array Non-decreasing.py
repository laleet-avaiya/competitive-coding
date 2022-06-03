'''
2289. Steps to Make Array Non-decreasing
3rd June 2022

Start: -
End  : -
Total: -

https://www.acwing.com/solution/content/118841/
'''

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res=0
        f = [0]*len(nums)
        st = []
        for i in range(len(nums)):
            cur = 0
            while len(st) != 0 and nums[st[-1]] <= nums[i]:
                cur = max(cur, f[st[-1]])
                st.pop()
            
            if len(st) != 0:
                res = max(res, cur+1)
                f[i] = cur + 1
            
            st.append(i)

        return res