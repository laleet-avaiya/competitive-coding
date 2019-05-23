def isSafe(x, y,sol):
        return (x >= 0 and x < 8 and y >= 0 and y < 8 and sol[x][y] == -1)

def printSolution(sol):
	for i in range(8):
		for j in range(8):
			print(sol[i][j] + " ")
		print()

def solveKTUtil(x,y,movei,sol,xmoves,ymoves):
	print(movei)
	if movei==53:
		return True
	for k in range(len(sol)):
		next_x=x+xmoves[k]
		next_y=y+ymoves[k]

		if isSafe(next_x,next_y,sol):
			sol[next_x][next_y]=movei
			if solveKTUtil(next_x,next_y,movei+1,sol,xmoves,ymoves):
				return True
			else:
				sol[next_x][next_y]=-1

	return False


def SolveKT():
	sol = [[-1 for i in range(8)]for j in range(8)]

	# Xmoves
	xmoves=[1,1,-1,-1,2,2,-2,-2]
	ymoves=[2,-2,2,-2,1,-1,1,-1]

	sol[0][0]=0

	if not solveKTUtil(0,0,1,sol,xmoves,ymoves):
		print("solution not exist")
	else:
		printSolution(sol)


if __name__ == '__main__':
	print(1)
	SolveKT()