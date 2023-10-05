class Person:
  def __init__(self, fname: str, lname: str):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname: str, lname: str):
    super().__init__(fname, lname)

studente = Student("Mike", "Olsen")
studente.printname()
