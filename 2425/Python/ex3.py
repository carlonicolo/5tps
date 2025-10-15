''' 
Programma calcolatrice
Visualizza un menu di scelta operazioni (funzioni):
- somma
- prodotto
- differenza
- rapporto
- quadrato
- check se è pari o dispari
'''
import math

# Funzioni

# Calcolatrice
def somma(lista_valori):
    ris=0
    for i in range(len(lista_valori)):
        ris = ris+lista_valori[i]    
    return ris


# Prodotto
def prodotto(lista_valori):
    ris=1
    for i in range(len(lista_valori)):
        ris = ris*lista_valori[i] 
        i+=1
    return ris


# Sottrazione
def sottrazione(lista_valori):
    ris=0
    primo_numero = lista_valori.pop(0)
    ris = primo_numero-somma(lista_valori)
    return ris


# Divisione
def frazione(lista_valori):
    res = lista_valori.pop(0)
    for i in range(len(lista_valori)):
        res = res/lista_valori[i]
    return res


# end funzioni

try:
    
    print("\n########## CALCOLATRICE ##########")
    lista_valori = []

    #operazioni disponibili
    indice = 0
    lista_operazioni = ["somma","prodotto","sottrazione","frazione","pari o dispari"]

    for count, value in enumerate(lista_operazioni):
        print(count, "-", value)


    # for i in range(len(lista_operazioni)):
    #     print(indice," - ",lista_operazioni[i])
    #     i=+1
    #     indice+=1

    print("##############################\n")

    #Scelta delle operazioni
    operazione = int(input("Scegli l'operazione:   "))
    print("\n##############################\n")



    if(operazione >= 0 and operazione <= 4):
        qta_valori = int(input("quanti valori vuoi inserire:    "))
        n=0
        for i in range(qta_valori):
            print("insersci il",i ," numero:")
            if(operazione == 3):
                num = int(input(""))
                if(num == 0):
                    while(num == 0):
                        num = int(input("Non puoi dividere per 0, riprova:  "))
                if(num != 0):
                    lista_valori.append(num)
                    n+=1
            if(operazione !=3):
                num = int(input(""))
                lista_valori.append(num)
                n+=1
    else:
        print("Mi dispice il codice operazione inserito non esiste.")

    if(operazione == 0):
        print("la somma è -> ",somma(lista_valori))
        
    if(operazione == 1):
        print("il prodotto è -> ",prodotto(lista_valori))
        
    if(operazione == 2):
        print("la differenza è -> ",sottrazione(lista_valori))
        
    if(operazione == 3):
        print("la frazione è -> ",frazione(lista_valori))
        
    if(operazione == 4):
        num = int(input("inserisci il numero:   "))
        ris = math.sqrt(num)
        print("la radice quadrata è -> ",ris) 
        
    if(operazione == 5):
        for i in range(len(lista_valori)):
            res = lista_valori[i]
            if (res%2==0):
                print(res,"-> è pari")
            else:
                print(res,"-> è dispari")

except Exception as e:
  print("Exception -> ", e)