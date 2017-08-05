


class EditorModel():
    lines = [""]

    def lineLength(self, lineIndex):
        if(lineIndex < self.lines.__len__()):
            line = self.lines[lineIndex]
            return len(line)
        else:
            return 0

class Line():
    id = None
    text = ""