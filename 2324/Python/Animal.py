class Animal:
  def __init__(self, tipo, age):
    self.tipo = tipo
    self.age = age

animal1 = Animal("Lepre", 7)

print(type(animal1))
print(animal1.tipo)
print(animal1.age)

animal2 = Animal("Cane", 9)  

print(type(animal2))
print(animal2.tipo)
print(animal2.age)
