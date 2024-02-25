class StatementNode:
    def __init__(self):
        self.codeStrings = []

    def add_node(self, node):
        self.codeStrings.append(node)
        