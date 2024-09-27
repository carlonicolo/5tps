import operazioni as op
import re


BMW_PER_DAY = 50
AUDI_PER_DAY = 70

def main():
        
    number = op.rentalOptions()
    # print("Numero scelta: ", rental_choice)
    
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
    
    # 1 noleggio
    if (number == 1):
        
        lista_auto = ["AUDI","BMW"]
        print("")
        print("Scegli quale auto noleggiare")
        
        for count, value in enumerate(lista_auto):
            print(count, "-", value)
        scelta_auto = int(input("-> "))
        
        print("\n##############################\n")
        
        if(scelta_auto == 0):
            days = int(input("Quanti giorni hai noleggiato l'auto? "))
            res = op.calcoloCostoGiornaliero(AUDI_PER_DAY, days)
            
        if(scelta_auto == 1):
            days = int(input("Quanti giorni hai noleggiato l'auto? "))
            res = op.calcoloCostoGiornaliero(BMW_PER_DAY, days)
        
        print("Devi pagare: ", res, "€")
    
        # 2 consegna
        
        ask = input("Inserisci intero")
        num = op.checkIsDigit(ask)
        
        print(num)
        
        
        
        # Check se ha percorso più di 1000 km
        # isMore = op.checkChilometraggio(kmpercorsi)
        # if(isMore > 1000):..... else:....


if __name__ == "__main__":
    main()