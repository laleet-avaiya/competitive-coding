def minoperaation(s,t,l):
	count_0=0
	count_1=0

	for i in range(l):
		if s[i]==t[i]:
			continue

		if s[i]=='0':
			count_0+=1
		else:
			count_1+=1


	return max(count_0,count_1)


if __name__ == '__main__':
	s='11'
	t='01'
	print(minoperaation(s,t,len(s)))
	