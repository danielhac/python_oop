# Demonstrating abstract classes
#   Blueprint for subclasses, by creating a set of methods that must be created within any 
#       subclasses built from the abstract class.
#   Abstract method has declaration but no implementation.
#   Cannot be instantiated and needs subclasses to provide implementations for abstract 
#       methods which are defined in abstract classes.


# ABC works by marking methods of the base class as abstract and then registering concrete 
#   classes as implementations of the abstract base. 
#   @abstractmethod: must use on the abstract method
from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def type(self):
        pass


class Mac(Computer):
    def type(self):
        print("MacOS")


class Windows(Computer):
    def ram(self):
        print("16 GB")


# Create objects and call methods
c1 = Mac()
c1.type()

# c2 = Windows()      # Will fail due to non-existing matching method with abstract method in superclass
