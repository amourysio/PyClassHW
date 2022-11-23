from Dog import Dog
from Cat import Cat
from Predator import Predator

dog = Dog(10,"Running")
cat = Cat(5,"Running")

dog.display()
cat.display()

predator = Predator(dog)

predator.display()
