
from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def valuta_eta(self):
        pass


class Person(User):
    
    def __init__(self, name, age):
        ## private varibale or property in Python
        self.__name = name
        self.__age = age
        

    ## getter method to get the properties using an object
    def get_name(self):
        return self.__name
    
    ## getter method to get the properties using an object
    def get_age(self):
        return self.__age

    ## setter method to change the value 'name' using an object
    def set_name(self, name):
        self.__name = name

    ## setter method to change the value 'age' using an object
    def set_age(self, age):
        self.__age = age
    
    # p is a Person object
    def valuta_eta(self, p):
        age = int(p.get_age())
        if age >= 18:
            print("Sei maggiorenne")
        else:
            print("Sei minorenne")
    
    def __str__(self) -> str:
        return "From str method of Person: name is %s, age is %s" % (self.get_name(), self.get_age()) 

name = str(input("Come ti chiami ? "))
age = str(input("Quanti anni hai? "))

p = Person(name, age)
p.valuta_eta(p)
print(p)