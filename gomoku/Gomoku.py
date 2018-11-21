from pyswip import Prolog

import prolog.KnowledgeBase as KnowledgeBase


def give_advice(board, player):
    prolog = Prolog()
    prolog.consult(KnowledgeBase.PATH)
    moves = [(soln['X'], soln['Y']) for soln in
             prolog.query(KnowledgeBase.GIVE_PLAYER_ADVICE_PREDICATE.format(player, board))]

    return moves


def print_board(board):
    for x in range(len(board)):
        print(board[x])


def main(players, board):
    while True:
        player = next(players)
        print_board(board.printable_fields)
        moves = give_advice(board.printable_fields, player.signature)
        print(moves)
        x, y = input('Type x y: ').split()
        board.set_field_taken(int(x), int(y), player.color)
