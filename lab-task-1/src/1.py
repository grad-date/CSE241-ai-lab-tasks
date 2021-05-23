def CheckWin():
    return (board[0] == '2' and board[1] == '2' and board[2] == '2') or \
           (board[3] == '2' and board[4] == '2' and board[5] == '2') or \
           (board[6] == '2' and board[7] == '2' and board[8] == '2') or \
           (board[0] == '2' and board[3] == '2' and board[6] == '2') or \
           (board[1] == '2' and board[4] == '2' and board[7] == '2') or \
           (board[2] == '2' and board[5] == '2' and board[8] == '2') or \
           (board[0] == '2' and board[4] == '2' and board[8] == '2') or \
           (board[2] == '2' and board[4] == '2' and board[6] == '2')



def printGame(position):
    print("""
              {} | {} | {}
             -----------
              {} | {} | {}
             -----------
              {} | {} | {}
            """.format(*position))



def printBoard():
    a = {'0': ' ', '1': 'X', '2': 'O'}
    position = map(lambda m: a[m], board)
    printGame(position)



def readMovetable():
    with open("MT.txt", "r") as f:
        table = f.readlines()
        for line in table:
            entry = line.split()
            move_table[entry[0]] = entry[1]



move_table = {}
readMovetable()
board = list("0" * 9)
turn = 0
printGame(range(1, 10))
while True:
    move = int(input("Your Turn, Enter from (1-9) : ")) - 1
    if move not in range(9) or board[move] != '0':
        print("Try Again, wrong move")
        continue

    board[move] = '1'
    printBoard()
    turn += 1
    if turn == 9:
        print('' * 10, "IT\'S A DRAW!", '' * 10)
        break

    new_board = list(move_table["".join(board)])
    move = [i + 1 for i in range(9) if board[i] != new_board[i]][0]
    print("Computer's Turn:", move)
    board = new_board
    printBoard()
    print('-' * 50, '\n')
    turn += 1
    if CheckWin():
        print('' * 10, "YOU LOST!", '' * 10)
        break
