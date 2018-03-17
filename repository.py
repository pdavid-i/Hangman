class RepositoryException(Exception):
    pass


class Repository:
    def __init__(self):
        self.elems = []

    def add(self, elem):
        if elem in self.elems:
            raise RepositoryException("existing elem!!!")
        self.elems.append(elem)
        return elem

    def __len__(self):
        return len(self.elems)

    def clean(self):
        self.elems = []

    def getAll(self):
        return self.elems[:]
