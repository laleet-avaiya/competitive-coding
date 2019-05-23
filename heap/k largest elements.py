# k largest elements 
# https://practice.geeksforgeeks.org/problems/k-largest-elements/0

import heapq

t = int(input())
while t>0:
    t-=1
    n,k = map(int,input().split())
    a=list(map(int,input().split()))
    
    heapq.heapify(a)
    a = list(heapq.nlargest(k,a,key=None))
    for i in a:
        print(i,end=" ")
    print()
