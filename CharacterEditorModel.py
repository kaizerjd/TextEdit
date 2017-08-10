
class EditorModel:
    chars = []

    def __init__(self):
        for i in range(0, 100):
            for j in range(0, 100):
                self.chars.append('a')
            self.chars.append('\n')
