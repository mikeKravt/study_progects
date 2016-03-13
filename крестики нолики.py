# -*- coding: utf-8 -*-
#Игра в Крестики-нолики с компьютером
#Global const
import random
X = "X"
O = "0"
EMPTY = " "
TIE = "НИЧЬЯ"
NUM_SQUARES = 9
#FUNCTIONS
def display_instruct():
    '''Function for output instruction'''
    print(
    """
    Добро пожаловать в игру КРЕСТИКИ-НОЛИКИ.
    Вам предоставлена возможность играть против копмьютера.
    \nЧтобы сделать ход, введите число от 0 до 8.
    Числа соответствут полям на доске, как показано ниже:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """
    )
def ask_yes_no(question):
    '''Function asks the question, the answer to be yes or no'''
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
def ask_number(question, low, high):
    '''Function for the number of band request'''
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
def pieces():
    '''Function for detection the first move'''
    go_first = ask_yes_no("Желаете ходить первым? Ответ (Y/N): ")
    if go_first == "y":
        print("\nПервый ход Ваш: ходите КРЕСТИКАМИ")
        human = X
        computer = 0
    else:
        print("\nНачинает компьютер. После него Вы ходите НОЛИКАМИ")
        computer = X
        human = 0
    return computer, human
def new_board():
    '''Function to create a new game board'''
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
def display_board(board):
    '''Function display screen on the game board'''
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
def legal_moves(board):
    '''Functoin to create a list of available courses'''
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
def winner(board):
    '''Winner determination function'''
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
        return None
def human_move(board, human):
    '''Human running function'''
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Ваш ход. Выберети одно из полей от 0 до 8: ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято. Выберете другое.\n")
    return move
def computer_move(board, computer, human):
    '''Computer running function'''
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Компьютер выбирает поле номер ", end = " ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
    board[move] = EMPY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def next_turn(turn):
    '''Stroke transition function'''
    if turn == X:
        return 0
    else:
        return X
def congrat_winner(the_winner, computer, human):
    '''Function for congratulations to the winner'''
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победил КОМПЬЮТЕР!\n")
    elif the_winner == human:
        print("Вы победили!\n")
    elif the_winner == TIE:
        print("НИЧЬЯ!\n")
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
#START PROGRAM
main()
input("\nНажмите Enter, чтобы выйти.")
    
    
    











    

