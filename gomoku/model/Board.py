from gomoku.model.Field import Field
from gomoku.types import FieldType, PlayerColor


class Board:
    ROWS = 10
    COLS = 10

    @property
    def printable_fields(self):
        return list(map(
            lambda row: list(map(
                lambda field: field.type.value,
                row)),
            self.fields
        ))

    def __init__(self, fields=None):
        self.fields = fields

        if self.fields is None:
            self.fields = [[Field(FieldType.EMPTY) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def get_field(self, x, y):
        return self.fields[x][y]

    def get_field_indices_from_gui(self, x, y):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.fields[row][col].x_start < x < self.fields[row][col].x_end \
                        and self.fields[row][col].y_start < y < self.fields[row][col].y_end:
                    return row, col

    def set_field_taken(self, x, y, player):
        field_types = {
            PlayerColor.BLUE: lambda: FieldType.BLUE,
            PlayerColor.RED: lambda: FieldType.RED
        }
        self.fields[x][y].type = field_types[player.color]()
