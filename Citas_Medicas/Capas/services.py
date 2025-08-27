from db import cursor, conexion

# Insertar datos
def ingresarDatos (cedula, nombre, edad):
    cursor.execute("INSERT INTO usuarios (cedula, nombre, edad) VALUES (?, ?, ?)", (cedula, nombre, edad))
    conexion.commit()

# Insertar Cita
def ingresarDatosCita (cedula, fecha, motivo):
    cursor.execute("INSERT INTO citas (cedula, fecha, motivo) VALUES (?, ?, ?)", (cedula, fecha, motivo))
    conexion.commit()

# Consultar
def traerCitas(cedula):
    cursor.execute("SELECT * FROM citas WHERE cedula = ?", (cedula,))
    resultados = cursor.fetchall()
    print(resultados)