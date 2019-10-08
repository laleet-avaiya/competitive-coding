# Surpasser Count
# 08-10-2019
# https://practice.geeksforgeeks.org/problems/surpasser-count/0


if __name__== "__main__" :
     
    test_cases = int(input())
    
    for _ in range(test_cases):
        n = int(input())
        a = list(map(int,input().split()))
        
        ans = [0]*n
    
        for i in range(n):
            for j in range(i,n):
                if a[i]<a[j]:
                    ans[i] += 1
        
        for p in ans:
            print(p,end=" ")
        
        print("")