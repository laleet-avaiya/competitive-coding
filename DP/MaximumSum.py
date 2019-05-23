# https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/tutorial/

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
# Sample bash code
nm = input().split()
n=int(nm[0])
m=int(nm[1])

G = [[0 for i in range(n)]for j in range(m)]
Ans = [[0 for i in range(n)]for j in range(m)]

for i in range(n):
    G[i] = list(map(int,input().split()))

prev = 0
for i in range(n):
    for j in range(m):
        
        if i-1>=0:
            top = Ans[i-1][j]
        else:
            top = 0
        if j-1>=0:
            left = Ans[i][j-1]
        else:
            left = 0
        
        if i-1>=0 and j-1>=0:
            upperleft = Ans[i-1][j-1]
        else:
            upperleft = 0
        
        Ans[i][j] = G[i][j] + top + left - upperleft

q = int(input())
while q>0:
    q-=1
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    print(Ans[x-1][y-1])