# Missing number in array
# https://practice.geeksforgeeks.org/problems/missing-number-in-array/0


#code

t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    total=n*(n+1)/2
    for i in a:
        total=total-i
    print(int(total))