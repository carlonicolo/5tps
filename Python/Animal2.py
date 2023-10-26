class Animal:
  def __init__(self, tipo, age):
    self.tipo = tipo
    self.age = age

  def __str__(self):
    return f"{self.tipo}({self.age})"
    
animal1 = Animal("Lepre", 7)

print(animal1)