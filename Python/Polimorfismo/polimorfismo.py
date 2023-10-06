class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

try:    
    car1 = Car("Ford", "Mustang","PiPPO") #Create a Car object
    boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
    plane1 = Plane("Boeing", "747") #Create a Plane object
    
    x = 10
    if x < 0:
        raise Exception("Sorry, no numbers below zero")

    for x in (car1, boat1, plane1):
        print(x.brand)
        print(x.model)
        x.move()
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

