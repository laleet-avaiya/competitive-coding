# Reverse words in a given string 
# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

#code
t=int(input())
while t>0:
    t-=1
    s = list(input().split("."))
    s.reverse()
    print(".".join(s))