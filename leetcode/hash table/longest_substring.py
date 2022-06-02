'''
3. Longest Substring Without Repeating Characters
2nd June 2022
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Laleet Avaiya
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        map = {}
        startIndex = 0
        maxLength = 0

        for i in range(len(s)):
            char = s[i]

            if char in map:
                currentLength = i - startIndex
                maxLength = max(maxLength, currentLength)

                newStartIndex = map[char] + 1

                while startIndex != newStartIndex:
                    del map[s[startIndex]]
                    startIndex += 1
            elif i == len(s)-1:
                currentLength = i - startIndex + 1
                maxLength = max(maxLength, currentLength)

            map[char] = i

        return maxLength