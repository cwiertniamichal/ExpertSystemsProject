class Field:
    def __init__(self, field_type=None):
        self.type = field_type

        self.x_start = None
        self.x_end = None

        self.y_start = None
        self.y_end = None

        self.is_recommended = False
