from gomoku.model.Field import Field
from gomoku.types import FieldType, PlayerColor


class Board:
    ROWS = 10
    COLS = 10

    @property
    def printable_fields(self):
        return [[field.type.value for field in row] for row in self.fields]

    @property
    def fields_with_indices(self):
        return [[(field, (x, y)) for y, field in enumerate(row)] for x, row in enumerate(self.fields)]

    @property
    def has_five_in_horizontally(self):
        five_in_row = _find_five_in_rows(self.fields_with_indices, 1)
        self.set_fields_in_winning_five(five_in_row)
        return len(five_in_row) == 5

    @property
    def has_five_in_vertically(self):
        transposed_fields_with_indices = [list(columns) for columns in zip(*self.fields_with_indices)]
        five_in_row = _find_five_in_rows(transposed_fields_with_indices, 0)
        self.set_fields_in_winning_five(five_in_row)
        return len(five_in_row) == 5

    @property
    def has_five_diagonally(self):
        five_in_row = _find_five_diagonally(self.fields_with_indices)
        self.set_fields_in_winning_five(five_in_row)
        return len(five_in_row) == 5

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
        return -1, -1

    def set_field_taken(self, x, y, player):
        field_types = {
            PlayerColor.BLUE: lambda: FieldType.BLUE,
            PlayerColor.RED: lambda: FieldType.RED
        }

        field = self.fields[x][y]

        if field.type is FieldType.EMPTY:
            self.fields[x][y].type = field_types[player.color]()
            return True
        else:
            return False

    def reset_recommended_fields(self):
        for row in range(self.ROWS):
            for cols in range(self.COLS):
                self.fields[row][cols].is_recommended = False

    def set_field_recommended(self, x, y):
        self.reset_recommended_fields()

        if self.fields[x][y].type is FieldType.EMPTY:
            self.fields[x][y].is_recommended = True

    def set_fields_in_winning_five(self, coordinates):
        for x, y in coordinates:
            self.fields[x][y].is_in_winning_five = True


def _get_non_empty_fields(fields):
    return list(filter(
        lambda row: len(row) > 0,
        [list(filter(lambda field_with_index: not field_with_index[0].is_empty, row)) for row in fields]
    ))


def _find_five_in_rows(fields, coordinate_index):
    non_empty_fields = _get_non_empty_fields(fields)

    grouped_non_empty_fields = [{FieldType.BLUE: [], FieldType.RED: []} for _ in non_empty_fields]
    for index, row in enumerate(non_empty_fields):
        for field_with_index in row:
            grouped_non_empty_fields[index][field_with_index[0].type].append(field_with_index[1])

    for field in grouped_non_empty_fields:
        for _, row in field.items():
            five_in_row = _find_five_in_row(row, coordinate_index)
            if len(five_in_row) == 5:
                return five_in_row

    return []


def _find_five_in_row(row, coordinate_index):
    five_in_row = []
    for field in row:
        if len(five_in_row) == 0 or field[coordinate_index] - five_in_row[-1][coordinate_index] == 1:
            five_in_row.append(field)
        else:
            five_in_row.clear()
    return five_in_row if len(five_in_row) == 5 else []


def _find_five_diagonally(fields):
    def _get_rows(grid):
        return [[col for col in row] for row in grid]

    def _get_cols(grid):
        return zip(*grid)

    def _get_backward_diagonals():
        grid_of_nones = [None] * (len(fields) - 1)
        grid = [grid_of_nones[i:] + row + grid_of_nones[:i] for i, row in enumerate(_get_rows(fields))]
        return [[col for col in row if col is not None] for row in _get_cols(grid)]

    def _get_forward_diagonals():
        grid_of_nones = [None] * (len(fields) - 1)
        grid = [grid_of_nones[:i] + row + grid_of_nones[i:] for i, row in enumerate(_get_rows(fields))]
        return [[col for col in row if col is not None] for row in _get_cols(grid)]

    backward_diagonals = _get_backward_diagonals()
    forward_diagonals = _get_forward_diagonals()

    five_in_row_backwards = _search_on_diagonals(backward_diagonals)
    five_in_row_forwards = _search_on_diagonals(forward_diagonals)

    return five_in_row_backwards if len(five_in_row_backwards) == 5 else \
        (five_in_row_forwards if len(five_in_row_forwards) == 5 else [])


def _search_on_diagonals(diagonals):
    non_empty_fields = _get_non_empty_fields(diagonals)

    grouped_non_empty_fields = [{FieldType.BLUE: [], FieldType.RED: []} for _ in non_empty_fields]
    for index, row in enumerate(non_empty_fields):
        for field_with_index in row:
            grouped_non_empty_fields[index][field_with_index[0].type].append(field_with_index[1])

    for field in grouped_non_empty_fields:
        for _, diagonal in field.items():
            five_in_row = _find_five_in_row_diagonally(diagonal)
            if len(five_in_row) == 5:
                return five_in_row

    return []


def _find_five_in_row_diagonally(diagonal):
    five_in_row = []
    for field in diagonal:
        if len(five_in_row) == 0 or \
                (abs(field[0] - five_in_row[-1][0]) == 1 and abs(field[1] - five_in_row[-1][1]) == 1):
            five_in_row.append(field)
        else:
            five_in_row.clear()
    return five_in_row if len(five_in_row) == 5 else []
