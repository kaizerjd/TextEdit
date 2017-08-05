from keycodes import keycodes


class EditorController():
    cursorLine = 0
    cursorPosition = 0

    def __init__(self,model,view):
        self.model = model
        self.view = view

        self.view.register(self)
        self.bindEvents()

        self.view.draw_lines(self.model.lines)
        self.view.draw_cursor()

    def getCursorPosition(self):
        return (self.cursorLine,
                self.cursorPosition)

    def keyPressed(self,event):
        debugStr = "char: {0}, keycode: {1}".format(event.char, event.keycode)
        print(debugStr)
        if(event.keycode == keycodes.left):
            self.cursorLeft()
            self.view.draw_cursor()
        elif(event.keycode == keycodes.up):
            self.cursorUp()
            self.view.draw_cursor()
        elif(event.keycode == keycodes.right):
            self.cursorRight()
            self.view.draw_cursor()
        elif(event.keycode == keycodes.down):
            self.cursorDown()
            self.view.draw_cursor()
        elif(event.keycode == keycodes.enter):
            self.newline()
            self.view.draw_cursor()
            self.view.draw_lines(self.model.lines)
        elif(event.keycode == keycodes.backspace):
            self.backspace()
            self.view.draw_cursor()
            self.view.draw_lines(self.model.lines)
        else:
            if(len(event.char) > 0):
                self.insertChar(event.char)
                self.view.draw_cursor()
                self.view.draw_lines(self.model.lines)


    def bindEvents(self):
        print("binding Events")
        self.view.bind_all("<Key>",self.keyPressed)

    def cursorRight(self):
        lineLength = self.model.lineLength(self.cursorLine)
        if(self.cursorPosition  < lineLength):
            self.cursorPosition += 1
        else:
            if(self.cursorLine + 1 < len(self.model.lines)):
                self.cursorLine += 1
                self.cursorPosition = 0

    def cursorLeft(self):
        if(self.cursorPosition - 1 >= 0):
            self.cursorPosition -= 1
        else:
            if(self.cursorLine - 1 >= 0):
                self.cursorLine -= 1
                self.cursorPosition = self.model.lineLength(self.cursorLine)

    def cursorUp(self):
        if(self.cursorLine - 1 >= 0):
            self.cursorLine -= 1
            if(self.cursorPosition > self.model.lineLength(self.cursorLine)):
                self.cursorPosition = self.model.lineLength(self.cursorLine)

    def cursorDown(self):
        if(self.cursorLine + 1 < len(self.model.lines)):
            self.cursorLine += 1
            if(self.cursorPosition > self.model.lineLength(self.cursorLine)):
                self.cursorPosition = self.model.lineLength(self.cursorLine)

    def backspace(self):
        if(self.cursorPosition == 0):
            if(self.cursorLine > 0):
                line1 = self.model.lines[self.cursorLine -1]
                line2 = self.model.lines[self.cursorLine]
                line = line1 + line2
                self.model.lines[self.cursorLine-1] = line
                del self.model.lines[self.cursorLine]
                self.cursorLine -= 1
                self.cursorPosition = len(line1)
        else:
            line = self.model.lines[self.cursorLine]
            line = line[:self.cursorPosition-1] + line[self.cursorPosition:]
            self.model.lines[self.cursorLine] = line
            self.cursorPosition = self.cursorPosition - 1

    def newline(self):
        line1 = self.model.lines[self.cursorLine][:self.cursorPosition]
        line2 = self.model.lines[self.cursorLine][self.cursorPosition:]
        self.model.lines[self.cursorLine] = line1
        self.cursorLine += 1
        self.cursorPosition = 0
        self.model.lines.insert(self.cursorLine, line2)

    def insertChar(self, char):
        line = self.model.lines[self.cursorLine]
        line = line[:self.cursorPosition ] + char + line[self.cursorPosition:]
        self.model.lines[self.cursorLine] = line
        self.cursorPosition = self.cursorPosition + 1