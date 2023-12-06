class Conto():
    
    def __init__(self, persona, codiceIBAN, saldo):
       self.__persona = persona
       self.__codiceIBAN = codiceIBAN
       self.__saldo = saldo
       
    
    def get_codiceIBAN(self):
        return self.__codiceIBAN
    
    def get_saldo(self):
        return self.__saldo
    
    def get_persona(self):
        return self.__persona