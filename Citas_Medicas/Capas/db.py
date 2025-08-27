# sistema de citas medicas en elq ue pueda incluir el nombre del paciente, nombre del medico fecha de la cita (dia mes y año), y que me muestre las citas registradas en el registro

import sqlite3

# Conectar (crea el archivo si no existe)
conexion = sqlite3.connect("Restaurante.db")
cursor = conexion.cursor()

# Crear tablas
    # Tabla de productos (menú)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        disponible INTEGER DEFAULT 1
    )
    """)

    # Tabla de clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT,
        correo TEXT
    )
    """)

    # Tabla de pedidos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total REAL DEFAULT 0,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    """)

    # Detalle del pedido (productos en cada pedido)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_pedido (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pedido_id INTEGER,
        producto_id INTEGER,
        cantidad INTEGER NOT NULL,
        subtotal REAL NOT NULL,
        FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    """)

