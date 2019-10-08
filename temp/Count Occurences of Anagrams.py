# Count Occurences of Anagrams 
# 04 Aug. 2019
#  https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams/0

for Testcases in range(int(input())):
    s = list(input())
    p = list(input())

    n = len(s)
    m = len(p)

    pf = [0] * 256

    ans = 0

    for i in range(m):
        pf[ord(p[i])] += 1


    for j in range(n-m+1):
        temp = [0] * 256
        for l in range(j,j+m):
            temp[ord(s[l])] += 1

        if temp==pf:
            ans += 1

    print(ans)
