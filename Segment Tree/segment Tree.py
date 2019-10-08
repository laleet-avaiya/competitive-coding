
# https://www.youtube.com/watch?v=BuoG-1KC4qs
def buildTree(arr,tree,start,end,treenode):
	
	if start == end:
		tree[treenode] = start
		return

	mid = (start+end)/2
	buildTree(arr,tree,start,mid,2*treenode)
	buildTree(arr,tree,mid+1,end,2*treenode+1)

	tree[treenode] = tree[2*treenode] + tree[2*treenode+1]


arr = [1,2,3,4,5,6,7,8,9]
tree = [0]*(18)

buildTree(arr,tree,1,9,1)
print(tree)
# print("A")
