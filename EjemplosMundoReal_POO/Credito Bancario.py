# Clase CreditoBancario
class CreditoBancario:
    def __init__(self, cliente, monto, tasa_interes, plazo):
        self.cliente = cliente
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.plazo = plazo

    def calcular_interes(self):
        return self.monto * self.tasa_interes * self.plazo

    def __str__(self):
        return f'Cliente: {self.cliente}, Monto: ${self.monto}, Tasa de Interés: {self.tasa_interes}%, Plazo: {self.plazo} meses'

# Ejemplo de uso
cliente1 = 'Mirian Sarango'
cliente2 = 'Ana Gomez'

credito1 = CreditoBancario(cliente1, 10000, 0.05, 12)
credito2 = CreditoBancario(cliente2, 5000, 0.06, 24)

# Mostrar información del crédito
print(credito1)
print(f'Interés a pagar: ${credito1.calcular_interes()}')

print(credito2)
print(f'Interés a pagar: ${credito2.calcular_interes()}')
