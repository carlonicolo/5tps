# Prima esercitazione di ripasso: if...else, for

'''
Crea un semplice programma che chiede all'utente
di inserire un valore numerico intero > 0
user_number

Se user_number è maggiore di 10 -> stampare il conto alla rovescia dal numero fino allo 0
altrimenti stampare i numeri dal valore fino a 20
'''

# Valore intero positivo > 0 inserito dall'utente

user_number = int(input("inserisci un numero maggiore di 0: "))

# print(type(user_number))

if (user_number > 10):
  for i in range(user_number,-1,-1):
    print(i)

else:
  for i in range(user_number,21,1):
    print(i)
