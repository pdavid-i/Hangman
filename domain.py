class Word:
    def __init__(self, word):
        list = []
        for i in range(len(word)):
            list.append(0)
        self.word = word
        self.check = list

    def __eq__(self, other):
        return (self.word == other.word)