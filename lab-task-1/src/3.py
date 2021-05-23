##### SOLUTION 3: 
##### MAGIC SQUARE METHOD


##### import Required Libraries
from math import inf as infinity
from random import choice
import platform
import time
from os import system



##### The Global Variables
HUMAN = -1
COMP = +1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
HumanMagic = []
CompMagic = []
square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]



##### Function to heuristic evaluation of state.
##### :param state: the state of the current board
##### :return: +1 if the computer wins; -1 if the human wins; 0 draw
def evaluate(state):

    if checkWin(state, COMP):
        score = +1
    elif checkWin(state, HUMAN):
        score = -1
    else:
        score = 0

    return score



##### This function tests if a specific player wins. Possibilities:
##### (i) Three rows      [X X X] or [O O O]
##### (ii) Three cols     [X X X] or [O O O]
##### (iii) Two diagonals [X X X] or [O O O]
##### :param state: the state of the current board
##### :param player: a human or a computer
##### :return: True if the player wins
def checkWin(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False



##### This function tests if the human or computer wins
##### :param state: the state of the current board
##### :return: True if the human or computer wins
def game_over(state):
    return checkWin(state, HUMAN) or checkWin(state, COMP)



##### Each empty cell will be added into cells' list
##### :param state: the state of the current board
##### :return: a list of empty cells
def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells



##### A move is valid if the chosen cell is empty
##### :param x: X coordinate
##### :param y: Y coordinate
##### :return: True if the board[x][y] is empty
def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False



##### Set the move on board, if the coordinates are valid
##### :param x: X coordinate
##### :param y: Y coordinate
##### :param player: the current player
def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        if player == COMP:
            CompMagic.append(square[x][y])
        else:
            HumanMagic.append(square[x][y])
        return True
    else:
        return False



def MagicSquare():
    if(len(CompMagic)>=2):
        for i in CompMagic:
            for j in CompMagic:
                if i!=j and 15-(i+j)>0 and 15-(i+j)<=9 and (15-(i+j) not in CompMagic and 15-(i+j) not in HumanMagic):
                    return 15-(i+j)
                
    if(len(HumanMagic)>=2):
        for i in HumanMagic:
            for j in  HumanMagic:
                if i!=j and 15-(i+j)>0 and 15-(i+j)<=9 and (15-(i+j) not in CompMagic and 15-(i+j) not in HumanMagic):
                    return 15-(i+j)

    if len(CompMagic)==0 and len(HumanMagic)==0:
        return 5

    if len(CompMagic)==1 and len(HumanMagic)==1:
        if HumanMagic[0]%2 == 1:
            p = HumanMagic[0]
            if p == 3:
                return 9
            if p == 9:
                return 7
            if p == 7:
                return 1
            if p == 1:
                return 3

    if len(CompMagic)==2 and len(HumanMagic)==2:
        p = CompMagic[0]
        q = CompMagic[1]
        if q == 3:
            return 4
        if q == 9:
            return 2
        if q == 7:
            return 6
        if q == 1:
            return 8
         
                
    if(5 not in HumanMagic and 5 not in CompMagic):
        return 5

    if len(CompMagic)==0 and len(HumanMagic)==1:
         p = HumanMagic[0]
         if p == 5:
             return 8
    
    
    for i in range(1,10):
        if i not in HumanMagic and i not in CompMagic:
            return i       
    


##### Clears the console
def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


##### Print the board on console
##### :param state: current state of the board
def render(state, c_choice, h_choice):

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)



##### It calls the Magic Squarre function if the depth < 9,
##### else it choices a random coordinate.
##### :param c_choice: computer's choice X or O
##### :param h_choice: human's choice X or O
##### :return:
def ai_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)
  
    r=MagicSquare()
    print(f"chosen number in magic square is {r}")
    for x, row in enumerate(square):
        for y, cell in enumerate(row):
            if cell == r:
                i, j = x, y
                break

    set_move(i, j, COMP)
    time.sleep(1)



##### The Human plays choosing a valid move.
##### :param c_choice: computer's choice X or O
##### :param h_choice: human's choice X or O
##### :return:
def human_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')



##### A function that calls all functions
def play():

    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if checkWin(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WON!')
    elif checkWin(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOST!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()



##### GAME PLAY
play()