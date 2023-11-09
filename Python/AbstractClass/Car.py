from Vehicle import Vehicle # fondamentale importare la classe abstract in questo modo

class Car(Vehicle):
    def __init__(self, name, model):
        self.__name = name
        self.__model = model
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value
    
    def start_engine(self):
        print("Starting car engine...")
    
    def stop_engine(self):
        print("Stopping car engine...")
    
    def accelerate(self):
        print("Accelerating car...")
    
    def brake(self):
        print("Applying car brakes...")
    
    
        
car = Car("BMW", "Serie 5")

print(type(car))
print(car.name)
print(car.model)