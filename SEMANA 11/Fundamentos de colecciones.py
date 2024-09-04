import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def cargar_inventario(self, archivo='inventario.json'):
        try:
            with open(archivo, 'r') as f:
                productos_dict = json.load(f)
                for id_producto, info in productos_dict.items():
                    producto = Producto(id_producto, info['nombre'], info['cantidad'], info['precio'])
                    self.productos[id_producto] = producto
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            self.productos = {}
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Asegúrese de que el formato sea correcto.")
            self.productos = {}

    def guardar_inventario(self, archivo='inventario.json'):
        try:
            with open(archivo, 'w') as f:
                productos_dict = {id_producto: vars(producto) for id_producto, producto in self.productos.items()}
                json.dump(productos_dict, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto {producto.nombre} agregado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

def menu():
    inventario = Inventario()
    inventario.cargar_inventario()

    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Mostrar Inventario\n5. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            inventario.guardar_inventario()
        elif opcion == '2':
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            inventario.guardar_inventario()
        elif opcion == '3':
            id_producto = input("ID del Producto a actualizar: ")
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
            inventario.guardar_inventario()
        elif opcion == '4':
            inventario.mostrar_inventario()
        elif opcion == '5':
            inventario.guardar_inventario()
            print("Inventario guardado. Saliendo...")
            break

if __name__ == "__main__":
    menu()
