'''

Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.


'''


def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial(numero - 1)


numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")