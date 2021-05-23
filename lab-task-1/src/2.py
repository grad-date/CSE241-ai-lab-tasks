##### SOLUTION 2:


##### For cleaning the console
import os



##### The Global Variables
board = [2, 2, 2, 2, 2, 2, 2, 2, 2]
turn = 1



##### A function to display the board
def displayBoard():
    global board

    # Temporary board corresponding to 'X', 'O' and empty space
    # To render the correct symbols
    temp_board =  [' ' for x in range(9)]
    for i in range(9):
        if board[i]==3:
            temp_board[i]='X'
        elif board[i]==5:
            temp_board[i]='O'

    print("       |       |       ")
    print("  ",  temp_board[0], "  |  ", temp_board[1], "  |  ", temp_board[2])
    print("_______|_______|_______")
    print("       |       |       ")
    print("  ",  temp_board[3], "  |  ", temp_board[4], "  |  ", temp_board[5])
    print("_______|_______|_______")
    print("       |       |       ")
    print("  ",  temp_board[6], "  |  ", temp_board[7], "  |  ", temp_board[8])
    print("       |       |       \n")



##### This function finds the winning or blocking index
##### for Computer's turn
##### :return: winning/blocking index
def posswin():
    global board

    # Checking rows to Win
    for i in range(0, 9, 3):
        if(board[i]*board[i+1]*board[i+2]==50):
            if(board[i]==2):
                return i
            elif(board[i+1]==2):
                return i+1
            elif(board[i+2]==2):
                return i+2

    # Checking columns to Win
    for i in range(3):
        if(board[i]*board[i+3]*board[i+6]==50):
            if(board[i]==2):
                return i
            elif(board[i+3]==2):
                return i+3
            elif(board[i+6]==2):
                return i+6

    # Checking Right Diagonal to Win
    if(board[0]*board[4]*board[8] == 50):
        if(board[0]==2):
            return 0
        elif(board[4]==2):
            return 4
        elif(board[8]==2):
            return 8

    # Checking Left Diagonal to Win
    if(board[2]*board[4]*board[6] == 50):
        if(board[2]==2):
            return 2
        elif(board[4]==2):
            return 4
        elif(board[6]==2):
            return 6

    # Checking rows to Block
    for i in range(0, 9, 3):
        if(board[i]*board[i+1]*board[i+2]==18):
            if(board[i]==2):
                return i
            elif(board[i+1]==2):
                return i+1
            elif(board[i+2]==2):
                return i+2

    # Checking columns to Block
    for i in range(3):
        if(board[i]*board[i+3]*board[i+6]==18):
            if(board[i]==2):
                return i
            elif(board[i+3]==2):
                return i+3
            elif(board[i+6]==2):
                return i+6

    # Checking Right Diagonal to Block
    if(board[0]*board[4]*board[8] == 18):
        if(board[0]==2):
            return 0
        elif(board[4]==2):
            return 4
        elif(board[8]==2):
            return 8

    # Checking Left Diagonal to Block
    if(board[2]*board[4]*board[6] == 18):
        if(board[2]==2):
            return 2
        elif(board[4]==2):
            return 4
        elif(board[6]==2):
            return 6

    return -1



##### This function takes care of invalid moves and valid assignments
##### :param move: current move in the game
##### :return: True for valid move after corresponding assignment
def go(move):
    global board, turn

    # Invalid if out of range
    if (move not in range(9)):
        return False

    # Invalid if 
    elif (board[move]!=2):
        return False

    # If valid then assign the square corresponding value
    else:
        board[move] = 3 if (turn&1) else 5
        return True



##### A function for Computer's turn to DRAW the game:
##### :return: center or corner position
def make2():
    global board

    # Return Centre position
    if board[4]==2:
        return 4

    # Return Corner position
    for i in range(0, 9, 2):
        if board[i]==2:
            return i



##### A function which keeps track of winning player
##### :return: True if anyone wins
def checkWin():
    global board

    # Check Rows
    for i in range(0, 9, 3):
        if(board[i] == board[i+1] == board[i+2] != 2):
            return True

    # Check Columns
    for i in range(3):
        if(board[i] == board[i+3] == board[i+6] != 2):
            return True 

    # Check diagonals
    if(board[0] == board[4] == board[8] != 2):
        return True
    elif(board[2] == board[4] == board[6] != 2):
        return True
    
    return False



##### The Driver Function to play and end the game that
##### calls other functions
def play():
    global board, turn

    # Initial i.e. Empty Board
    displayBoard()

    # First turn (i.e 'X') is given to Human
    while(not checkWin() and turn<10):

        # Human's turn
        if(turn&1):
            
            # Assuming no ValueError
            move = int(input('Enter field (1-9): '))

            while not go(move-1):
                move = int(input('Enter valid field (1-9): '))


            os.system('clear')
            print('Your move:')
            displayBoard()

            if checkWin():
                print('YOU WON!')
                break

        # Computer's turn
        else:
            if(posswin()!=-1):
                go(posswin())
            else:
                go(make2())

            print('Computer\'s move:')
            displayBoard()

            if checkWin():
                print('YOU LOST!')
                break

        turn += 1

    # Check Draw
    if not checkWin():
        print('IT\'S A DRAW!')



##### GAME PLAY
play()