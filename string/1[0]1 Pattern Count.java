// 1[0]1 Pattern Count 
// 20 June 2019
// https://practice.geeksforgeeks.org/problems/101-pattern-count/0/?ref=self
// #code
for _ in range(int(input())):
    s = input()
    s = list(s)
    stack = []
    
    count=0
    for i in s:
        if i!="0" and i!="1":
            stack = []
        else:
            if i=="1":
                if len(stack)==0:
                    stack.append(i)
                    
                if stack[-1] == "0":
                    stack=[]
                    stack.append(i)
                    count += 1
                
            else:
                 if len(stack)>0 and stack[-1]=="1":
                    stack.append(i)
    print(count)