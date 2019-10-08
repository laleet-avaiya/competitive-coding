s='aabcbcdbca'

d=set(s)
p=len(d)
ans=0
i=0

while True:
	if set(s[i:p+i])==d:
		ans=len(s[i:p+i])
		break
	i=i+1
	if i>=len(s)-p+1:
		i=0
		p=p+1

print(ans)