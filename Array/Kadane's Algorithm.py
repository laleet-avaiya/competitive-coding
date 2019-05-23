# Kadane's Algorithm 
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0


#code

t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    y=-999999999999
    for i in range(0,len(a)):
        x= x + a[i]
        if y<x:
            y=x
        
        if x<0:
            x=0
    
    print(y)