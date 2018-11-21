import itertools

from gomoku.Gomoku import run
from gomoku.model import Board, Player
from gomoku.types import PlayerColor


def play():
    board = Board()
    players = [Player(PlayerColor.BLUE), Player(PlayerColor.RED)]

    run(itertools.cycle(players), board)
