import tkinter as tk

from gomoku.types import FieldType


class TkBoard(tk.Frame):
    FIELD_SIZE = 64

    BACKGROUND_COLOR = "#ffdd99"
    FIELD_BORDER_COLOR = "black"

    STONE_COLORS = {
        FieldType.BLUE: "#0066cc",
        FieldType.RED: "#b32d00"
    }

    def __init__(self, parent=None, players=None, board=None):
        self.parent = parent

        self.players = players
        self.current_player = next(self.players)

        self.board = board
        self.cols = board.COLS
        self.rows = board.ROWS

        canvas_with = self.cols * self.FIELD_SIZE
        canvas_height = self.rows * self.FIELD_SIZE

        super().__init__(parent)

        self.canvas = tk.Canvas(self, width=canvas_with, height=canvas_height, background=self.BACKGROUND_COLOR)
        self.canvas.pack(side="top", fill="both", anchor="c", expand=True)

        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.click)

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
                x2 = x1 + self.size
                y2 = y1 + self.size

                field = self.board.get_field(row, col)
                field.x_start = x1
                field.x_end = x2
                field.y_start = y1
                field.y_end = y2

                self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.FIELD_BORDER_COLOR,
                                             fill=self.BACKGROUND_COLOR, tags="field")
                if field.type is not FieldType.EMPTY:
                    stone_color = self.STONE_COLORS[field.type]
                    stone_offset = 5
                    self.canvas.create_oval(x1 + stone_offset, y1 + stone_offset, x2 - stone_offset, y2 - stone_offset,
                                            outline=stone_color, fill=stone_color, tags="stone")

    def click(self, event):
        x, y = self.board.get_field_indices_from_gui(event.x, event.y)
        self.board.set_field_taken(x, y, self.current_player)
        self.refresh()
        self.change_player()

    def change_player(self):
        self.current_player = next(self.players)
