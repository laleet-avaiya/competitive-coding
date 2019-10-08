# 11. Reverse array in groups 
# https://practice.geeksforgeeks.org/problems/reverse-array-in-groups/0

# Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.


#code
t=int(input())
while t>0:
    
    t=t-1
    n,k=(input().split())
    n=int(n)
    k=int(k)
    
    a=list(map(int,input().split()))
    for i in range(0,n-(n%k),k):
    	left = i;
    	right = i+k-1;
    	
    	while left<right:
    	    temp=a[right]
    	    a[right]=a[left]
    	    a[left]=temp
    	    left=left+1
    	    right=right-1
    	    
    left=n-(n%k)
    right=n-1	
    
    
    while left<right:
	    temp=a[right]
	    a[right]=a[left]
	    a[left]=temp
	    left=left+1
	    right=right-1
	    
    for i in a:
        print(i,end=" ")