from db import cursor, conexion

# Insertar datos
def ingresarDatosCliente (cedula, nombre, telefono, correo):
    cursor.execute("INSERT INTO clientes (cedula, nombre, telefono, correo) VALUES (?, ?, ?, ?)", (cedula, nombre, telefono, correo))
    conexion.commit()

class Productos:
    def __init__(self):
        pass

    productos = [
        {"nombre": "Hamburguesa Clásica", "precio": 18000, "disponible": True},
        {"nombre": "Pizza Margarita", "precio": 25000, "disponible": True},
        {"nombre": "Ensalada César", "precio": 15000, "disponible": True},
        {"nombre": "Perro Caliente Especial", "precio": 12000, "disponible": False},
        {"nombre": "Sándwich de Pollo", "precio": 16000, "disponible": True},
        {"nombre": "Sopa del Día", "precio": 10000, "disponible": True},
        {"nombre": "Tacos Mexicanos", "precio": 20000, "disponible": True},
        {"nombre": "Arepa Rellena", "precio": 8000, "disponible": False},
        {"nombre": "Pasta Alfredo", "precio": 22000, "disponible": True},
        {"nombre": "Postre de Chocolate", "precio": 9000, "disponible": True}
    ]

    def ingresarListaProductos (self):
        for producto in self.productos:
            cursor.execute("INSERT INTO productos (nombre, precio, disponible) VALUES (?, ?, ?)", (producto["nombre"], producto["precio"], int(producto["disponible"])))
        conexion.commit()

    def crearProducto (nombre, precio, disponible):
        cursor.execute("INSERT INTO productos (nombre, precio, disponible) VALUES (?, ?, ?)", (nombre, precio, int(disponible)))
        conexion.commit()

    def mostrarProductos ():
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        for producto in resultados:
            print(f"opcion {producto[0]}. {producto[1]}............${producto[2]}")

    def traerProducto(producto_id):
        cursor.execute("SELECT nombre, precio FROM productos WHERE id = ?", (producto_id,))
        respuesta = cursor.fetchone()
        return respuesta
        
    def actualizarProducto (id, nombre, precio, disponible):
        cursor.execute("UPDATE productos SET nombre = ?, precio = ?, disponible = ? WHERE id = ?", (nombre, precio, int(disponible), id))
        conexion.commit()

    def eliminarProducto (id):
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conexion.commit()

class Pedidos:
    def __init__(self):
        pass

    def crearPedido (cedula_cliente):
        cursor.execute("INSERT INTO pedidos (cedula_cliente) VALUES (?)", (cedula_cliente,))
        conexion.commit()
        return cursor.lastrowid  # Retorna el ID del pedido creado

    def agregarDetallePedido (pedido_id, producto_id, cantidad, subtotal):
        cursor.execute("INSERT INTO detalle_pedido (pedido_id, producto_id, cantidad, subtotal) VALUES (?, ?, ?, ?)", (pedido_id, producto_id, cantidad, subtotal))
        conexion.commit()

    def mostrarPedidos ():
        cursor.execute("""
            SELECT p.id, c.nombre, p.fecha, p.total
            FROM pedidos p
            JOIN clientes c ON p.cedula_cliente = c.cedula
        """)
        resultados = cursor.fetchall()
        print(resultados)

    def actualizarTotalPedido (pedido_id):
        cursor.execute("SELECT SUM(subtotal) FROM detalle_pedido WHERE pedido_id = ?", (pedido_id,))
        total = cursor.fetchone()[0] or 0
        cursor.execute("UPDATE pedidos SET total = ? WHERE id = ?", (total, pedido_id))
        conexion.commit()




