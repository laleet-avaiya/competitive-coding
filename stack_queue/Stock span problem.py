# Stock span problem 
# https://practice.geeksforgeeks.org/problems/stock-span-problem/0

# O(n^2)

t=int(input())
while t>0:
    t-=1
    n = int(input())
    c=list(map(int,input().split()))
    a=[1]*n
    for i in range(1,n):
        temp = 0
        if c[i]<c[i-1]:
            a[i]=1
        else:
            j=i-1
            while c[i] >= c[j] and j>-1:
                temp += 1
                j -= 1
            a[i]+=temp
    
    for i in a:
        print(i,end=" ")
    print("")





# O(n)

#code

def Test(arr):
    
    s=[]
    s.append(0)
    a=[1]*len(arr)
    
    for i in range(1,len(arr)):
        
        while len(s)>0 and arr[i]>=arr[s[-1]]:
            s.pop()
            
        if len(s)==0:
            a[i]=i+1 
        else:
            a[i]=i-s[-1]
        
        s.append(i)
    
    return a
    
t=int(input())
while t>0:
    t-=1
    n = int(input())
    c=list(map(int,input().split()))
    a = Test(c)
    
    for i in a:
        print(i,end=" ")
    print("")