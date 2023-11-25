'''

Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
……
“Desea ingresar un número?”: NO
Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
Cantidad de números pares: 5
Cantidad de números impares: 4
Nota:
- Quizás a manera de ayuda el uso de una lista le sea de utilidad.
- El empleo de break sobre condiciones while también le serán de utilidad.



'''



numeros_ingresados = []
while input("¿Desea ingresar un número? (SI/NO): ").upper() == 'SI':
    numero = int(input("Ingrese el número: "))
    numeros_ingresados.append(numero)

numeros_pares = sum(1 for num in numeros_ingresados if num % 2 == 0)
numeros_impares = sum(1 for num in numeros_ingresados if num % 2 != 0)

print("Números ingresados:", numeros_ingresados)
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)




  

