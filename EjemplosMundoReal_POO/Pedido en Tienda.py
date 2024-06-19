# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'{self.nombre} - ${self.precio}'

# Clase Pedido
class Pedido:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total_pedido(self):
        return sum(producto.precio for producto in self.productos)

    def __str__(self):
        productos_str = '\n'.join(str(producto) for producto in self.productos)
        return f'Productos en el pedido:\n{productos_str}\nTotal: ${self.total_pedido()}'

# Ejemplo de uso
producto1 = Producto('Laptop', 1000)
producto2 = Producto('Ratón', 50)

pedido = Pedido()
pedido.agregar_producto(producto1)
pedido.agregar_producto(producto2)

# Mostrar información del pedido
print(pedido)
