from Veicolo import *

class Camion(Veicolo):
    
    def __init__(self, numeroMatricola: int, proprietario: str, numAssi: int) -> object:
        super().__init__(numeroMatricola, proprietario)
        self.numAssi = numAssi 
    
    def get_numAssi(self):
        return self.numAssi
    
    # Creare il metodo set