class ManejadorDeArchivos:
    def __init__(self, nombre_archivo):
        """Constructor: Inicializa el ManejadorDeArchivos con un nombre de archivo y abre el archivo."""
        self.nombre_archivo = nombre_archivo
        self.archivo = None
        try:
            self.archivo = open(self.nombre_archivo, 'w')
            print(f"Archivo '{self.nombre_archivo}' abierto para escritura.")
        except Exception as e:
            print(f"Error al abrir el archivo '{self.nombre_archivo}': {e}")

    def escribir_datos(self, datos):
        """Método para escribir datos en el archivo."""
        if self.archivo:
            self.archivo.write(datos)
            print(f"Datos escritos en el archivo '{self.nombre_archivo}'.")
        else:
            print(f"El archivo '{self.nombre_archivo}' no está abierto. No se pueden escribir datos.")

    def __del__(self):
        """Destructor: Asegura que el archivo se cierre correctamente cuando se destruya el objeto."""
        if self.archivo:
            try:
                self.archivo.close()
                print(f"Archivo '{self.nombre_archivo}' cerrado.")
            except Exception as e:
                print(f"Error al cerrar el archivo '{self.nombre_archivo}': {e}")

# Demostración de constructores y destructores
def main():
    # Crear una instancia de ManejadorDeArchivos, lo que llama al constructor (__init__)
    manejador_de_archivos = ManejadorDeArchivos("ejemplo.txt")

    # Escribir datos en el archivo
    manejador_de_archivos.escribir_datos("¡Hola, Mundo!")

    # El destructor (__del__) se llama cuando se elimina el objeto o sale de alcance
    del manejador_de_archivos

if __name__ == "__main__":
    main()
