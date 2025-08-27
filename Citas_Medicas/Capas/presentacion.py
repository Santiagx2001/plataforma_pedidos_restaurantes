from services import *
from db import conexion

def interfaz ():
    print(">>>Registro de Usuario<<<")
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ingresarDatos(cedula, nombre, edad)

    print(">>>Registro de Cita<<<")
    fecha = input("Fecha: ")
    motivo = input("Motivo: ")
    ingresarDatosCita(cedula, fecha, motivo)
    print(traerCitas(cedula))
    conexion.close()




interfaz()