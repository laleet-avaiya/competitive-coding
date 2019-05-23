# # 4
# # 1 2
# # 2 3
# # 2 4

# class Node:

# 	def __init__ (self,data):
# 		self.data = data
# 		self.left = None
# 		self.right = None


# def InOrder(ans,node):
# 	if node:
# 		ans.append(node)
# 		InOrder(ans,node.left)
# 		InOrder(ans,node.right)

# def Height(node):
# 	if node:
# 		if node.left== None and node.right==None:
# 			return 0
# 		else:
# 			return 1+max(Height(node.left),Height(node.right))


# def calculate_distance_height(count,node,distance_from_root):
# 	if node:
# 		calculate_distance_height(count,node.left,distance_from_root+1)
# 		calculate_distance_height(count,node.right,distance_from_root+1)
# 		count+=1

# edges = [[1,2],[2,3],[2,4]]

# for i in edges:

# a = Node(1)
# a.right = Node(2)
# a.right.left = Node(3)
# a.right.right = Node(4)

# ans = []
# InOrder(ans,a)

# height=[0]*4
# j=0

# for i in ans:
# 	height[j]=Height(i)
# 	j=j+1

# count=0
# distance_from_roottance=0
# calculate_distance_height(count,a,distance)
# print(count)

# # print(height)






L = [1,2,3]
print([L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)])