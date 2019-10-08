# Drive the car 
# https://practice.geeksforgeeks.org/problems/drive-the-car/0


#code
t=int(input())
while t>0:
    t -= 1
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans = 0
    for i in a:
        if i<=k:
            continue
        else:
            ans = ans + i - k
            k += i-k
    
    if ans == 0:
        print(-1)
    else:
        print(ans)
        
