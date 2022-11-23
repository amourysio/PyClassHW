from Cat import Cat
from Dog import Dog


class Predator(Cat, Dog):

    predator = None

    def __init__(self, predator):
        self.predator = predator

    def display(self):
        self.predator.display()
        return self.predator
