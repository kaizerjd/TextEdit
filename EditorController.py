from keycodes import keycodes
from EditorModel import *


class EditorController:
    cursorLine = 0
    cursorPosition = 0

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.register(self)
        self.bind_events()
        self.draw_all_lines()
        self.view.draw_cursor()

    def get_cursor_position(self):
        return (self.cursorLine,
                self.cursorPosition)

    def draw_all_lines(self):
        self.view.delete("all")
        for i in range(0, len(self.model.lines)):
            self.view.draw_line(self.model.lines[i], i)

    def draw_current_line(self):
        self.view.draw_line(self.model.lines[self.cursorLine], self.cursorLine)

    def key_pressed(self, event):
        debug_str = "char: {0}, keycode: {1}".format(event.char, event.keycode)
        print(debug_str)
        if event.keycode == keycodes.left:
            self.cursor_left()
            self.view.draw_cursor()
        elif event.keycode == keycodes.up:
            self.cursor_up()
            self.view.draw_cursor()
        elif event.keycode == keycodes.right:
            self.cursor_right()
            self.view.draw_cursor()
        elif event.keycode == keycodes.down:
            self.cursor_down()
            self.view.draw_cursor()
        elif event.keycode == keycodes.enter:
            self.newline()
            self.view.draw_cursor()
            self.draw_all_lines()
        elif event.keycode == keycodes.backspace:
            self.backspace()
            self.view.draw_cursor()
            self.draw_all_lines()
        else:
            if len(event.char) > 0:
                self.insert_char(event.char)
                self.view.draw_cursor()
                self.draw_current_line()

    def bind_events(self):
        print("binding Events")
        self.view.bind_all("<Key>", self.key_pressed)

    def cursor_right(self):
        line_length = self.model.line_length(self.cursorLine)
        if self.cursorPosition  < line_length:
            self.cursorPosition += 1
        elif self.cursorLine + 1 < len(self.model.lines):
                self.cursorLine += 1
                self.cursorPosition = 0

    def cursor_left(self):
        if self.cursorPosition - 1 >= 0:
            self.cursorPosition -= 1
        else:
            if self.cursorLine - 1 >= 0:
                self.cursorLine -= 1
                self.cursorPosition = self.model.line_length(self.cursorLine)

    def cursor_up(self):
        if self.cursorLine - 1 >= 0:
            self.cursorLine -= 1
            if self.cursorPosition > self.model.line_length(self.cursorLine):
                self.cursorPosition = self.model.line_length(self.cursorLine)

    def cursor_down(self):
        if self.cursorLine + 1 < len(self.model.lines):
            self.cursorLine += 1
            if self.cursorPosition > self.model.line_length(self.cursorLine):
                self.cursorPosition = self.model.line_length(self.cursorLine)

    def backspace(self):
        if self.cursorPosition == 0:
            if self.cursorLine > 0:
                text1 = self.model.lines[self.cursorLine -1].text
                text2 = self.model.lines[self.cursorLine].text
                text = text1 + text2
                line = Line()
                line.text = text
                self.model.lines[self.cursorLine-1] = line
                del self.model.lines[self.cursorLine]
                self.cursorLine -= 1
                self.cursorPosition = len(text1)
        else:
            text = self.model.lines[self.cursorLine].text
            text = text[:self.cursorPosition-1] + text[self.cursorPosition:]
            self.model.lines[self.cursorLine].text = text
            self.cursorPosition = self.cursorPosition - 1

    def newline(self):
        text1 = self.model.lines[self.cursorLine].text[:self.cursorPosition]
        text2 = self.model.lines[self.cursorLine].text[self.cursorPosition:]
        self.model.lines[self.cursorLine].text = text1
        self.cursorLine += 1
        self.cursorPosition = 0
        line2 = Line()
        line2.text = text2
        self.model.lines.insert(self.cursorLine, line2)

    def insert_char(self, char):
        line = self.model.lines[self.cursorLine]
        line.text = line.text[:self.cursorPosition] + char + line.text[self.cursorPosition:]
        self.model.lines[self.cursorLine] = line
        self.cursorPosition = self.cursorPosition + 1
