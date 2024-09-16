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
    
    def prelievoInterattivo(self):
        pass
    
    def prelievo(self, importo_da_prelevare):
        try:
            if(importo_da_prelevare < self.__saldo ):
                print("Saldo corrente: ", str(self.__saldo))
                print("Puoi effettuare il prelievo")
                self.__saldo = self.__saldo - importo_da_prelevare
                print("Il tuo nuovo saldo è: ", str(self.__saldo))
            else:
                print("Mi dispiace l'importo da prelevare eccede il tuo credito")
        except Exception as e:
            print("Errore: ", e)
            