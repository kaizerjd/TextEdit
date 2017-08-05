from tkinter import Menu

class AppMenu(Menu):
    def __init__(self, master):
        Menu.__init__(self, master)

        filemenu = Menu(self)
        filemenu.add_command(label="Quit",command=master.quit)
        self.add_cascade(label="File",menu=filemenu)

        master.config(menu = self)