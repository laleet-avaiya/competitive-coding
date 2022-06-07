class Solution:

    ans = [] 

    def generate(self, s: str, open: int, close: int, n: int) -> None:
    	global ans
    	if close > open or len(s) > 2*n:
    		return
    	
    	elif len(s) == 2*n and open == close:
    		self.ans.append(s)
    		return
    	else:
    		self.generate(s+"(", open+1, close, n)
    		self.generate(s+")", open, close+1, n)
    		
    
    def generateParenthesis(self, n: int) -> List[str]:
    	global ans
    	self.ans = []
    	self.generate("", 0, 0, n)
    	return self.ans