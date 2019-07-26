

v=4

adj=[[0 for i in range(v)]for j in range(4)]

edges=[[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]

for i in edges:
	adj[i[0]][i[1]]=1

#   for i in adj:
# 	print(i)

# print("")
visited=[0 for i in range(v)]
print(visited)

def DFS(a):
	print(a)
	visited[a]=1

	for i in range(v):
		if adj[a][i]==1 and visited[i]==0:
			DFS(i)

visited[2]=1
DFS(2)

