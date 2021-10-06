# this is sample for testing the sudokuSolver function
sample = [[0,6,0,0,5,1,0,7,0],[3,7,4,9,0,0,0,0,0],[0,0,0,0,0,0,0,2,0],
          [4,9,0,0,0,0,0,3,2],[2,0,8,0,6,9,7,0,5],[7,0,3,2,0,0,1,9,0],
          [5,0,1,6,2,7,0,0,4],[6,4,0,8,1,0,0,0,7],[0,0,0,0,0,4,6,0,3]]
# checking whether the postion [r][c] is valid from number n
def sudokuCheck(board,r,c,n):
    for x in range(9):
        if(n in [board[r][x],board[x][c]]):
            return False
    bR,bC = r//3,c//3
    for R in range(3):
        for C in range(3):
            if(n==board[R+3*bR][C+3*bC]):
                return False
    return True
# this function check whether given sudoku is valid or invalid
def validation(board,r=0,c=0):
    if(r==9):
        return True
    n=board[r][c]
    if(n==0):
        return validation(board,r+(c==8),(c+1)%9)
    board[r][c]=0
    if(sudokuCheck(board,r,c,n)):
        board[r][c]=n
        return validation(board,r+(c==8),(c+1)%9)
    board[r][c]=n
    return False
# sudoku solver main function
# if sudoku is solvable than this fuction return solved sudoku (2d array)
# else it will return 0 which means "sudoku is not solvable"
def sudokuSolver(board,r=0,c=0):
    if(r==9):
        return board
    for n in range(1,10):
        if (board[r][c]):
            return sudokuSolver(board,r+(c==8),(c+1)%9)
        elif(sudokuCheck(board,r,c,n)):
           board[r][c]=n
           re = sudokuSolver(board,r+(c==8),(c+1)%9)
           if(re):
              return re
           board[r][c]=0
    return False
