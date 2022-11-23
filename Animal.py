class Animal:
    _specie = None
    __age = None

    def __init__(self, specie, age):
        self._specie = specie
        self.__age = age

    # properties
    def get_age(self):   # getter method
        return self.__age

    def set_age(self, age):  # setter method
        self.__age = age

    def display(self):
        print(f"This is a {self._specie} and is {self.__age} years old")
        return self