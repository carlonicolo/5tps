class Animal:
  def __init__(self, tipo, age):
    self.tipo = tipo
    self.age = age

  def myfunc(self):
    print("Ciao sono " + self.tipo)

  def __str__(self):
    return f"{self.tipo}({self.age})"
    
a1 = Animal("Gatto", 10)
print(a1)
a1.age = 12

print(a1.age)

f"myfunc -> {a1.myfunc()}"
    
