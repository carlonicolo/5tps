import operazioni as op

BMW_PER_DAY = 50
AUDI_PER_DAY = 70

def main():
    
    lista_auto = ["AUDI","BMW"]

    for count, value in enumerate(lista_auto):
        print(count, "-", value)
        
    #Scelta delle operazioni
    scelta_auto = int(input("Scegli quale auto noleggiare:   "))
    print("\n##############################\n")
    
    if(scelta_auto == 0):
        days = int(input("Quanti giorni hai noleggiato l'auto? "))
        res = op.calcoloCostoGiornaliero(AUDI_PER_DAY, days)
        
    
    # Check se ha percorso più di 1000 km
    # isMore = op.checkChilometraggio(kmpercorsi)
    # if(isMore > 1000):..... else:....
    






if __name__ == "__main__":
    main()