class Veicolo():
    
    def __init__(self, numeroMatricola: int, proprietario: str) -> object:
        self.numeroMatricola = numeroMatricola
        self.proprietario = proprietario
    
    def get_NumeroMatricola(self):
        return self.numeroMatricola
    
    def get_proprietario(self):
        return self.proprietario
    
    def set_numeroMatricola(self, numMatr):
        self.numeroMatricola = numMatr
        
    def set_proprietario(self, newProprietario):
        self.proprietario = newProprietario
        
    def __str__(self):
        return f"\nNumero matricola:{self.numeroMatricola} \nProprietario:{self.proprietario}"
    
    