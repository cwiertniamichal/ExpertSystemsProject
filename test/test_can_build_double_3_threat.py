import prolog.KnowledgeBase as KnowledgeBase
from pyswip import Prolog
import os


def canBuildDouble3Threat(board, player='x'):
    prolog = Prolog()
    prolog.consult(os.path.join('..', KnowledgeBase.PATH))
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query(KnowledgeBase.CAN_BUILD_DOUBLE_3_THREAD_PREDICATE.format(player, board))]

    return moves


def opponentCanBuildDouble3Threat(board, player='o'):
    prolog = Prolog()
    prolog.consult(os.path.join('..', KnowledgeBase.PATH))
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query(KnowledgeBase.OPPONENT_CAN_BUILD_DOUBLE_3_THREAD_PREDICATE.format(player, board))]

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
