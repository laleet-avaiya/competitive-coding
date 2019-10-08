input = ['go','bat','me','eat','goal','boy','run'] 
charSet = ['e','o','b', 'a','m','g', 'l'] 
print(list(charSet))

for word in input:
	a = list(word)

	if a in charSet:
		print(word)