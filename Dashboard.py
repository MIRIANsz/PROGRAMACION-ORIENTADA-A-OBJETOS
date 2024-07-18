import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'SEMANA 2/Abstracción.py',
        '2': 'Semana 3/Programacion Orientada a Objetos.py',
        '3': 'EjemplosMundoReal_POO/Boleto de Avion.py',
        '4': 'Semana 5/Cálculo del área de un circulo.py',
        '5': 'Semana 6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '6': 'Semana 7/Manejo de Archivos.py',
    }

    def mostrar_codigo(ruta_script):
        # Asegúrate de que la ruta al script es absoluta
        ruta_base = os.path.dirname(__file__)
        ruta_script_absoluta = os.path.abspath(os.path.join(ruta_base, ruta_script))
        try:
            with open(ruta_script_absoluta, 'r') as archivo:
                print(f"\n--- Código de {ruta_script} ---\n")
                print(archivo.read())
        except FileNotFoundError:
            print("El archivo no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

    if __name__ == "__main__":
        while True:
            print("\nMenu Principal - Dashboard")
            for key in opciones:
                print(f"{key} - {opciones[key]}")
            print("0 - Salir")

            eleccion = input("Elige un script para ver su código o '0' para salir: ")
            if eleccion == '0':
                break
            elif eleccion in opciones:
                ruta_script = opciones[eleccion]
                mostrar_codigo(ruta_script)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
