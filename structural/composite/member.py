from abc import ABC, abstractmethod

class Member(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass
