# Maximum Tip Calculator 
# 19 June 2019
# https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0


def maximumTip(x,y,order):
    # print(x,y,order)
    if order == N+1:
        return 0
    
    if x==0:
        return B[order-1] + maximumTip(x,y-1,order+1)
    
    if y==0:
        return A[order-1] + maximumTip(x-1,y,order+1)
        
    return max(maximumTip(x-1,y,order+1)+ A[order-1] ,maximumTip(x,y-1,order+1) +  B[order-1])
    
for _ in range(int(input())):
    N,X,Y = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(maximumTip(X,Y,1))
    # print("Done ---")