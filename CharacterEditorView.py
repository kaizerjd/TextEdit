from tkinter import Canvas


class EditorView(Canvas):
    bg_color = "#252525"
    fg_color = "#faebd7"
    font = ("courier", "15")
    left_margin = 10
    top_margin = 10
    line_height = 20
    line_width = 9

    def __init__(self, master):
        Canvas.__init__(self, master, highlightthickness=0)
        self.master = master
        self.initialise_ui()
        self.controller = None

    def initialise_ui(self):
        self.config(bg=self.bg_color)
        self.pack(fill="both", expand=1)

    def register(self, controller):
        self.controller = controller

    def draw_char(self, char, x, y, selected = False):
        screen_x = self.left_margin + x * self.line_width
        screen_y = self.top_margin + y * self.line_height
        id = self.create_text(screen_x, screen_y,
            text=char,
            font=self.font,
            fill=self.fg_color,
            anchor="nw")
        if selected:
            bbox = self.bbox(id)
            self.delete(id)
            self.create_rectangle(bbox, fill="blue", outline="blue")
            self.create_text(screen_x, screen_y,
                             text=char,
                             font=self.font,
                             fill=self.fg_color,
                             anchor="nw")
