board = [
    ["5", ".",".",".","4",".",".",".","9"],
    [".","2",".",".","1",".","6","8","."],
    [".",".","9","8","7",".","1",".","."],
    [".",".","6","7",".",".","2",".","."],
    [".","9",".","3","5","4",".","6","."],
    ["3",".",".",".",".",".",".",".","1"],
    ["9",".",".",".","6",".",".",".","2"],
    [".","1","4",".","3",".",".","5","7"],
    [".",".","5",".","8","7",".",".","."]
]
def resolver_sudokus():
    global board
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for k in range(1,10):
                    if es_valido(i,j,str(k)):
                        board[i][j] = str(k)
                        resolver_sudokus()
                        board[i][j] = "."
                return
    print(board)
    input("Más?")
def es_valido(i,j,k):
    global board
    for l in range(9):
        if board[i][l] == k:
            return False
    for l in range(9):
        if board[l][j] == k:
            return False
    for l in range(3):
        for m in range(3):
            if board[(i//3)*3+l][(j//3)*3+m] == k:
                return False
    return True
resolver_sudokus()

  