# Sort an array of 0s, 1s and 2s
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0


#code

t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    for i in a:
        print(i,end=" ")
    print()