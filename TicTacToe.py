"""Tic Tac Toe
Author: Karanbir Singh, ksohi97@gmail.com
"""
def printBoard(board):
    for x in board:
        print(" ".join(map(str, x)))

#check if someone won aliging 3 tokens horizontally
def checkHorizontalWinner(board, user):
    count = 0
    for i in board:
        for j in i:
            if j == user:
                count = count + 1
        if count == 3:
            return True
            break
        else:
            count = 0
    return False

#check if someone won aliging 3 tokens diagonally
def checkDiagonalWinner(board, usr):
    if board[0][0] == usr and board[1][1] == usr and board[2][2] == usr:
        return True
    elif board[0][2] == usr and board[1][1] == usr and board[3][0] == usr:
        return True
    return False

#check if someone won aliging 3 tokens vertically
def checkVerticalWinner(board, usr):
    if board[0][0] == usr and board[1][0] == usr and board[2][0] == usr:
        return True
    if board[0][1] == usr and board[1][1] == usr and board[2][1] == usr:
        return True
    if board[0][2] == usr and board[1][2] == usr and board[2][2] == usr:
        return True
    return False

#check if the input is out of boundary or there is an element already placed in that place, in both cases: retake the input
def checkInput(board, r, c, usr):
    if r < 0 or r > 2 or c < 0 or c > 2:
        print "input out of Index "
        print "user", usr, "please enter the position for your token: "
        r = input("row position: ")
        c = input("column position: ")
        if board[r][c] != 0:
            print "token is already present"
            print "user", usr, "please inter the position for your token: "
            r = input("row position: ")
            c = input("column position: ")
    else:
        board[r][c] = usr



def checkWinner(board, us):
    if checkHorizontalWinner(board, us):
        return True
    elif checkDiagonalWinner(gameBoard, us):
        return True
    elif checkVerticalWinner(gameBoard, us):
        return True
    return False


print "Welcome to Tic Tac Toe"

gameBoard = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
totInput = 0
user = 1
printBoard(gameBoard)
#run the game till the max number of inputs
while totInput < 9:
    print "user", user, "please enter the position for your token: "
    row = input("row position: ")
    column = input("column position: ")
    checkInput(gameBoard, row, column, user)
    totInput = totInput + 1
    #checkWinner after the 4th input and keep checking until the whole table is not filled
    if totInput > 4:
        if checkWinner(gameBoard, user):
            print "User", user, "has won the game"
            printBoard(gameBoard)
            break
    if user == 1:
        user = 2
    else:
        user = 1
    printBoard(gameBoard)

if totInput > 8:
    print "Match Drawn"
    printBoard(gameBoard)
