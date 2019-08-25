# Demonstrating polymorphism
#   Operator overloading: giving extended meaning beyond their predefined operational meaning.
#   Ex: add two integers as well as join two strings and merge two lists

# This example takes two separate objects' passed in numbers 1, 5 and uses
# operator overloading of the __add__ method so the class can use the '+' symbol.
class Plus:
    def __init__(self, a):
        self.a = a
    
    # Operator overloading so that the class can use the '+' symbol
    def __add__(self, second):
        return self.a + second.a


s1 = Plus(1)
s2 = Plus(5)

s3 = s1 + s2
print(s3)