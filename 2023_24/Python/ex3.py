# 26/09/2023
# Costrutto WHILE

magic_numer: int = 5

try_number = 4
counter_try = 1

while counter_try < try_number:
    guess_number = int(input("Indovina il numero magico -> "))
    if guess_number == magic_numer:
        print("Hai vinto !!!")
        print("Game over")
    if counter_try == 2:
        print("Ultimo tentativo")
        # print(counter_try)
    if counter_try == 3:
        print("Mi dispace hai terminato le vite a disposizione")
        print("Game over")
    counter_try +=1





