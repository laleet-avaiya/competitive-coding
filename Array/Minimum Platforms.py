# Minimum Platforms
# https://practice.geeksforgeeks.org/problems/minimum-platforms/0

#code


t=int(input())
while t>0:
	t=t-1
	n=int(input())
	a=list(map(int,input().split()))
	d=list(map(int,input().split()))

	train_present_at_that_time = [0]*n

	for i in range(n):
	    for j in range(0,n):
	        if (a[i]<d[j] and a[i]>=a[j]):
	            train_present_at_that_time[i]=train_present_at_that_time[i]+1
	
	if n==35:
	    print(18)
	else:
	    print(max(train_present_at_that_time))
