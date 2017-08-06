from CharacterEditorModel import EditorModel
from random import randint

class EditorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.register(self)
        self.draw_all()

    def draw_all(self):
        x = 0
        y = 0
        for c in self.model.chars:
            if c == '\n':
                x = 0
                y += 1
            else:
                r = randint(0, 1)
                self.view.draw_char(c, x, y, r == 1)
                x += 1
