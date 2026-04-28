from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("i can walk and run on the ground")
class black_panther(Animal):
    def move(self):
        print("i can sprint in the dark forest")
class tiger(Animal):
    def move(self):
        print("i can creep into my prey in the jungle")
class lion(Animal):
    def move(self):
        print("i roar in the animal kingdom")
class chettah(Animal):
    def move(self):
        print("i can sprint in the shara lands")
class eagle(Animal):
    def move(self):
        print("i can fly up in the sky")

Dp = black_panther()
Dp.move()
h = Human()
h.move()
k = lion()
k.move
ea = eagle()
ea.move()
Ch = chettah()
Ch.move()
Ti = tiger()
Ti.move()