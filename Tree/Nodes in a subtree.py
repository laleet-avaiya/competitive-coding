def dfs(string,edge,count,node,visited):
	#checking node
	if node not in visited:
		count[node-1][ord(string[node-1])-ord('a')]+=1
		visited.add(node)

	for kids in edge[node]:
		if kids not in visited:
			dfs(string,edge,count,kids,visited)
			for i in range(26):
				count[node-1][i]+=count[kids-1][i]

#taking inputs
n,q=map(int,input().split())
string=list(input())

#making adj list for the edges give
edge={ i:[] for i in range(1,n+1) }
for _ in range(n-1):
	u,v=map(int,input().split())
	edge[u].append(v)
	edge[v].append(u)

#initialising count matrix of size (26,n)
count=[[0 for i in range(26)] for j in range(n)]
visited=set()

dfs(string,edge,count,1,visited)

for _ in range(q):
	x,s=input().split()
	print(count[int(x)-1][ord(s)-ord('a')])
