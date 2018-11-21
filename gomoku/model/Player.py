
class Player:

    @property
    def signature(self):
        return self.color.value

    def __init__(self, color=None):
        self.color = color
