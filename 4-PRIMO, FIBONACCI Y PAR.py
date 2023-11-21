import math

number = 3

def fibonacci(number):
    print("1")
    old = 1 #a
    current = 1 # b
    next_number = 0 #c
    current_number = 0

    print(old)
    while current_number <= number:
        next_number = old + current
        current_number = next_number
        if current_number >= number:
            break
        else:
            print(current_number)
        old = current + next_number
        current_number = old
        if current_number >= number:
            break
        else:
            print(current_number)
        current = old + next_number
        current_number = current
        if current_number >= number:
            break
        else:
            print(current_number)

def check_facts(number):

    message = ""
    
    #primo
    if number > 1:
        for index in range(2, number):
            if number % index == 0:
                message += "Es Primo, "
        else:
            message += "No es primo, "
    else:
        print("No es Primo, ")

    #Fibonacci
    fibonacci(number)

    #par
    message += "y es par." if number % 2 == 0 else "y es impar."

    return print(message)

check_facts(number)