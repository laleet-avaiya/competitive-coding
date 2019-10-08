# Find whether path exist 
# https://practice.geeksforgeeks.org/problems/find-whether-path-exist/0

#code
import numpy as np


def DFS(G,i,j,N,M):
    global c
    
    if i<0 or j<0 or i>=N or j>=M or G[i][j]==0:
        return
    
    if G[i][j]==2:
        c += 1
        G[i][j]=0
        return
    
    G[i][j]=0
    
    DFS(G,i-1,j,N,M);
    DFS(G,i,j+1,N,M);
    DFS(G,i+1,j,N,M);
    DFS(G,i,j-1,N,M);

    
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    G = np.reshape(a, (-1, n))
    # print(G[1][1])
    c=0
    for i in range(n):
        for j in range(n):
            if G[i][j]==1:
                G[i][j]==2
                DFS(G,i,j,n,n)
                
    print(c)