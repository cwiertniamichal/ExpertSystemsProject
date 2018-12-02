from gomoku.types import FieldType


class Field:

    @property
    def is_empty(self):
        return self.type is FieldType.EMPTY

    def __init__(self, field_type=None):
        self.type = field_type

        self.x_start = None
        self.x_end = None

        self.y_start = None
        self.y_end = None

        self.is_recommended = False

        self.is_in_winning_five = False
