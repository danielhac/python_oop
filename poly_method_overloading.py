# Demonstrating polymorphism
#   Method overloading: ability to pass in and handle 0 or more args to a method


class Calculate:
    def area(self, a=None, b=None):
        if a != None and b != None:
            print( a * b )
        elif a != None:
            print(a * a)
        else:
            print(0)

# Object creation
c1 = Calculate()
c2 = Calculate()
c3 = Calculate()


# Object calling method with various number of args
c1.area()
c2.area(5)
c3.area(4, 8)
