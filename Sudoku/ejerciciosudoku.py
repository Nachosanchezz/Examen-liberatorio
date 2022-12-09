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
    for i in range(9):                  #Recorre las filas
        for j in range(9):              #Recorre las columnas
            if board[i][j] == ".":      #Si encuentra un punto
                for k in range(1,10):   #Recorre los numeros del 1 al 9
                    if es_valido(i,j,str(k)):           #Si el numero es valido
                        board[i][j] = str(k)       #Lo pone en el tablero
                        resolver_sudokus()         #Vuelve a llamar a la funcion
                        board[i][j] = "."          #Si no es valido, vuelve a poner el punto
                return
    print(board)
    input("Más?")                           
def es_valido(i,j,k):
    global board                            #Para poder usar la variable board
    for l in range(9):                      #Recorre las filas    
        if board[i][l] == k:          #Si el numero esta en la fila
            return False              #No es valido
    for l in range(9):                #Recorre las columnas
        if board[l][j] == k:          #Si el numero esta en la columna
            return False              #No es valido
    for l in range(3):                #Recorre los cuadrados
        for m in range(3):            #Recorre los cuadrados
            if board[(i//3)*3+l][(j//3)*3+m] == k:              #Si el numero esta en el cuadrado
                return False                       #No es valido
    return True                                   #Si no esta en ninguna de las condiciones anteriores, es valido
resolver_sudokus()

  