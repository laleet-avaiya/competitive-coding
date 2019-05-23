# 20. Kth largest element in a stream 
# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0


#code
from heapq import heapify, heappush, heappop

def k_smallest(arr,k):
    heapify(arr)
    for i in range(k-1):
        heappop(arr)
    return arr[0]
        
    
    
t=int(input())
while t>0:
    t=t-1
    k,n=input().split()
    k=int(k)
    n=int(n)
    a=list(map(int,input().split()))
    ans=[0]*n
    for i in range(n):
        if i<k-1:
            ans[i]=-1
        else:
            ans[i]=k_smallest(a[0:i+1],i+2-k)
        
        
    for i in ans:
        print(i,end=" ")
    print("")
        
        
            
