# 03/10/2023
# Funzioni

def square(num1: int, num2: int) -> int:
    square = num1 * num2
    return square

def greeting(name: str, age: int) -> None:
    if age < 40:
        msg_age = "sei giovane"
        to_greeting = "Ciao " + name + " " + msg_age
        print(to_greeting)
    else:
        msg_age = "il tempo passa..."
        to_greeting = "Ciao " + name + " " + msg_age
        print(to_greeting)
        
def two_square(first_num: int, second_num: int):
    square_first_number = first_num * first_num
    square_second_number = second_num * second_num
    lst_square = [square_first_number, square_second_number]
    return square_first_number, square_second_number, lst_square

def greeting_all(*args) -> None:
    """ Funzione per salutare n persone
        
        @param: *args lista di persone da salutare 
    """    
    print(args)
    for i in args:
        print("Ciao " + i)

        
res_square = square(5,6)

print(res_square)
greeting("Marco",19)

first, second, lst_number = two_square(2,3)
print(first)
print(second)
print(lst_number)

greeting_all("Marco","Carlo","Pippo","Pluto")