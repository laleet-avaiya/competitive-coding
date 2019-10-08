# Subarray with given sum 
# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0


#code

t=int(input())
while t>0:
    t=t-1
    a = list(map(int,input().split()))
    n=a[0]
    ans=a[1]
    arr=list(map(int,input().split()))
    
    total=0
    start=0
    i=0
    
    while total!=ans:
        if i==n:
            print(-1)
            break
        total=total+arr[i]
        if(total>ans):
            total=total-arr[start]-arr[i]
            start=start+1
        elif total==ans:
            print(start+1,i+1)
            break
        else:
            i=i+1

    
    


    
    
