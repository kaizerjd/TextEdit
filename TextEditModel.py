

class TextEditModel:

    def __init__(self):
        file = open("sample.txt")
        self.text = file.read()


class DisplayLine:
    def __init__(self):
        self.start_index = None
        self.end_index = None

    def get_length(self):
        if self.start_index is None or self.end_index is None:
            return -1
        return self.end_index - self.start_index


if __name__ == "__main__":
    t = TextEditModel()

    print("Text")
    print(t.text)

    line = DisplayLine()
    line.start_index = 0
    line.end_index = t.text.index("\n")

    print("Display Line")
    print(t.text[line.start_index:line.end_index])
