# Love For The Twins
# 06 Aug. 2019
# https://practice.geeksforgeeks.org/problems/love-for-the-twins/0/?ref=self


import collections

for TestCases in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # count Frequency
    p = collections.Counter(arr)
    # convert to dict
    p = dict(p)

    ans = 0
    for i in p:
        ans += p[i]
        ans -= p[i] % 2
    print(ans)
