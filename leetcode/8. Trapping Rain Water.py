class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxArr = []

        stack = []
        for a in height:
            if len(stack) == 0:
                stack.append(a)
                leftMaxArr.append(0)
            else:
                leftMaxArr.append(stack[-1])
                if stack[-1] < a:
                    while len(stack) > 0 and stack[-1] < a:
                        stack.pop()
                    stack.append(a)

        rightMaxArr = [0] * len(height)
        stack = []

        for i in range(len(height) - 1, -1, -1):
            if len(stack) == 0:
                stack.append(height[i])
                rightMaxArr[i] = 0
            else:
                rightMaxArr[i] = stack[-1]
                if stack[-1] < height[i]:
                    while len(stack) > 0 and stack[-1] < height[i]:
                        stack.pop()
                    stack.append(height[i])

        ans = 0
        for i in range(len(height)):
            if (min(leftMaxArr[i], rightMaxArr[i]) - height[i]) > 0:
                ans += (min(leftMaxArr[i], rightMaxArr[i]) - height[i])

        return ans
