# https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/tutorial/
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

nm = input().split()
n = int(nm[0])
m = int(nm[1])

G = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    ab = input().split()
    a=int(ab[0])
    b=int(ab[1])
    G[a][b]=1
#     G[b][a]=1

Q = int(input())
while Q>0:
    Q -= 1
    AB = input().split()
    A=int(AB[0])
    B=int(AB[1])
    if G[A][B]==1:
        print("YES")
    else:
        print("NO")
    
    