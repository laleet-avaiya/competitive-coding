# Nuts and Bolts Problem
# 16 June 2019
# https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem/0

#code

def temp(a,b):
    return ord(a)-ord(b)
    
for _ in range(int(input())):
    n = int(input())
    a = list(input().split())
    b = list(input().split())
   
    a.sort()
    b.sort()
    
    for i in a:
        print(i, end=" ")
    print("")
    for i in b:
        print(i, end=" ")
    print("")