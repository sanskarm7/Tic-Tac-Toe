import pprint


def main():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    pprint.pprint(board)

    turn = True

    while winner(board) is None:
        if turn:
            player_turn(board)

        else:
            comp_turn(board)
        print_board(board)


def winner(board):
    pass


def player_turn(board):
    choice = input("Choose your move: ")
    row = ord(choice[0]) - 65
    col = ord(choice[1]) - ord("1")
    board[row][col] = 'x'


def comp_turn(board):
    pass


def print_board(board):
    pprint.pprint(board)


if __name__ == '__main__':
    main()
