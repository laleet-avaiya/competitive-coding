# Maximum distinct elements after removing K elements
# https://practice.geeksforgeeks.org/problems/maximum-distinct-elements-after-removing-k-elements/0

#code
def maxDistinctElmnts(n,k,arr):
    listAsSet = set()
    for num in arr:
        if num in listAsSet:
            k -=1
        else:
            listAsSet.add(num)
    if k <= 0:
        print(len(listAsSet))
    else:
        print(len(listAsSet) - k)

T = int(input())
for _ in range(T):
    n, k = (int(num) for num in input().strip().split())
    arr = [int(data) for data in input().strip().split()]
    maxDistinctElmnts(n,k,arr)