#this program written by Abolfazl Soltani
import random

def display_board(board):

    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('|' + '|'.join(row) + '|')

def player_input():
    symbol=['X','O']
    valid_player = False
    player2=0
    player1=0
    val = None
    while player1 not in symbol:
        player1=input("player choose X or O:")
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return player1,player2


def place_marker(board, marker, position):
    theBoard = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
    dictionary = dict(zip(theBoard, board))

    board_values = []

    for value in dictionary.values():
        board_values.append(value)
    if str(position) in theBoard:
        board_values[theBoard.index(str(position))] = marker

    return board_values


def win_check(board, marker):
    for i in range(3):
        row = board[i * 3:(i + 1) * 3]
        if all([spot == marker for spot in row]):
            return True

    for col_ind in range(3):
        column = [board[col_ind + i * 3] for i in range(3)]
        if all([spot == marker for spot in column]):
            return True

    diagonal1 = [board[i] for i in [0, 4, 8]]
    if all([spot == marker for spot in diagonal1]):
        return True

    diagonal2 = [board[i] for i in [2, 4, 6]]
    if all([spot == marker for spot in diagonal2]):
        return True

def choose_first():
    player=['player1','player2']
    n=random.randint(0,1)
    return player[n]

def space_check(board,position):
    theBoard = ['7','8','9','4','5','6','1','2','3']
    dictionary = dict(zip(theBoard , board))
    if  dictionary[str(position)]=='X' or dictionary[str(position)]=='O':
        return True

def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True

def player_choice(board):
    p=int(input('Choose a position (1-9):'))
    if p in board :
        return p

def replay():
    restart = input("playe again? Enter yes or non(y/n)")
    if restart=='n':
        return 0

print('welcome to tic tac toe')
testboard = [' '] * 9
t = testboard
p = player_input()
c_h = choose_first()
marks = None
marks=p[0] if c_h=='player1' else p[1]
print('game start by '+c_h+' and he choose '+marks)
while True:
    if c_h=='player1':
        pl = player_choice(list(range(1, 10)))
    if c_h=='player2':
        pl=random.randint(1,9)

    if  space_check(t, pl):
        print('it\'s full'+c_h+',choose another number')
        continue
    t = place_marker(t, marks, pl)


    display_board(t)
    if win_check(t, marks) == True:
        print(c_h + '\'s win')
        R=replay()
        if R==0:
            break
        else :
            t=testboard


    marks = 'O' if marks == 'X' else 'X'
    c_h='player1' if marks==p[0] else 'player2'

    if full_board_check(t)==True:
        print("player1=player2")
        R = replay()
        if R == 0:
            break
        else:
            t = testboard



