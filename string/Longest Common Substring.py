Longest Common Substring
13 June 2019
https://practice.geeksforgeeks.org/problems/longest-common-substring/0/?ref=self


for _ in range(int(input())):
    n,m = map(int,input().split())
    a = input()
    b = input()
    
    a=list(a)
    b=list(b)
    
    G = [[0 for i in range(m)]for j in range(n)]
    
    maxi = 0
    
    for i in range(n):
        if a[i]==b[0]:
            G[i][0] = 1
            maxi = G[i][0]
    
    for j in range(m):
        if b[j]==a[0]:
            G[0][j]=1
            maxi = G[0][j]
    
    
    for i in range(1,n):
        for j in range(1,m):
            if a[i]==b[j]:
                G[i][j] = G[i-1][j-1] + 1
                if maxi<G[i][j]:
                    maxi =G[i][j]
    
    print(maxi)
    # for i in G:
    #     print(i)