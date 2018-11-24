import prolog.KnowledgeBase as KnowledgeBase
from pyswip import Prolog
import os


def opponent_can_build_free_4(board, player='o'):
    prolog = Prolog()
    prolog.consult(os.path.join('..', KnowledgeBase.PATH))
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query(KnowledgeBase.OPPONENT_CAN_BUILD_FREE_4_PREDICATE
                          .format(player, board))]
    print(KnowledgeBase.OPPONENT_CAN_BUILD_FREE_4_PREDICATE
                          .format(player, board))
    return moves


def opponent_can_build_double_3_threat(board, player='o'):
    prolog = Prolog()
    prolog.consult(os.path.join('..', KnowledgeBase.PATH))
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query(KnowledgeBase.OPPONENT_CAN_BUILD_DOUBLE_3_THREAD_PREDICATE
                          .format(player, board))]
    return moves


def test_block_free_four_and_win():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'x', 'x', 'x', 'e', 'e'],
        ['e', 'o', 'e', 'e', 'e', 'o', 'e'],
        ['e', 'o', 'e', 'e', 'e', 'o', 'e'],
        ['e', 'o', 'e', 'e', 'e', 'o', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'o', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e']
    ]

    moves = opponent_can_build_free_4(board)
    for move in moves:
        assert move == (3, 5)


def test_block_free_four_and_build_free_4():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'o', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'o', 'o', 'e', 'e', 'e'],
        ['e', 'e', 'o', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'o', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'o', 'o', 'o', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    ]

    moves = opponent_can_build_free_4(board)
    assert [(6, 6)] == moves


def test_block_free_four_and_build_double_3_threat():
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'o', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'o', 'o', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'o', 'x', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'o', 'e', 'x', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'x', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'o', 'o', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    ]

    moves = opponent_can_build_free_4(board)
    assert [(3, 3)] == moves
