from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def __init__(self, name, model):
        self.__name = name
        self.__model = model
    
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass
    
    @property
    @abstractmethod
    def model(self):
        pass

    @model.setter
    @abstractmethod
    def model(self, value):
        pass
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass