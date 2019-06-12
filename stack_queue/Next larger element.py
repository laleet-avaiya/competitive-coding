# Next larger element
# https://practice.geeksforgeeks.org/problems/next-larger-element/0

#code

t = int(input())
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    
    s = []
    s.append(a[-1])
    ans = [-1]*n
    
    for i in range(n-2,-1,-1):

        while len(s)!=0 and s[-1] <= a[i]:
            s.pop()
        
        if len(s)!=0:
            ans[i] = s[-1]
        else:
            ans[i] = -1
        
        s.append(a[i])
        
    for i in ans:
        print(i,end=" ")
    print("")