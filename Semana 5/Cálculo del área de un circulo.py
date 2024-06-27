# Programa para calcular el área de un círculo y un rectángulo
# Utiliza diferentes tipos de datos (integer, float, string, boolean)
# y sigue la convención snake_case para identificadores

import math


def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    :param radio: Radio del círculo.
    :return: Área del círculo.
    """
    area = math.pi * (radio ** 2)
    return area


def calcular_area_rectangulo(longitud: float, anchura: float) -> float:
    """
    Calcula el área de un rectángulo dada su longitud y anchura.

    :param longitud: Longitud del rectángulo.
    :param anchura: Anchura del rectángulo.
    :return: Área del rectángulo.
    """
    area = longitud * anchura
    return area


def mostrar_informacion():
    """
    Muestra la información de las áreas calculadas.
    """
    # Datos de entrada
    radio_circulo = 5.0
    longitud_rectangulo = 10
    anchura_rectangulo = 4.5

    # Cálculo de áreas
    area_circulo = calcular_area_circulo(radio_circulo)
    area_rectangulo = calcular_area_rectangulo(longitud_rectangulo, anchura_rectangulo)

    # Resultados
    print(f"Área del círculo con radio {radio_circulo}: {area_circulo:.2f}")
    print(f"Área del rectángulo de {longitud_rectangulo} x {anchura_rectangulo}: {area_rectangulo:.2f}")


# Ejecución del programa
if __name__ == "__main__":
    mostrar_informacion()
