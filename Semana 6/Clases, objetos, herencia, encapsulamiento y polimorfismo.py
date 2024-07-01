class Book:
    def __init__(self, titulo, autor, paginas):
        # Atributos encapsulados
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    # Métodos para acceder a los atributos encapsulados
    def get_title(self):
        return self.__titulo

    def get_author(self):
        return self.__autor

    def get_pages(self):
        return self.__paginas

    # Método para obtener la información del libro
    def get_info(self):
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Paginas: {self.__paginas}"

class EBook(Book):
    def __init__(self, titulo, autor, paginas, file_size):
        # Llamar al constructor de la clase base
        super().__init__(titulo, autor, paginas)
        self.__file_size = file_size

    # Sobrescribir el método get_info para incluir el tamaño del archivo
    def get_info(self):
        # Llamar al método get_info de la clase base
        base_info = super().get_info()
        return f"{base_info}, File Size: {self.__file_size}MB"

if __name__ == "__main__":
    # Crear una instancia de Book
    book = Book("1984", "George Orwell", 328)
    print(book.get_info())

    # Crear una instancia de EBook
    ebook = EBook("Brave New World", "Aldous Huxley", 288, 2)
    print(ebook.get_info())
