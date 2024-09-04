class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return "No hay libros prestados."
        return "\n".join([str(libro) for libro in self.libros_prestados])


class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN como clave, Libro como valor
        self.usuarios = {}  # ID de usuario como clave, Usuario como valor

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado de la biblioteca.")
        else:
            print("No se encontró el libro con el ISBN proporcionado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("El ID de usuario ya existe.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print("No se encontró al usuario con el ID proporcionado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]
        usuario.libros_prestados.append(libro)
        del self.libros[isbn]
        print(f"Libro prestado: {libro} a {usuario}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro_devuelto = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_devuelto = libro
                break

        if libro_devuelto:
            usuario.libros_prestados.remove(libro_devuelto)
            self.libros[isbn] = libro_devuelto
            print(f"Libro devuelto: {libro_devuelto}")
        else:
            print("El usuario no tiene prestado un libro con el ISBN proporcionado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if titulo and titulo.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif autor and autor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif categoria and categoria.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            return "\n".join([str(libro) for libro in resultados])
        else:
            return "No se encontraron libros que coincidan con los criterios de búsqueda."


# Pruebas del sistema
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Ficción", "978-3-16-148410-0")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "978-84-376-0494-7")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "978-2-07-061275-8")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("Ana García", "U002")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("U001", "978-3-16-148410-0")  # Prestar "Cien Años de Soledad"
biblioteca.prestar_libro("U002", "978-84-376-0494-7")  # Prestar "Don Quijote de la Mancha"

# Listar libros prestados
print(usuario1.listar_libros_prestados())
print(usuario2.listar_libros_prestados())

# Devolver libros
biblioteca.devolver_libro("U001", "978-3-16-148410-0")

# Buscar libros
print(biblioteca.buscar_libro(autor="Antoine de Saint-Exupéry"))

# Dar de baja un usuario
biblioteca.dar_de_baja_usuario("U002")
