class Token:
    def __init__(self, pos, index, text, info):
        self.index = index
        self.pos = pos
        self.text = text
        self.info = info