"""
Tic Tac Toe Player
"""

import math
import copy
import random
from shutil import move

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Initialize number of empty cells
    emptyCells = 0
    # Count number of empty cells
    for row in board:
        for col in row:
            if col is EMPTY:
                emptyCells += 1
    # If odd number of empty Cells:
    if emptyCells % 2 == 1:
        # X's turn
        return X
    else:
        # Otherwise O's turn
        return O
    


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
    # Make a deep copy of the board before making any changes
    board_copy = copy.deepcopy(board)
    # Check for Invalid Move
    if (action[0],action[1]) not in actions(board):
        raise Exception('Invalid Move.')
    else:
        board_copy[action[0]][action[1]] = player(board)
    
    return board_copy
        

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(3):
        # Checks for win state per column
        if board[0][x] == board[1][x] == board[2][x]:
            return board[0][x]
        # Checks for win state per row
        if board[x][0] == board[x][1] == board[x][2]:
            return board[x][0]
        # Checks for win state diagonally
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if game is won by either Player X or Player O
    if  winner(board) == X or winner(board) == O:
        return True

    # Check if all cells have been filled without anyone winning
    elif len(actions(board)) == 0:
        return True
    else:
        return False


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check if the game is over
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Get the current player
    currentPlayer = player(board)
    # Return None is there are no available moves
    if terminal(board):
        return None
    # X will always be Maximizer
    if currentPlayer is X:
        bestScore = -99999
        bestMove = []
        openSpaces = actions(board)
        for possibleMoves in openSpaces:
            # Create simulated board with player making some move 'a'
            possibleBoard = result(board,possibleMoves)
            # Get enemy-optimal movement from simulated board
                # Issue - if possibleBoard is terminal, bad things happen
            #if possibleBoard is terminal: return move(?)
            if terminal(possibleBoard):
                return possibleMoves
            # If !terminal(possibleBoard), then the enemy is able to make some move
            enemyMove = minimax(possibleBoard)
            enemyBoard = result(possibleBoard,enemyMove)
            # If the simulation's score is better than current bestScore:
            if score(enemyBoard) > bestScore:
                # New bestScore is simulation's score
                bestScore = score(enemyBoard)
                # set new best move as move 'a'
                bestMove = possibleMoves
    # O will always be Minimizer
    elif currentPlayer is O:
        bestScore = 99999
        bestMove = []
        openSpaces = actions(board)
        for possibleMoves in openSpaces:
            # Create simulated board with player making some move 'b'
            possibleBoard = result(board,possibleMoves)
            # Get enemy-optimal movement from simulated board
                ## Issue - if possibleBoard is terminal, bad things happen
            #if possibleBoard is terminal: return move(?)
                ## I think this works because it needs to return a move
                ## to the function call above itself
            if terminal(possibleBoard):
                return possibleMoves
            # If !terminal(possibleBoard), then the enemy can make some move
            enemyMove = minimax(possibleBoard)
            enemyBoard = result(possibleBoard,enemyMove)
            # If the enemy's best score is better than curr bestScore:
            if score(enemyBoard) < bestScore:
                # New bestScore is enemy Score
                bestScore = score(enemyBoard)
                # Set new best move as move 'b'
                bestMove = possibleMoves

    return bestMove

