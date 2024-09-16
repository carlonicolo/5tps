from Veicolo import *

class Moto(Veicolo):
    
    def __init__(self, numeroMatricola: int, proprietario: str, numPosti: int) -> object:
        super().__init__(numeroMatricola, proprietario)
        self.numPosti = numPosti
    
    def get_numPosti(self):
        return self.numPosti
    
    # creare il metodo set