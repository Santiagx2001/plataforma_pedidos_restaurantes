from interfaz import *

while True:
    Interfaz.mostrarMenu()
    opcion = input("Escoja una opcion: ")
    if opcion == '9':
        break
    else:
        Interfaz.ejecutarOpcion(opcion)
        