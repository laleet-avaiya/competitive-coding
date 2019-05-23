# def is_sorted(arr):
#     return True if list(arr) == sorted(arr) else False

# def gridChallenge(grid):
#     sorted_col = (is_sorted(z) for z in zip(*grid))  
#     return(['NO','YES'][all(sorted_col)])


# a1 = 1 3 5 7
# a2 = 2 4 6 8 9 10

# output : 1 2 3 4 5 6 7 8 9 10

arr1 = [1,3,5,7]
arr2 = [2,4,6,8,9,10]

for i in range(len(arr1)-1,-1,-1):
	
	j=len(arr2)-1
	temp = arr2[j]	# 10
	# print(temp)

	while arr2[j]>arr1[i] and j>=0:
		arr2[j]=arr2[j-1]
		j=j-1

	arr2[j+1]=arr1[i]
	arr1[i]=temp

print(arr2 + arr1)



# from heapq import merge

# for _ in range(int(input())):
#     p,q=map(int,input().split())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     c=list(merge(a,b))
#     print(*c)






