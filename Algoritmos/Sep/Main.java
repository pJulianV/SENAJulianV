package SENAJulianV.Algoritmos.Sep;

import java.util.ArrayList;
import java.util.List;




// Clase Libro
class Libro {
    private String titulo;
    private String autor;
    private int anioPublicacion;

    public Libro(String titulo, String autor, int anioPublicacion) {
        this.titulo = titulo;
        this.autor = autor;
        this.anioPublicacion = anioPublicacion;
    }

    public String mostrarInformacion() {
        return "Título: " + titulo + ", Autor: " + autor + ", Año de Publicación: " + anioPublicacion;
    }
}

// Clase Biblioteca
class Biblioteca {
    private List<Libro> libros;

    public Biblioteca() {
        libros = new ArrayList<>();
    }

    public void agregarLibro(Libro libro) {
        libros.add(libro);
    }

    public void mostrarLibros() {
        for (Libro libro : libros) {
            System.out.println(libro.mostrarInformacion());
        }
    }
}

// Clase principal
public class Main {
    public static void main(String[] args) {
        // Creando objetos Libro
        Libro libro1 = new Libro("Cien años de soledad", "Gabriel García Márquez", 1967);
        Libro libro2 = new Libro("The Subtle Art of Not Giving a F*ck", "Mark Manson", 1985);
        Libro libro3 = new Libro("Hábitos Atómicos", "James Clear", 1605);

        // Creando el objeto Biblioteca
        Biblioteca biblioteca = new Biblioteca();

        // Agregando libros a la biblioteca
        biblioteca.agregarLibro(libro1);
        biblioteca.agregarLibro(libro2);
        biblioteca.agregarLibro(libro3);

        // Mostrando todos los libros en la biblioteca
        biblioteca.mostrarLibros();
    }
}