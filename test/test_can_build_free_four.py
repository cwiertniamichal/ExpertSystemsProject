import prolog.KnowledgeBase as KnowledgeBase
from pyswip import Prolog


def canBuildFree4(board, player='x'):
    prolog = Prolog()
    prolog.consult(KnowledgeBase.PATH)
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query(KnowledgeBase.CAN_BUILD_FREE_4_PREDICATE.format(player, board))]

    return moves


def opponentCanBuildFree4(board, player='o'):
    prolog = Prolog()
    prolog.consult(KnowledgeBase.PATH)
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query(KnowledgeBase.OPPONENT_CAN_BUILD_FREE_4_PREDICATE.format(player, board))]

    return moves


def test_can_build_free_four():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'x', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (1, 5) in canBuildFree4(board) or (1, 1) in canBuildFree4(board)


def test_can_build_free_four2():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'x', 'e', 'x', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (1, 4) in canBuildFree4(board)


def test_can_build_free_four3():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'x', 'x', 'e', 'o'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (1, 1) in canBuildFree4(board)


def test_can_build_free_four4():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'o', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (3, 1) in canBuildFree4(board)


def test_can_build_free_four5():
    board = [
        ['o', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'o', 'x', 'o', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'o', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (5, 5) in canBuildFree4(board)


def test_can_build_free_four6():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (4, 1) in canBuildFree4(board)


def test_block_free_four():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'x', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert ((1, 5) in opponentCanBuildFree4(board) or
            (1, 1) in opponentCanBuildFree4(board))


def test_block_free_four2():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'x', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'o', 'e', 'e', 'e', 'e', 'e'],
    ]

    assert (3, 1) in opponentCanBuildFree4(board)
