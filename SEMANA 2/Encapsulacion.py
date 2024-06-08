class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser positiva.")

    def get_edad(self):
        return self.__edad

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)
print(persona.get_nombre())
persona.set_edad(35)
print(persona.get_edad())

