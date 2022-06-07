class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
        	if len(stack) > 0:
        		if a == ')' and stack[-1] == '(':
        			stack.pop()
        		elif a == '}' and stack[-1] == '{':
        			stack.pop()
        		elif a == ']' and stack[-1] == '[':
        			stack.pop()
        		elif a == '{' or a == '(' or a =='[':
        			stack.append(a)
        		else:
        			return False
        	else:
        		stack.append(a)
        
        return len(stack) == 0