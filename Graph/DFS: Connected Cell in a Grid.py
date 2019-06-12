# DFS: Connected Cell in a Grid
# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
count = 0


def DFS(a,i,j,n,m):
    global count

    if(i<0 or i>=n or j<0 or j>=m or a[i][j]==0):
        return;

    count += 1 
    a[i][j] = 0;
    
    DFS(a,i+1,j,n,m);
    DFS(a,i-1,j,n,m);
    DFS(a,i,j+1,n,m);
    DFS(a,i,j-1,n,m);
    DFS(a,i+1,j+1,n,m);
    DFS(a,i-1,j-1,n,m);
    DFS(a,i-1,j+1,n,m);
    DFS(a,i+1,j-1,n,m);

def maxRegion(a):

    global count
    n = len(a)
    m = len(a[0])
    maximum = 0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                count = 0
                DFS(a,i,j,n,m)
                if count > maximum:
                    maximum = count
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
