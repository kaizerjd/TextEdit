from tkinter import Frame
from tkinter import Text
from AppMenu import AppMenu
from EditorView import EditorView
from EditorModel import EditorModel
from EditorController import EditorController


# from CharacterEditorView import EditorView
# from CharacterEditorModel import EditorModel
# from CharacterEditorController import EditorController


class Application(Frame):
    def __init__(self, title, master=None):
        Frame.__init__(self, master)
        self.master.title(title)

    def geometry(self, geometry):
        self.master.geometry(geometry)

    def lift(self):
        self.lift()


def run(profile):
    app = Application('Text Edit')
    app.geometry("1000x500+100+100")
    app.pack(fill="both", expand=1)

    menu = AppMenu(app.master)

    editor_view = EditorView(app)
    editor_model = EditorModel()
    editor_controller = EditorController(editor_model, editor_view)

    app.mainloop()


if __name__ == "__main__":
    run(False)
