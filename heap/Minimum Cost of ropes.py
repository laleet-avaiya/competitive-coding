# Minimum Cost of ropes 
# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0


#code
import heapq

t = int(input())
while t>0:
    t-=1
    n = int(input())
    a=list(map(int,input().split()))
    ans = 0
    heapq.heapify(a)
    while len(a)>1:
        p=heapq.heappop(a)
        q=heapq.heappop(a)
        ans = ans + p + q
        heapq.heappush(a,p+q)
    
    print(ans)
    