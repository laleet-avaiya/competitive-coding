n=4

def issafe(maze,x,y):

	if x<n and y<n and maze[x][y]==1:
		return True

	return False

def rate_in_maze(maze,x,y,sol):
	#base case:

	if x==n-1 and y==n-1:
		sol[x][y]=1
		for i in sol:
			print(i,end="\n")

	if issafe(maze,x,y):

		sol[x][y]=1

		if rate_in_maze(maze,x+1,y,sol):
			return True

		if rate_in_maze(maze,x,y+1,sol):
			return True

		sol[x][y]=0

	return False




if __name__ == '__main__':
	maze=[	[1,1,0,0],
			[1,0,1,0],
			[1,0,1,0],
			[1,1,1,1]]

	sol = [[0 for i in range(n)] for i in range(n)]
	rate_in_maze(maze,0,0,sol)