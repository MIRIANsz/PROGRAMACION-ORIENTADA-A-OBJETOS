class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, dia, temperatura):
        """
        Método para ingresar la temperatura de un día específico.
        """
        if len(self.temperaturas) < 7:
            self.temperaturas.append((dia, temperatura))
        else:
            print("Ya se han ingresado las temperaturas de todos los días de la semana.")

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal de las temperaturas.
        """
        if len(self.temperaturas) == 0:
            return 0
        total = sum(temp for dia, temp in self.temperaturas)
        return total / len(self.temperaturas)

    def mostrar_temperaturas(self):
        """
        Método para mostrar las temperaturas ingresadas.
        """
        for dia, temp in self.temperaturas:
            print(f"Día {dia}: {temp}°C")


def main():
    """
    Función principal que organiza la entrada de datos y el cálculo del promedio utilizando la clase ClimaSemanal.
    """
    print("Bienvenido al programa de cálculo de promedio de temperaturas semanales.")
    clima = ClimaSemanal()

    for i in range(7):
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                clima.ingresar_temperatura(i + 1, temperatura)
                break
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")

    print("\nLas temperaturas ingresadas son:")
    clima.mostrar_temperaturas()

    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()
