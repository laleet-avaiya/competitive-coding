# Parenthesis Checker 
# https://practice.geeksforgeeks.org/problems/parenthesis-checker/0

#code

t=int(input())
while t>0:
    t=t-1
    s=input()
    s=list(s)
    ans=[]
    flag=0
    for i in s:
        if i=='{' or i=='[' or i=='(':
            ans.append(i)
        else:
            if len(ans)==0:
                flag=1
                break
            
            
            if (i=='}' and ans[-1]=='{') or (i==')' and ans[-1]=='(') or (i==']' and ans[-1]=='['):
                ans.pop()
            else:
                flag=1
                break
            
                
    
    if flag==0 and len(ans)==0:
        print("balanced")
    else:
        print("not balanced")