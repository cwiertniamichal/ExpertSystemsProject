import tkinter as tk

from gomoku.types import FieldType, PlayerColor


class TkBoard(tk.Frame):
    FIELD_SIZE = 64

    BACKGROUND_COLOR = "#ffdd99"
    FIELD_BORDER_COLOR = "black"
    FIELD_IN_WINNING_FIVE_COLOR = "#ff9900"

    HIGHLIGHT_BORDER_COLORS = {
        PlayerColor.BLUE: "#66b3ff",
        PlayerColor.RED: "#ff6633"
    }

    STONE_COLORS = {
        FieldType.BLUE: "#0066cc",
        FieldType.RED: "#b32d00"
    }

    def __init__(self, parent=None, players=None, board=None, get_advice=None, has_any_player_five_stones=None):
        self.parent = parent

        self.players = players
        self.current_player = None

        self.board = board
        self.cols = board.COLS
        self.rows = board.ROWS

        self.get_advice = get_advice
        self.has_any_player_five_stones = has_any_player_five_stones

        canvas_with = self.cols * self.FIELD_SIZE
        canvas_height = self.rows * self.FIELD_SIZE

        super().__init__(parent)

        self.canvas = tk.Canvas(self, width=canvas_with, height=canvas_height, background=self.BACKGROUND_COLOR)
        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)

        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.click)

        self.set_current_player()

    def refresh(self, event=None):
        if event:
            xsize = int((event.width - 1) / self.cols)
            ysize = int((event.height - 1) / self.rows)
            self.size = min(xsize, ysize)

        self.canvas.delete("field")
        self.canvas.delete("stone")
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size - 3
                y2 = y1 + self.size - 3

                field = self.board.get_field(row, col)
                field.x_start = x1
                field.x_end = x2
                field.y_start = y1
                field.y_end = y2

                field_border_color = self.FIELD_IN_WINNING_FIVE_COLOR if field.is_in_winning_five else \
                    (self.HIGHLIGHT_BORDER_COLORS[self.current_player.color] if field.is_recommended else self.FIELD_BORDER_COLOR)

                field_border_width = 3 if field.is_recommended or field.is_in_winning_five else 1
                self.canvas.create_rectangle(x1, y1, x2, y2, outline=field_border_color, width=field_border_width,
                                             fill=self.BACKGROUND_COLOR, tags="field")
                if field.type is not FieldType.EMPTY:
                    stone_color = self.STONE_COLORS[field.type]
                    stone_offset = 5
                    self.canvas.create_oval(x1 + stone_offset, y1 + stone_offset, x2 - stone_offset, y2 - stone_offset,
                                            outline=stone_color, fill=stone_color, tags="stone")

    def click(self, event):
        x, y = self.board.get_field_indices_from_gui(event.x, event.y)
        if x >= 0 and y >= 0:
            if self.board.set_field_taken(x, y, self.current_player):
                if self.should_finish_game():
                    self.finish_game()
                else:
                    self.set_current_player()
                self.refresh()

    def set_current_player(self):
        self.current_player = next(self.players)
        recommended_fields = self.get_advice(self.board.printable_fields, self.current_player.signature)

        print(recommended_fields)
        if len(recommended_fields) > 0:
            self.board.set_field_recommended(recommended_fields[0][0], recommended_fields[0][1])
        else:
            self.board.reset_recommended_fields()

    def should_finish_game(self):
        return self.has_any_player_five_stones(self.board)

    def finish_game(self):
        self.canvas.unbind("<Button-1>")
