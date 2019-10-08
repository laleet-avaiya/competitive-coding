# Leaders in an array 
# https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

#code


t=int(input())
while t>0:
    flag=0
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    
    ans=[-1]*n
    ans[n-1]=a[n-1]
    maximum=a[n-1]
    for i in range(1,n):
        if a[n-1-i]>=ans[n-i] and a[n-1-i]>=maximum:
            ans[n-1-i]=a[n-1-i]
            maximum=a[n-1-i]
            
    for i in ans:
        if i !=-1:
            print(i,end=" ")
    print()