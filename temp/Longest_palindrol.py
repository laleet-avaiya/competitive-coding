def LPS(o,i):
	ans=0
	n=i-1
	m=i+1
	while(n>=0 and m<len(o) and o[n]==o[m]):
		ans+=1
		n=n-1
		m=m+1
	return ans



p='aaaabbaa'
a=list(p)
s='|'.join(a)
p='|'+s+'|'

# print(p)


answer=[]
for i in range(len(p)):
	answer.append(LPS(p,i))

print(max(answer))

start=answer.index(max(answer))-max(answer)
stop=answer.index(max(answer))+max(answer)+1

sa=''.join(p[start:stop])
ans=list(sa.split('|'))
ans.pop()
ans.pop(0)
print(''.join(ans))