from pyswip import Prolog


def canBuildDouble3Threat(board, player='x'):
    prolog = Prolog()
    prolog.consult('Gomoku.pl')
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query('canBuildDouble3Threat({}, {}, X, Y).'
                          .format(player, board))]

    return moves


def opponentCanBuildDouble3Threat(board, player='o'):
    prolog = Prolog()
    prolog.consult('Gomoku.pl')
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query('opponentCanBuildDouble3Threat({}, {}, X, Y).'
                          .format(player, board))]

    return moves


def testcanBuildDouble3Threat():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (2, 4) in canBuildDouble3Threat(board)


def testcanBuildDouble3Threat2():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 4) in canBuildDouble3Threat(board)


def testcanBuildDouble3Threat3():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 4) in canBuildDouble3Threat(board)


def testcanBuildDouble3Threat4():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 4) in canBuildDouble3Threat(board)


def testcanBuildDouble3Threat5():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'o', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 4) not in canBuildDouble3Threat(board)


def testcanBuildDouble3Threat6():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (3, 5) not in canBuildDouble3Threat(board)


def testcanBuildDouble3Threat7():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'X', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (4, 5) not in canBuildDouble3Threat(board)


def testblockDouble3Threat():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 4) in opponentCanBuildDouble3Threat(board)
