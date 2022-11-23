from Animal import Animal


class Dog(Animal):

    _specie = "Dog"
    move = None

    def __init__(self,age,move):
        super().__init__(self._specie,age)
        self.move = move

    def display(self):
        print(f"This is a {self._specie} and is, {self.get_age()} years old and also can {self.move}")
        return self
