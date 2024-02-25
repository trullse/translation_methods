class Token:
    def __init__(self, pos, index, text: str, info, value=None):
        self.index = index
        self.pos = pos
        self.text = text
        self.info = info
        self.value = value

    def __str__(self):
        return self.text
