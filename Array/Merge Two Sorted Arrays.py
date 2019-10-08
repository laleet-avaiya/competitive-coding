# Merge Two Sorted Arrays 
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0


#code
t = int(input())
while t>0:
    
    t=t-1
    n1,n2 = input().split()
    
    n1=int(n1)
    n2=int(n2)
    
    a1 = list(map(int,input().split()))
    a2 = list(map(int,input().split()))
    
    ans=[0]*(n1+n2)
    
    i=0
    j=0
    z=0
    
    while i!=n1 and j!=n2:
        if a1[i]<a2[j]:
            ans[z]=a1[i]
            i += 1
        else:
            ans[z]=a2[j]
            j += 1
        
        z += 1
            
    while i!=n1:
        ans[z]=a1[i]
        i += 1
        z += 1
        
    while j!=n2:
        ans[z]=a2[j]
        j += 1
        z += 1
        
    
    for i in ans:
        print(i,end=" ")
    print("")
    