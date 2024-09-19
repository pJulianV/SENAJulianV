# Clase Libro
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}'

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.mostrar_informacion())


if __name__ == "__main__":
    # Creando objetos Libro
    libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 1967)
    libro2 = Libro('The Subtle Art of dont Give a F*', 'Mark Manson', 1985)
    libro3 = Libro('Habitos Atomicos', 'James Clear', 1605)

    # Creando el objeto Biblioteca
    biblioteca = Biblioteca()

    # Agregando libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Mostrando todos los libros en la biblioteca
    biblioteca.mostrar_libros()