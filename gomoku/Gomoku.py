from pyswip import Prolog
from tkinter import Tk

import prolog.KnowledgeBase as KnowledgeBase
from gomoku.ui import TkBoard


def get_advice(board, player):
    prolog = Prolog()
    prolog.consult(KnowledgeBase.PATH)
    moves = [(soln['X'], soln['Y'], soln['PredName']) for soln in
             prolog.query(KnowledgeBase.GIVE_PLAYER_ADVICE_PREDICATE.format(player, board))]

    return moves


def print_board(board):
    for x in range(len(board)):
        print(board[x])


def run(players, board):
    root = Tk()
    root.title("Gomoku")

    tk_board = TkBoard(root, players, board, get_advice)
    tk_board.pack(side="top", fill="both", expand="true")
    root.mainloop()
