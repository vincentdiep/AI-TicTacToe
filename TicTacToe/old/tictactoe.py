"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

game_over = False

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_Counter = 0
    O_Counter = 0
    for row in board:
        for value in row:
            if value == X:
                X_Counter += 1
            elif value == O:
                O_Counter += 1
    
    if X_Counter > O_Counter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # If cell is empty, add it to set of possible actions
    action_set = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_set.append((i,j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check for Invalid Move
    if action not in actions(board):
        raise Exception('Invalid Move.')
    else:
        # If player is X, mark cell with X
        if player(board) == X:
            board[action[0]][action[1]] = X
        # If player is O, mark cell with O
        else:
            board[action[0]][action[1]] = O
        return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if  winner(board) == 'X' or winner(board) == 'O':
        return True
    elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]:
        return True
    else :
        return False


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        return actions(board).pop(random.randrange(len(actions(board))))

