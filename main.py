import random
import copy
import sys


def main():
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    # for b1 in generator(board, True):
    #     for b2 in generator(b1, False):
    #         display_board(b2)
    #         print(" ")
    # g = generator(board, True)
    # print(g)
    # b1_1 = next(g)
    # display_board(b1_1)
    # sys.exit()
    display_board(board)

    turn = True

    while winner(board) is None:
        if turn:
            player_turn(board)


        else:
            comp_turn(board)
        display_board(board)

        turn = not turn

    if winner(board) == 'x':
        print("Player won")
    elif winner(board) == 'o':
        print("Computer Won")
    else:
        print("stalemate")


def winner(board):
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[1] != "-":
            return row[1]
    for j in range(len(board)):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[1][j] != "-":
            return board[1][j]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != "-":
        return board[1][1]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != "-":
        return board[1][1]
    for row in board:
        for val in row:
            if val == "-":
                return None
    return "s"


def player_turn(board):
    choice = input("Choose your move: ").upper()
    row = ord(choice[0]) - 65
    col = ord(choice[1]) - ord("1")
    board[row][col] = 'x'


def comp_turn(board):
    # while True:
    #     row = random.randint(0, 2)
    #     col = random.randint(0, 2)
    #     if board[row][col] is None:
    #         board[row][col] = 'o'
    #         return
    score, state = minimax(board)
    for i in range(len(board)):
        board[i] = state[i]


def display_board(board):
    for row in board:
        print(row)


def generator(board, turn):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "-":
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = "x" if turn else "o"
                yield board_copy

def scoring(board):
    s = winner(board)

    if s == 'x':
        return 100
    if s == 'o':
        return -100
    if s == 's':
        return 0
    return None

def minimax(board):
    score = scoring(board)
    if score is not None:
        return score, None
    scores = []
    states = list(generator(board, False))
    for state in states:
        scores.append(maximin(state)[0])
    i = 0
    for j in range(1, len(scores)):
        if scores[j] < scores[i]:
            i = j

    return scores[i], states[i]

def maximin(board):
    score = scoring(board)
    if score is not None:
        return score, None
    scores = []
    states = list(generator(board, True))
    for state in states:
        scores.append(minimax(state)[0])
    i = 0
    for j in range(1, len(scores)):
        if scores[j] > scores[i]:
            i = j

    return scores[i], states[i]







if __name__ == '__main__':
    main()
