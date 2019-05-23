# 12. Kth smallest element 
# https://practice.geeksforgeeks.org/problems/kth-smallest-element/0

#code
from heapq import heapify,heappush,heappop

t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    heapify(a)
    for i in range(k-1):
        heappop(a)
    print(a[0])
    