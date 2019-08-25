# Demonstrating polymorphism
#   Method overriding: defining in the child class a method with the same name of a method in the parent class.
#       When you define a method in the object you make the latter able to satisfy that method call, 
#       so the implementations of its ancestors do not come in play.


# Superclass
class A:
    def func_common(self):
        print("in func_common of A")


# Subclass of A
# NOTE: there is same name method in this subclass, so this subclass' method is used
class B(A):
    def func_common(self):
        print("in func_common of B")


# Subclass of A
# NOTE: there is no same name method in this subclass, so superclass' method is used
class C(A):
    pass


# Creating objects
b1 = B()
c1 = C()


# Calling objects' functions
b1.func_common()
c1.func_common()