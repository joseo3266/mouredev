import math

number = 13

def primos(numero):
    # Comprobamos si es un numero primo.
    if numero > 1:

        #Al ser mayor que 1, puede ser primo
        for number in range(2,numero): 
            """ Creamos un ciclo para comprobar
                si el residuo de los numeros anteriores queda limpio"""
            result = numero % number
            if result == 0:
                # esto nos indica que puede ser producto de los anteriores
                mensaje = f"{numero} No es primo, "
                break
            else:
                mensaje = f"{numero} es primo, "
    else:
        mensaje = f"{numero} No es primo, "
 
    return mensaje

def fibonacci(number):
    secuencia = []
    old = 1 #a
    current = 1 # b
    next_number = 0 #c
    current_number = 0 #5

    secuencia.append(old)
    while current_number <= number:
        next_number = old + current #8
        current_number = next_number #8
        secuencia.append(current_number)
        if current_number >= number:
            break
        
        old = current + next_number #3
        current_number = old #3
        secuencia.append(current_number)
        if current_number >= number:
            break
        
        current = old + next_number #5
        current_number = current #5
        secuencia.append(current_number)
        if current_number >= number:
            break
           
        #hacer una lista para almacenar los numeros de la sucecion y 
        # comparar si es o no fibonacci.
    if number in secuencia:
        message = ("Es fibonacci, ")
    else:
        message = ("No es fibonacci, ")
    
    return message

def check_facts(number):

    message = ""
    
    #primo
    message += primos(number)

    #Fibonacci
    message += fibonacci(number)

    #par
    message += "y es par." if number % 2 == 0 else "y es impar."

    return print(message)

check_facts(number)