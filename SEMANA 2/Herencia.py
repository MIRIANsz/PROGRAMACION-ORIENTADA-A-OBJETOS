class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Gua Gua"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau Miau"

# Crear instancias de las clases Perro y Gato
mi_perro = Perro("Blu")
mi_gato = Gato("Botas")

print(f"{mi_perro.nombre} dice: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hacer_sonido()}")
