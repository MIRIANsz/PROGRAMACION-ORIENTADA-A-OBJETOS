from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Crear instancias de Circulo y Rectangulo
mi_circulo = Circulo(5)
mi_rectangulo = Rectangulo(4, 6)

print(f"Área del círculo: {mi_circulo.area()}")
print(f"Área del rectángulo: {mi_rectangulo.area()}")
