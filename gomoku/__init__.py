import itertools

from gomoku.Gomoku import main
from gomoku.model import Board, Player
from gomoku.types import PlayerColor


def play():
    board = Board()
    players = [Player(PlayerColor.BLUE), Player(PlayerColor.RED)]

    main(itertools.cycle(players), board)
