# Seconda esercitazione di ripasso: struttura dati list e funzioni

'''
Creare una lista contenente i numeri da 1 a 10
definire 4 funzioni per effettuare le quattro operazioni aritimetiche fondamentali
'''

# list con 6 valori da 1 a 6
# a = [1,2,3,4,5,6]
# print("Before ->", a)
# a.append(5)
# print("After ->", a)

# TASK 0
# Creazione lista usando un ciclo
lista=[]
for i in range(0,11,1):
  lista.append(i)

#print(lista)  
#print("")

# TASK 1
# Funzione somma con due parametri interi
def somma(a,b):
  sum = a + b
  return sum


# TASK 2
# Funzione differenza (sottrazione) con due parametri interi
def differenza(a,b):
  diff = a - b
  return diff


# TASK 3
# Funzione prodotto (moltiplicazione) con due parametri interi
def moltiplicazione(a,b):
  mult = a * b
  return mult


# TASK 4
# Funzione rapporto (divisione) con due parametri interi di cui 
# il denomitaore necessariamente diverso e maggiore di 0
#a=8
#b=3
def divisione(a,b):
  div = a / b
  return div


# TASK 5
# Creazione una funziona che ritorna una lista di n numeri positivi
'''
def createList(numero_elementi_lista):
  lst=[3,4,5,6,7,8]
#for i in range(len(lst)):
    #print(i,end=' ')
  return list
for i in range(createList):
  
print("\nla lista è:  ",createList)
'''

#### Funcion call ####

# Funzione somma
print(" ### Funzione somma ###")
val1 = int(input("Inserisci primo numero: "))
val2 = int(input("Inserisci secondo numero: "))
print("la somma è:  ", somma(val1, val2))
print(" ")

# Funzione differenza
print(" ### Funzione differenza  ###")
val1 = int(input("Inserisci primo numero: "))
val2 = int(input("Inserisci secondo numero: "))
print("la somma è:  ", differenza(val1, val2))
print(" ")

# Funzione prodotto
print(" ### Funzione prodotto  ###")
val1 = int(input("Inserisci primo numero: "))
val2 = int(input("Inserisci secondo numero: "))
print("la somma è:  ", moltiplicazione(val1, val2))
print(" ")

# Funzione rapporto
print(" ### Funzione divisione ###")
print(" *** Ricorda che il denominatore DEVE essere diverso da 0 *** ")
val1 = int(input("Inserisci primo numero: "))

val2 = int(input("Inserisci secondo numero: ")) 
if (val2 != 0):
  print("il rapporto è:  ", divisione(val1, val2))
else:
  print("Il denominatore non può essere uguale a 0 !!!")
  while(val2 == 0):
    val2 = int(input("Inserisci secondo numero: "))
  print("il rapporto è:  ", divisione(val1, val2))
  
