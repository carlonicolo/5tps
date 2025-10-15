import re

def checkIsNumber(word: str) -> bool:
    if re.match(r"^-?\d+$", word):
        res = True
    else:
        res = False
    return res
        

def insertDigit() -> int:
    flag = True
    number = input("Inserisci un numero ")
    
    while(flag):
        if re.match(r"^-?\d+$", number):
            number = int(number)
            flag = False
        else:
            print("Numero non corretto rinserisci il numero")
            number = input()
    
    return int(number)
    