# Snake and Ladder Problem
# 26 July 2019
# https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem/0

def BFS(d):
    q=[]
    q.append([1,0])
    
    while len(q)>0:
        a = q.pop(0)
        
        pos = a[0]
        throw = a[1]
        
        if pos == 30:
            return throw
        
        i = pos+1
        while i<31 and i<=pos +6:
            
            if i in d:
                q.append([d[i],throw+1])
            else:
                q.append([i,throw+1])
            
            i+=1
    
    return -1
    
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    d = {}
    for i in range(0,2*n,2):
        d[arr[i]] = arr[i+1]
    
    
    print(BFS(d))
    