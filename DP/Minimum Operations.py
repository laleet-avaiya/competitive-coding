# Minimum Operations
# https://practice.geeksforgeeks.org/problems/find-optimum-operation/0

def minimumOpearion(n):
    if ans[n]:
        return ans[n]
        
    if n%2==0:
        return 1 + minimumOpearion(n//2)
    else:
        return 2 + minimumOpearion(n//2)
    
for _ in range(int(input())):
    n = int(input())
    ans=[False]*10000
    
    ans[1]=1
    ans[2]=2
    ans[3]=3
    

    ans[n] = minimumOpearion(n)
    
    print(ans[n])