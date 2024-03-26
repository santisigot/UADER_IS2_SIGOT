import sys

def factorial(num): 
    if num < 0: 
        print("El factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def calcular_factoriales(rango):
    if '-' in rango:
        inicio, fin = map(int, rango.split('-'))
    else:
        inicio = 1
        fin = int(rango)

    if inicio < 1:
        inicio = 1
    if fin > 60:
        fin = 60

    for num in range(inicio, fin + 1):
        print("El factorial de", num, "! es", factorial(num))

if len(sys.argv) < 2:
    rango = input("Por favor, ingresa un rango en el formato 'desde-hasta' o '-hasta' o 'desde-' para calcular los factoriales: ")
else:
    rango = sys.argv[1]

calcular_factoriales(rango)

#comentario prueba factorial

