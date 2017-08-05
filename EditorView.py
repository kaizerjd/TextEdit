from tkinter import Canvas


class EditorView(Canvas):
    bg_color = "#252525"
    fg_color = "#faebd7"
    font = ("courier", "15")
    cursor_id = None
    top_margin = 10
    left_margin = 10
    line_height = 20
    font_height = 15
    line_width = 9
    cursor_animated = False
    cursor_animation_speed = 750

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

    def draw_line(self, line, line_number):
        if line.id is not None:
            self.delete(line.id)
        x = self.left_margin
        y = self.top_margin + line_number * self.line_height
        line.id = self.create_text(x, y, text=line.text, font=self.font, fill=self.fg_color, anchor="nw")

    def draw_lines(self, lines):
        self.delete("all")
        self.cursor_id = None
        x = self.left_margin
        y = self.top_margin
        for line in lines:
            self.create_text(x, y, text=line, font=self.font, fill=self.fg_color, anchor="nw")
            y += self.line_height

    def draw_cursor(self):
        if self.cursor_id:
            self.delete(self.cursor_id)
            self.cursor_id = None

        cursor_position = self.controller.get_cursor_position()
        self.cursor_id = self.create_line(
            self.left_margin + self.line_width * cursor_position[1],
            self.top_margin + self.line_height * cursor_position[0],
            self.left_margin + self.line_width * cursor_position[1],
            self.top_margin + self.line_height * cursor_position[0] + self.font_height,
            fill=self.fg_color)
        if not self.cursor_animated:
            self.animate_cursor()

    def animate_cursor(self):
        self.cursor_animated = True
        if self.cursor_id:
            self.delete(self.cursor_id)
            self.cursor_id = None
        else:
            cursor_position = self.controller.get_cursor_position()
            self.cursor_id = self.create_line(
                self.left_margin + self.line_width * cursor_position[1],
                self.top_margin + self.line_height * cursor_position[0],
                self.left_margin + self.line_width * cursor_position[1],
                self.top_margin + self.line_height * cursor_position[0] + self.font_height,
                fill=self.fg_color)
        self.master.after(self.cursor_animation_speed, self.animate_cursor)
