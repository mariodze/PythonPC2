'''
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).

'''

numeros_encontrados = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
print("Números divisibles por 7 y múltiplos de 5:", numeros_encontrados)