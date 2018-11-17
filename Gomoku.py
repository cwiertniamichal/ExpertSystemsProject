from pyswip import Prolog


def opponent(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'


def give_advice(board, player):
    prolog = Prolog()
    prolog.consult('Gomoku.pl')
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query("givePlayerAdvice({}, {}, X, Y).".format(player,
                                                                   board))]

    return moves


def print_board(board):
    for x in range(len(board)):
        print(board[x])


def main():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]
    player = 'x'

    while True:
        print_board(board)
        moves = give_advice(board, player)
        print(moves)
        x, y = input('Type x y: ').split()
        board[int(x)][int(y)] = player
        player = opponent(player)


if __name__ == '__main__':
    main()

