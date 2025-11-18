class Tree Node:
    def __init__(self, value):
        self.value = value
        self.kid = []

    def add_kid(self, kid_node):
        self.kid.append(kid_node)

    def __str__(self, level=0):
        ret = " " * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
