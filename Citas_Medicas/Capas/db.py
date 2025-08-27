# sistema de citas medicas en elq ue pueda incluir el nombre del paciente, nombre del medico fecha de la cita (dia mes y año), y que me muestre las citas registradas en el registro

import sqlite3

# Conectar (crea el archivo si no existe)
conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    cedula INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cedula INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    motivo TEXT,
    FOREIGN KEY (cedula) REFERENCES usuarios(cedula)
)
""")

