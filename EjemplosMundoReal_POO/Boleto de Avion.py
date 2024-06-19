# Clase BoletoAvion
class BoletoAvion:
    def __init__(self, origen, destino, fecha, precio):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

    def __str__(self):
        return f'Origen: {self.origen}, Destino: {self.destino}, Fecha: {self.fecha}, Precio: ${self.precio}'

# Ejemplo de uso
boleto1 = BoletoAvion('COCA', 'QUITO', '2024-08-15', 45)
boleto2 = BoletoAvion('QUITO-ECUADOR', 'ARGENTINA-BUENOS AIRES', '2024-09-20', 500)

# Mostrar información del boleto
print(boleto1)
print(boleto2)
