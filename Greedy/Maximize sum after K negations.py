# Maximize sum after K negations 
# https://practice.geeksforgeeks.org/problems/maximize-sum-after-k-negations/0

#code
import heapq

t=int(input())
while t>0:
    t-=1
    n,k = input().split()
    n=int(n)
    k=int(k)
    a=list(map(int,input().split()))
    heapq.heapify(a)
    for i in range(k):
        b=heapq.heappop(a)
        heapq.heappush(a,-b)
    
    print(sum(a))