# https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
class Ans:
    ans = 0
    
def bfs(Tree,s):
    q=[]
    level=1
    q.append([1,s])
    
    while len(q)!=0:
        nod = q.pop(0)
        
        level = nod[0]
        node = nod[1]
        visited[node] = 1
        if level == x:
            Ans.ans += 1
            
        for j in range(n):
            if G[node][j] ==1 and visited[j]!=1:
                q.append([level+1,j])
        
    

# Write your code here
n = int(input())

G = [[0 for i in range(n)] for j in range(n)]
visited = [0]*n


for i in range(n-1):
    ab = input().split()
    a=int(ab[0])-1
    b=int(ab[1])-1
    G[a][b]=1
    G[b][a]=1


x = int(input())
bfs(G,0)

print(Ans.ans)


    
    
    