# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Cliente: {self.nombre}'

# Clase Habitación
class Habitacion:
    def __init__(self, numero):
        self.numero = numero
        self.reservada = False

    def reservar(self):
        self.reservada = True

    def __str__(self):
        estado = "Reservada" if self.reservada else "Disponible"
        return f'Habitación {self.numero} - Estado: {estado}'

# Clase Reserva
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion
        self.habitacion.reservar()

    def __str__(self):
        return f'Reserva: {self.cliente}, {self.habitacion}'

# Ejemplo de uso
cliente = Cliente('Mirian Sarango')
habitacion = Habitacion(101)
reserva = Reserva(cliente, habitacion)

# Mostrar el estado de la reserva
print(reserva)
