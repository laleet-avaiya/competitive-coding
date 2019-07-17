# Topological Sort 
# https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/

# Write your code here
def TopologicalSort(src):
    global S
    global visited
    
    visited[src] = True
    
    for j in reversed(sorted(Adj[src])):
        if visited[j] == False:
            TopologicalSort(j)
    
    S.append(src)




#  ------------- Main Code ----------------
n,m = map(int,input().split())

S = []
visited = [False for i in range(n+1)]

Adj = {}
for i in range(1,n+1):
    Adj[i]=[]
    
for _ in range(m):
    x,y = map(int,input().split())
    Adj[x].append(y)


# print(Adj)
for i in range(n,0,-1):
    if visited[i]==False:
        TopologicalSort(i)

while len(S)>0:
    print(S.pop(),end=" ")
    