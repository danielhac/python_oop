# Demonstrating encapsulation: 
#   Used to hide data members and members function but
#   private variables in python are not actually hidden fields like in other object oriented languages.
#   Usage of double underscore before the attrib name seems like it works by not being able to access it directly.
#   In order to access a double underscore attrib name, getters and setters methods must be made.


class Person:
    def __init__(self, email):
        self.__email = email
    
    
    def get_email(self):
        return self.__email
    

    def set_email(self, change_email):
        self.__email = change_email


# Creating object
p1 = Person("dan@gmail.com")


# DIRECTLY calling/setting object's attribtues
# print(p1.__email)                 # cannot access directly (throws error)
p1.__email = "test@gmail.com"       # cannot set directly (no error thrown)

# INDIRECTLY calling/setting object's attribtues
print(p1.get_email())

p1.set_email("new@gamil.com")
print(p1.get_email())