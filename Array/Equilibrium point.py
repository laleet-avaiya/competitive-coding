# Equilibrium point 
# https://practice.geeksforgeeks.org/problems/equilibrium-point/0

#code

t=int(input())
while t>0:
    flag=0
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    left_sum=[0]*n
    right_sum=[0]*n
    
    for i in range(1,len(a)):
        left_sum[i]=left_sum[i-1]+a[i-1]
    
    for i in range(0,len(a)):
        right_sum[len(a)-2-i]=right_sum[len(a)-1-i]+a[len(a)-1-i]

    for i in range(0,len(a)):
        if(left_sum[i]==right_sum[i]):
            print(i+1)
            flag=1
            break
        
    if flag==0 and len(a)!=1:
        print(-1)
    if len(a)==1:
        print(1)