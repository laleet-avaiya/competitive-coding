import math

arr1 = [1,3,5,7]
arr2 = [2,4,6,8,9,10]

n=len(arr1)
m=len(arr2)

gap = int(math.ceil((n+m)/2))

print(gap)
# exit()

print(arr1)
print(arr2)		
print(" ")	


while gap!=0:
	

	# Arr1
	print("Gap",gap)
	for i in range(n):
		if i+gap > n-1:
			break
		if arr1[i] > arr1[i+gap]:
			arr1[i] = arr1[i] + arr1[i+gap]
			arr1[i+gap] = arr1[i] - arr1[i+gap]
			arr1[i] = arr1[i] - arr1[i+gap]



	# comparing elements in both arrays.

	if gap>n:
		start=gap - n
	else:
		start=0

	
	for j in range(start,m):

		if i>n-1 or j>m-1:
			break

		if arr1[i] > arr2[j]:
			temp = arr2[j]
			arr2[j]=arr1[i]
			arr1[i]=temp

		i+=1


	if j < m:

		for i in range(0,m):
			if i+gap > m-1:
				break

			if arr2[i] > arr2[i+gap]:
				arr2[i] = arr2[i] + arr2[i+gap]
				arr2[i+gap] = arr2[i] - arr2[i+gap]
				arr2[i] = arr2[i] - arr2[i+gap]

	
	print(arr1)
	print(arr2)		
	print(" ")	

	gap = int(math.ceil(gap/2))

	 

for i in arr1:
	print(i,end=" ")

for i in arr2:
	print(i,end=" ")