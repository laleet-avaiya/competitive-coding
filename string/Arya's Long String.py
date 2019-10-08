# Arya's Long String 
# https://practice.geeksforgeeks.org/problems/aryas-long-string/0/?ref=self

t = int(input())
while t > 0 :
    s = input()
    aa = []
    aa = input().split(" ")
    k = int(aa[0])
    n = int(aa[1])
    key = aa[2]
            
    count = 0
    
    for i in range(len(s)):
        if s[i] == key:
            count += 1
       
    x = int(n/len(s))
    y = n%len(s)
    count *= x
    
    for i in range(y):
        if s[i] == key:
            count += 1
            
    print(count)
    t -= 1;