import re

# Funzioni

def rentalOptions() -> str:
    print("Benvenuto in Predazzo Rental Auto")
    print("Scegli tra le opzioni disponibili")
    print("1 - Noleggio auto")
    print("2 - Consegna auto")
    choice = input()
    return choice


def calcoloCostoGiornaliero(costo_giornaliero: int, giorni_noleggio: int) -> int:
    return costo_giornaliero * giorni_noleggio



def checkChilometraggio(chilometri_percorsi: int) -> bool:
    pass


def checkIsDigit(number: str):
    flag = True

    while(flag):
        if re.match(r"^-?\d+$", number):
            print("Here 2")
            number = int(number)
            print(f"The number you entered is {number}.")
            flag = False
        else:
            print("Numero non corretto rinserisci il numero")
            number = input()
    
    return number