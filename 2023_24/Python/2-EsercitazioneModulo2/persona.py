class Persona():
    '''
    '''
    def __init__(self, name, cognome, age, codiceFiscale):
        ## private varibale or property in Python
        self.__name = name
        self.__cognome = cognome
        self.__age = age
        self.__codiceFiscale = codiceFiscale
        self.__lst_conti = []
    
    
    ## getter method to get the properties using an object
    def get_name(self):
        return self.__name
    
    ## getter method to get the properties using an object
    def get_cognome(self):
        return self.__cognome
    
    ## getter method to get the properties using an object
    def get_age(self):
        return self.__age
    
    ## getter method to get the properties using an object
    def get_codiceFiscale(self):
        return self.__codiceFiscale

    ## setter method to change the value 'name' using an object
    def set_name(self, name):
        self.__name = name

    ## setter method to change the value 'name' using an object
    def set_cognome(self, cognome):
        self.__cognome = cognome

    ## setter method to change the value 'age' using an object
    def set_age(self, age):
        self.__age = age
    
    ## setter method to change the value 'age' using an object
    def set_codiceFiscale(self, codiceFiscale):
        self.__codiceFiscale = codiceFiscale
    
    def get_conto(self):
        '''
        Ritorna il primo conto nella lista dei conti
        associati alla persona
        '''
        return self.__conto[0]
    
    def set_lst_conti(self, conto):
        self.__lst_conti.append(conto)