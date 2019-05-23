# Maximize âˆ‘arr[i]*i of an Array 
# https://practice.geeksforgeeks.org/problems/maximize-arrii-of-an-array/0


#code
t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(n):
        ans+=i*a[i]
    print(ans%(10**9+7))

   