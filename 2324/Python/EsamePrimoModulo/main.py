from Veicolo import *
from Auto import *
from Moto import *
from Camion import *

def main():
    veicolo1 = Veicolo(12345, "Karlitos")
    auto1 = Auto(98765, "Jim", "Spider")
    moto1 = Moto(76354, "Jack", 2)
    camion1 = Camion(102938, "Billy", 1)
    
    print(veicolo1)
    print(veicolo1.__class__.__name__)
    
    print(auto1)
    print(auto1.__class__.__name__)
    
    print(moto1)
    print(moto1.__class__.__name__)
    
    print(camion1)
    print(camion1.__class__.__name__)


if __name__ == "__main__":
    main()