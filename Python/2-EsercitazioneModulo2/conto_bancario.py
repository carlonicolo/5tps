class Persona():
    '''
    '''
    def __init__(self, name, age, conto):
        ## private varibale or property in Python
        self.__name = name
        self.__age = age
        self.__conto = conto
    
    
    ## getter method to get the properties using an object
    def get_name(self):
        return self.__name
    
    ## getter method to get the properties using an object
    def get_age(self):
        return self.__age
    
    def get_conto(self):
        return self.__conto

    ## setter method to change the value 'name' using an object
    def set_name(self, name):
        self.__name = name

    ## setter method to change the value 'age' using an object
    def set_age(self, age):
        self.__age = age
        
    def set_conto(self, conto):
        self.__conto = conto