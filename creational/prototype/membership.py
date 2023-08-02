import copy

class Member:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def clone(self):
        return copy.deepcopy(self)
