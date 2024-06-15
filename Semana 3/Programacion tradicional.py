def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias durante una semana.
    """
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio de una lista de temperaturas.
    """
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que organiza la entrada de datos y el cálculo del promedio.
    """
    print("Bienvenido al programa de cálculo de promedio de temperaturas semanales.")

    # Ingresar temperaturas
    temperaturas = ingresar_temperaturas()

    # Calcular promedio semanal
    promedio = calcular_promedio(temperaturas)

    print(f"\nLas temperaturas ingresadas son: {temperaturas}")
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()

