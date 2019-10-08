# Majority Element 
# 04 June 2019
# https://practice.geeksforgeeks.org/problems/majority-element/0/?track=md-arrays&batchId=144

#code
for i in range(int(input())):
    p=int(input())
    n = list(map(int,input().split()))
    ans = {}
    
    # print(n)
    for i in n:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    
    # print(ans)
    
    final = -1
    for i in ans:
        if ans[i] > len(n)//2:
            final = i
            break
    
    print(final) 
    