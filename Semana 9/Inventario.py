class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto
    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Representación del objeto como cadena
    def __str__(self):
        return f'{self.id_producto},{self.nombre},{self.cantidad},{self.precio:.2f}'

    @classmethod
    def from_string(cls, producto_str):
        id_producto, nombre, cantidad, precio = producto_str.strip().split(',')
        return cls(id_producto, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo_inventario='inventario.txt'):
        self.archivo_inventario = archivo_inventario
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        productos = []
        try:
            with open(self.archivo_inventario, 'r') as archivo:
                for linea in archivo:
                    producto = Producto.from_string(linea)
                    productos.append(producto)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo_inventario} no encontrado. Se creará uno nuevo.")
        except PermissionError:
            print(f"No se tiene permiso para leer el archivo {self.archivo_inventario}.")
        return productos

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                for producto in self.productos:
                    archivo.write(str(producto) + '\n')
            print(f"Inventario guardado exitosamente en {self.archivo_inventario}.")
        except PermissionError:
            print(f"No se tiene permiso para escribir en el archivo {self.archivo_inventario}.")

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(f"Error: El ID {producto.get_id()} ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print(f"Producto {producto.get_nombre()} añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        self.guardar_inventario()
        print(f"Producto con ID {id_producto} eliminado exitosamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print(f"Producto con ID {id_producto} actualizado exitosamente.")
                return
        print(f"Error: No se encontró el producto con ID {id_producto}.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (dejar en blanco si no desea cambiar): ")
            precio = input("Ingrese nuevo precio (dejar en blanco si no desea cambiar): ")
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None, precio=float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()


