# Permutations of a given string 
# https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0

#code
import itertools

t=int(input())
while t>0:
    t=t-1
    s=list(input())
    ans=list(itertools.permutations(s))
    ans.sort()
    for i in ans:
        print("".join(i),end=" ")
    print("")
    