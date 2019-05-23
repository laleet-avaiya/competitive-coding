# Array:

# 1. Subarray with given sum
# 2. Kadanes Algorithm
# 3. Missing number in array
# 4. Subarray with given sum
# 5. Sort an array of 0s, 1s and 2s
# 6. Equilibrium point
# 	Maximum sum increasing subsequence
# 8. Leaders in an array
# 	Minimum Platforms
# 	Maximum of all subarrays of size k 

from collections import Counter

cnta = Counter()
cntb = Counter()

s1="laleet"
s2="eetlal"
a=list(s1)
b=list(s2)
# a=[0,0,1,2,3,1,2,2,2,2,2,3,4]

for i in a:
	cnta[i] += 1

for i in b:
	cntb[i] += 1

print(cnta==cntb)
print(list(cnta.elements()))



import math, heapq, itertools,copy
help()