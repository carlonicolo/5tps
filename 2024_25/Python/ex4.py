'''
Programma somma n valori richiesti all'utente
'''

def somma(lst_elements: list) -> int:
    print("Inside function -> ", lst_elements)
    res = 0
    for i in range(len(lst_elements)):
        print(lst[i])
        res = res + lst[i]
    return res
    
    
lst = []
number_of_elements = int(input("Quanti valori vuoi inserire? "))

for i in range(number_of_elements):
    print("Inserisci elemento ", i, "esimo:")
    element = int(input(""))
    lst.append(element)

print("len -> ", len(lst))
print("Valori lst -> ", lst)
print("La somma dei valori nella lista è: ", somma(lst))