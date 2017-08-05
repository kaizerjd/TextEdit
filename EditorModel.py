
class Line:
    id = None
    text = ""

    def __init__(self):
        self.id = None
        self.text = ""


class EditorModel:
    lines = []

    def __init__(self):
        line = Line()
        self.lines.insert(0, line)

    def line_length(self, line_index):
        if line_index < len(self.lines):
            line = self.lines[line_index]
            return len(line.text)
        else:
            return 0
