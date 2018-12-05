from pyswip import Prolog
from tkinter import Tk

import prolog.KnowledgeBase as KnowledgeBase
from gomoku.ui import TkBoard


def set_board_size(board):
    prolog = Prolog()
    prolog.consult(KnowledgeBase.PATH)
    prolog.assertz(KnowledgeBase.BOARD_SIZE_FACT.format(board.ROWS, board.COLS))


def get_advice(board, player):
    prolog = Prolog()
    prolog.consult(KnowledgeBase.PATH)
    moves = [(soln['X'], soln['Y'], soln['PredName']) for soln in
             prolog.query(KnowledgeBase.GIVE_PLAYER_ADVICE_PREDICATE.format(player, board))]

    return moves


def has_any_player_five_stones(board):
    return board.has_five_in_horizontally or board.has_five_in_vertically or board.has_five_diagonally


def run(players, board):
    root = Tk()
    root.title("Gomoku")

    set_board_size(board)

    tk_board = TkBoard(root, players, board, get_advice, has_any_player_five_stones)
    tk_board.pack(side="top", fill="both", expand="true")
    root.mainloop()
