v=4
adj=[[0 for i in range(v)]for j in range(4)]
edges=[[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]

for i in edges:
	adj[i[0]][i[1]]=1

print(adj)

visited=[0 for i in range(v)]
print(visited)

q=[]

q.append(2)
visited[2]=1

while len(q)!=0:
	# print(q)
	ver=q.pop(0) #2
	print(ver)

	for i in range(v):
		if adj[ver][i]==1 and visited[i]==0:
			q.append(i)
			visited[i]=1


