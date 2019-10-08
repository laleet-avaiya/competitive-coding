# Merge k Sorted Arrays
# https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1

import heapq

def mergeKArrays(arr, n):
    # Code here
    a=[]
    for i in arr:
        a = list(heapq.merge(a,i))
        
    return a
