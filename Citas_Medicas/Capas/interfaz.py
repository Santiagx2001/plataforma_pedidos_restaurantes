from services import *
from db import conexion

class Interfaz:
    def __init__(self):
        pass

    def mostrarMenu():
        print("=== Menú de Opciones ===")
        print("1. Ingresar datos del cliente")
        print("2. Crear lista de productos estandar")
        print("3. Crear nuevo producto")
        print("4. Mostrar productos")
        print("5. Actualizar producto")
        print("6. Eliminar producto")
        print("7. Crear nuevo pedido")
        print("8. Mostrar pedidos")
        print("9. Salir")
        print("=======================")


    def ejecutarOpcion(opcion):
        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            cedula = int(input("Ingrese el número de cédula: "))
            telefono = input("Ingrese el teléfono del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            ingresarDatosCliente(cedula, nombre, telefono, correo)
            print("Datos del cliente ingresados correctamente.")
        elif opcion == '2':
            productos = Productos()
            productos.ingresarListaProductos()
            print("Lista de productos ingresada correctamente.")
        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            disponible = input("¿El producto está disponible? (s/n): ").lower() == 's'
            Productos.crearProducto(nombre, precio, disponible)
            print("Producto creado correctamente.")
        elif opcion == '4':
            print("=== Menu ===")
            Productos.mostrarProductos()
        elif opcion == '5':
            id = int(input("Ingrese el ID del producto a actualizar: "))
            nombre = input("Ingrese el nuevo nombre del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            disponible = input("¿El producto está disponible? (s/n): ").lower() == 's'
            Productos.actualizarProducto(id, nombre, precio, disponible)
            print("Producto actualizado correctamente.")
        elif opcion == '6':
            id = int(input("Ingrese el ID del producto a eliminar: "))
            Productos.eliminarProducto(id)
            print("Producto eliminado correctamente.")
        elif opcion == '7':
            #pedido_id = Pedidos.crearPedido(cliente_id)
            cedula_cliente = int(input("Ingrese la cédula del cliente que realiza el pedido: "))
            pedido_id = Pedidos.crearPedido(cedula_cliente)
            while True:
                Productos.mostrarProductos()
                producto_id = int(input("Ingrese la opción del producto a agregar al pedido (0 para finalizar): "))
                if producto_id == 0:
                    break
                else:
                    producto = Productos.traerProducto(producto_id)
                    cantidad = int(input(f"Cuant@s {producto[0]} desea pedir: "))
                    subtotal = producto[1] * cantidad
                    #print(subtotal)
                    Pedidos.agregarDetallePedido(pedido_id, producto_id, cantidad, subtotal)

            Pedidos.actualizarTotalPedido(pedido_id)
            print("Pedido creado correctamente.")        
            Pedidos.mostrarPedidos()
        elif opcion == '8':
            Pedidos.mostrarPedidos()
            
        


