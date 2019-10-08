# Count the numbers
# 17 July 2019
# https://practice.geeksforgeeks.org/problems/count-the-numbers/0

for _ in range(int(input())):
    n = int(input())
    a = set(["1","2","3","4","5"])
    ans = 0
    for j in range(1,n+1):
        p = set(list(str(j)))
        flag = 0
        for i in p:
            if i not in a:
                flag = 1
                
        if flag!=1:
            ans += 1
            
    print(ans)