#03-Generador_de_contrasenas
import random
import string

class Opciones:

    def minuscula(password):
        letra = random.choice(string.ascii_lowercase)
        password.append(letra)
    
    def mayusculas(password):
        letra = random.choice(string.ascii_uppercase)
        password.append(letra)

    def numeros(password):
        numero = random.choice(string.digits)
        numero = str(numero)
        password.append(numero)

    def digitos(password):
        digito = random.choice(string.punctuation)
        password.append(digito)

OP = Opciones
contra = ''
password = []
opciones = ['minusculas']

while True:
    size = input("Introduce la cantidad de caracteres(8-16): ")
    size = int(size)
    if size >= 8 and size <= 16:
        break  

mayusculas = input("incluir mayusculas: (y/n) ")
if mayusculas == 'y':
    opciones.append("mayusculas")
    
numeros = input("Incluir numeros: (y/n) ")
if numeros == 'y':
    opciones.append("numeros")
    
simbolos = input("Incluir Simbolos: (y/n) ")
if simbolos == 'y':
    opciones.append("simbolos")

# Random selections
while size:
	opcion = random.choice(opciones)
	if opcion == "mayusculas":
		OP.mayusculas(password)

	elif opcion == "numeros":
		OP.numeros(password)

	elif opcion == "simbolos":
		OP.digitos(password)
	else:
		OP.minuscula(password)

	size -= 1
	
# Password making
for x in password:
	contra += x

print(contra)
exit = input("Presiona cualquier tecla para salir.")