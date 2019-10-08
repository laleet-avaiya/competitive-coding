# Find the nearest clone
# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#


minDistanct = 100000000
n = 0
c = 0

def DFS(G,visited,colors,s,distance):
    global minDistanct
    global n
    visited[s] = True
    
    for i in range(n):
        if G[s][i]==1 and visited[i]==False:
            print(s,i,colors[s],colors[i])
            if c==colors[i]:
                print(distance)
                if distance + 1<minDistanct:
                    minDistanct = distance+1
            DFS(G,visited,colors,i,distance+1)



def findShortest(graph_nodes, graph_from, graph_to, colors, s):
    # solve here

    if colors.count(colors[s-1])==1:
        return -1

        
    global n
    global minDistanct
    global c

    n = graph_nodes
    G = [[0 for i in range(n)]for j in range(n)]
    visited = [False]*n
    c = colors[s-1]
    
    e = len(graph_from)
    for i in range(e):
        a=graph_from[i]-1
        b=graph_to[i]-1
        G[a][b] = 1
        G[b][a] = 1
    # print(ids)

    DFS(G,visited,colors,s-1,0)

    if minDistanct == 100000000:
        return -1 
    return minDistanct

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

