from gomoku.types import FieldType, PlayerColor


class Board:
    BOARD_ROWS = 10
    BOARD_COLS = 10

    @property
    def printable_fields(self):
        return list(map(
            lambda row: list(map(
                lambda field_type: field_type.value,
                row)),
            self.fields
        ))

    def __init__(self):
        self.fields = [[FieldType.EMPTY for _ in range(self.BOARD_COLS)] for _ in range(self.BOARD_ROWS)]

    def set_field_taken(self, x, y, player_color):
        field_types = {
            PlayerColor.BLUE: lambda: FieldType.BLUE,
            PlayerColor.RED: lambda: FieldType.RED
        }
        self.fields[x][y] = field_types[player_color]()
