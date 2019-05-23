# 13. Trapping Rain Water 
# https://practice.geeksforgeeks.org/problems/trapping-rain-water/0

#code

t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    maxi=a[0]
    
    left=[0]*n
    right=[0]*n
    leftmax=0
    rightmax=0
    
    for i in range(0,n):
        left[i]=leftmax
        if a[i]>leftmax:
            leftmax=a[i]
    
    for i in range(0,n):
        right[n-1-i]=rightmax
        if a[n-1-i]>rightmax:
            rightmax=a[n-1-i]
    

    
    ans=0
    for i in range(1,n):
        if a[i]<left[i] and a[i]<right[i]:
            ans=ans+min(left[i],right[i])-a[i]

    print(ans)
        