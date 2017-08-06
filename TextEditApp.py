from tkinter import Frame
from AppMenu import AppMenu
from CharacterEditorView import EditorView
from CharacterEditorModel import EditorModel
from CharacterEditorController import EditorController


class Application(Frame):
    def __init__(self, title, master=None):
        Frame.__init__(self, master)
        self.master.title(title)

    def geometry(self, geometry):
        self.master.geometry(geometry)


app = Application('Text Edit')
app.geometry("1000x500+100+100")
app.pack(fill="both", expand=1)

menu = AppMenu(app.master)

editorView = EditorView(app)
editorModel = EditorModel()
editorController = EditorController(editorModel, editorView)

app.mainloop()
