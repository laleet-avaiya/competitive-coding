def toogle(adj,managers,lamp):
    q=[]
    visited=[0 for i in range(n)]

    q.append(managers)

    if lamp[managers-1]==1:
        lamp[managers-1]=0
    else:
        lamp[managers-1]=1

    
    while len(q)!=0:
        manager=q.pop(0)
        

        for i in range(len(adj)):
            if adj[manager][i]==1 and i!=manager:
                if visited[i-1]!=1:
                    q.append(i)

                    visited[i-1]=1


                if lamp[i-1]==1:
                    lamp[i-1]=0
                else:
                    lamp[i-1]=1

    return lamp

n=int(input())
manager=list(map(int,input().split()))
edges=[]
for i in range(len(manager)):
    edges.append([manager[i],i+2])
q=int(input())
ao=list(map(int,input().split()))


adj=[[0 for i in range(n+1)]for j in range(n+1)]


for i in range(1,len(adj)):
    adj[i][i]=1

for i in edges:
    adj[i[0]][i[1]]=1

lamp=[0 for i in range(n)]

for i in ao:
    lamp=toogle(adj,i,lamp)
    
    
for j in lamp:
    print(j,end=' ')
    


