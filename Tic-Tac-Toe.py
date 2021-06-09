from random import randrange
board=[[1,2,3],[4,5,6],[7,8,9]]


# the function accepts one parameter containing the board's current status
# and prints it out to the console
def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  {}    |   {}   |  {}    |".format(board[0][0],board[0][1],board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  {}    |   {}   |  {}    |".format(board[1][0],board[1][1],board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  {}    |   {}   |  {}    |".format(board[2][0],board[2][1],board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")


# the function accepts the board current status, asks the user about their move,
# checks the input and updates the board according to the user's decision
def EnterMove(board):
    O=int(input("Enter Your Move:"))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==O:
                board[i][j]="O"
                DisplayBoard(board)
                if VictoryFor(board,"O"):
                    print("Game Over")
                else:
                    DrawMove(board)


# the function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers
def MakeListOfFreeFields(board):
    global list
    list=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=="O" or board[i][j]=="X":
                continue
            else:
                list.append(board[i][j])


# the function analyzes the board status in order to check if
# the player using 'O's or 'X's has won the game
def VictoryFor(board, sign):
    check_rows=check_columns=check_diagonals=False
    for i in range(len(board)):
            if board[i][0]==board[i][1]==board[i][2]:
                check_rows=True
                if board[i][0]=="O":
                    print("You Won!")
                    return True
                if board[i][0]=="X":
                    print("computer Won!")
                    return True
    for j in range(len(board)):
        if board[0][j]==board[1][j]==board[2][j]:
            check_columns=True
            if board[0][j]=="O":
                print("You Won!")
                return True
            if board[0][j]=="X":
                print("computer Won!")
                return True
    if board[0][0]==board[1][1]==board[2][2]:
        check_diagonals=True
        if board[1][1]=="O":
            print("You Won!")
            return True
        if board[1][1]=="X":
            print("computer Won!")
            return True
    if board[0][2]==board[1][1]==board[2][0]:
        check_diagonals=True
        if board[1][1]=="O":
            print("You Won!")
            return True
        if board[1][1]=="X":
            print("computer Won!")
            return True
    if check_rows is False or check_columns is False or check_diagonals is False:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if str(board[i][j]).isnumeric():
                    print(str(board[i][j]).isnumeric())
                    return False

        print("game is tie")
        return True




# the function draws the computer's move and updates the board
def DrawMove(board):
    MakeListOfFreeFields(board)
    X_element_index=randrange(len(list))
    X=list[X_element_index]
    print(X)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==X:
                board[i][j]="X"
                DisplayBoard(board)
                if VictoryFor(board,"X"):
                    print("Game Over")
                else:
                    EnterMove(board)



board[1][1]="X"
DisplayBoard(board)
EnterMove(board)
