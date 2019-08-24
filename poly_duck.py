# Demonstrating polymorphism
#   Duck typing:    way of programming in which an object passed into a function or method supports all 
#                   method signatures and attributes expected of that object at run time


# Duck typing demonstration
class Duck:
    def fly(self):
        print("duck is flying")


class Bird:
    def fly(self):
        print ("bird is flying")


class Airplane:
    def fly(self):
        print("plane is flying")


# NOTE: this is where it will not work due to not having the same method signature
class Shark:
    def swim(self):
        print("shark is swimming")


def execute(flying_obj):
    flying_obj.fly()


# Creating objects
duck = Duck()
bird = Bird()
airplane = Airplane()
shark = Shark()


# Executing the method by calling each object
execute(duck)
execute(bird)
execute(airplane)
execute(shark)