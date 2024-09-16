from Veicolo import *

class Auto(Veicolo):
    
    def __init__(self, numeroMatricola: int, proprietario: str, tipo: str) -> object:
        super().__init__(numeroMatricola, proprietario)
        self.tipo = tipo
    
    def get_tipo(self):
        return self.tipo
    
    # creare il metodo set