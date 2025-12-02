# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 21:48:57 2025

@author: Karlitos
"""

# Define the Person class
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, Email: {self.email})"
    

# Example usage
if __name__ == "__main__":
    
    lstPerson = []

    person = Person("Daniel",35,"daniel@salvador.com")
    lstPerson.append(person)
    
    person = Person("Pippo",45,"pippo@salvador.com")
    lstPerson.append(person)
    
    person = Person("Ziggo",25,"ziggo@salvador.com")
    lstPerson.append(person)
    
    # Print the Person object
    print(person)
    print("")
    

    # Print each Person object
    for person in lstPerson:
        print(person)
        
    
    lstNumbers = []
    a = 5
    lstNumbers.append(a)
    
    a = 7
    lstNumbers.append(a)
    
    a = 9
    lstNumbers.append(a)

    