'''
Creare un programma che utilizza almeno:
- una funzione di tipo void
- una funzione di tipo int
- una funzione di tipo str
- una funzione che restituisce due valore

Le funzioni possono avere zero, uno o più parametri
'''
import utilities as u


def main():
    res_somma, res_diff = u.computeAddSub(10,5)
    print("Somma: ", res_somma)
    print("Differenza: ", res_diff)


if __name__ == "__main__":
    main()