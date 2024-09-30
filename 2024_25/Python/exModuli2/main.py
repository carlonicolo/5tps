import operazioni as op
import re
import utilities as util


BMW_PER_DAY = 50
AUDI_PER_DAY = 70

def main():
        
    number = op.rentalOptions()
    # print("Numero scelta: ", rental_choice)
    
    isNumber = util.checkIsNumber(number)
    
    while(not isNumber):
        print("Numero non corretto rinserisci il numero")
        number = input()
        isNumber = util.checkIsNumber(number)
    
    number = int(number)
    
    # 1 noleggio
    if (number == 1):
        
        lista_auto = ["AUDI","BMW"]
        print("")
        print("Scegli quale auto noleggiare")
        
        for count, value in enumerate(lista_auto):
            print(count, "-", value)
        scelta_auto = util.insertDigit()
        
        print("\n##############################\n")
        
        if(scelta_auto == 0):
            print("Quanti giorni hai noleggiato l'auto? ")
            days = util.insertDigit()
            res = op.calcoloCostoGiornaliero(AUDI_PER_DAY, days)
            
        if(scelta_auto == 1):
            print("Quanti giorni hai noleggiato l'auto? ")
            days = util.insertDigit()
            res = op.calcoloCostoGiornaliero(BMW_PER_DAY, days)
        
        print("Devi pagare: ", res, "€")


if __name__ == "__main__":
    main()
    

'''
flag = True

while(flag):
    if re.match(r"^-?\d+$", number):
        # print("Here 2")
        number = int(number)
        # print(f"The number you entered is {number}.")
        flag = False
    else:
        print("Numero non corretto rinserisci il numero")
        number = input()
'''