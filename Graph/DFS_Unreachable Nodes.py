# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def DFS(G,s):
    visited[s-1]=1
    for j in range(n):
        if G[s-1][j] == 1 and visited[j]==0:
            DFS(G,j+1);


# Driven Code

nm = input().split()

n=int(nm[0])
m=int(nm[1])
adj = [[0 for i in range(n)] for j in range(n)]
# for i in adj:
#     print(i)    
    
visited = [0]*n
# print(adj)

for i in range(m):
    e = list(map(int,input().split()))
    adj[e[0]-1][e[1]-1]=1
    adj[e[1]-1][e[0]-1]=1


s=int(input())

DFS(adj,s)
# print(visited)

for i in visited:
    if i==1:
        n=n-1

print(n)
# print(visited)

