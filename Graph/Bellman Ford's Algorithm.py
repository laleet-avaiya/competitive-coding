# Bellman Ford's Algorithm:

a = 1
b = 2
c = 3
d = 4
s = 0

edges = [[a,b,5],[a,c,8],[a,d,-4],[b,a,-2],[c,b,-3],[c,d,9],[d,s,2],[d,b,7],[s,a,6],[s,c,7]]
v = 5
distance = [999999]*v

distance[0] = 0
# print(distance)

for i in range(0,v):
	for j in edges:
		if distance[j[0]] + j[2] < distance[j[1]]:
			distance[j[1]] = distance[j[0]] + j[2]

print(distance)







