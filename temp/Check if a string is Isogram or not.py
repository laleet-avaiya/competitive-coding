# Check if a string is Isogram or not
# 06 Aug. 2019
# https: // practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not/1


def isIsogram(s):
    # Your code here
    return True if len(s) == len(set(s)) else False
