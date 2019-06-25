# Twice counter
# 17 June 2019
# https://practice.geeksforgeeks.org/problems/twice-counter/0






# python


for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    
    d = {}
    
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    ans=0
    for i in d:
        if d[i]==2:
            ans +=1
            
    print(ans)
    

  