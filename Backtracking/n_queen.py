n=4

def issafe(x,y,board):
    for i in range(n):
        if board[i][y]==1:
            return False
        if board[x][i]==1:
            return False

    for i in range(n):
        for j in range(n):
            if i+j==x+y and board[i][j]==1:
                return False
            if i-j==x-y and board[i][j]==1:
                return False

    return True


def Queen(col,board):
    
    if col==0:
        for i in board:
            print(i)
        return True

    for i in range(n):
        for j in range(n):
            if issafe(i,j,board):
                board[i][j]=1
                if Queen(col-1,board):
                    return True
                board[i][j]=0
    return False


if __name__ == '__main__':
    board=[[0 for i in range(n)]for i in range(n)]
    print(Queen(n,board))