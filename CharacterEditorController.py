from CharacterEditorModel import EditorModel
from random import randint

class EditorController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.register(self)
        self.view.draw_all_chars(self.model.chars)

