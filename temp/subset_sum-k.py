import itertools

def subset_with_sum_k(arr,k):
	arr.sort()
	for i in itertools.combinations(arr,2):
		if sum(i)==k:
			print(i)
		


if __name__ == '__main__':
	arr=[1,2,3,0]
	k=3
	subset_with_sum_k(arr,k)
