'''

Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
Nota:
El uso de listas con diccionarios le será de utilidad.


'''





alumnos = []
while True:
    nombre_alumno = input("Ingrese el nombre del alumno (o escriba 'fin' para salir): ")
    if nombre_alumno.lower() == 'fin':
        break
    calificaciones = [int(input(f"Ingrese la calificación {i + 1} del alumno {nombre_alumno}: ")) for i in range(3)]
    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}
    alumnos.append(alumno)


print("Listado completo de alumnos:")
for alumno in alumnos:
    print(alumno)
