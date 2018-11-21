from enum import Enum

from gomoku.types.PlayerColor import PlayerColor


class FieldType(Enum):
    EMPTY = 'e'
    BLUE = PlayerColor.BLUE.value
    RED = PlayerColor.RED.value

