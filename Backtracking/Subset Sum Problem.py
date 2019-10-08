# Subset Sum Problem
# https://practice.geeksforgeeks.org/problems/subset-sum-problem/0

def subsum(a, b, n):
    if (b ==0):                         #when sum ==0
        return True
    if (n == 0 and b!=0):               #when elements in list ==0 but sum !=0
        return False
    if (a[n-1] > b ):
        return subsum(a,b, n-1)         #exclude the element if its greater then sum
    return subsum(a,int(b-a[n-1]),n-1) or subsum(a,b, n-1)
    
    
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))  # taking inputs
    if sum(a)%2 == 1:                   #if sum is odd return no
        print ("NO")
    else:
        b = int(sum(a)/2)               #half the sum and search for values recursively
        val = subsum(a,b,n)
        
        if (val == True) : 
            print("YES") 
        else : 
            print("NO") 
        