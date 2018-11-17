from pyswip import Prolog


def can_win_in_one_move(board, player='x'):
    prolog = Prolog()
    prolog.consult('Gomoku.pl')
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query('canWinInOneMove({}, {}, X, Y).'.format(player,
                                                                  board))]

    return moves


def opponentCanWinInOneMove(board, player='o'):
    prolog = Prolog()
    prolog.consult('Gomoku.pl')
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query('opponentCanWinInOneMove({}, {}, X, Y).'
                          .format(player, board))]

    return moves


def test_can_win_in_one_move():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'x', 'x', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (1, 5) in can_win_in_one_move(board)


def test_can_win_in_one_move2():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'x', 'x', 'e', 'x', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (1, 4) in can_win_in_one_move(board)


def test_can_win_in_one_move3():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'x', 'x', 'x', 'o', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (1, 0) in can_win_in_one_move(board)


def test_can_win_in_one_move4():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 1) in can_win_in_one_move(board)


def test_can_win_in_one_move5():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 5) in can_win_in_one_move(board)


def test_can_win_in_one_move6():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 0) in can_win_in_one_move(board)


def test_block_win_in_one_move():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'x', 'x', 'x', 'o', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (1, 0) in opponentCanWinInOneMove(board)


def test_block_win_in_one_move2():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['x', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (2, 3) in opponentCanWinInOneMove(board)
