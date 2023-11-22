
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
                mensaje = f"{numero} No es primo"
                break
            else:
                mensaje = f"{numero} es primo"
    else:
        mensaje = f"{numero} No es primo"

    return mensaje

message = primos(11)

print(message)