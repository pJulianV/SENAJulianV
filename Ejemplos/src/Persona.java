// Clase Persona
public class Persona {
    // Atributos de la clase
    private String nombre;
    private int edad;

    // Constructor por defecto
    public Persona() {
        this.nombre = "Desconocido";
        this.edad = 0;
    }

    // Constructor con parámetros
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Método para mostrar la información de la persona
    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
    }

    // Método principal
    public static void main(String[] args) {
        // Crear objeto usando el constructor por defecto
        Persona persona1 = new Persona();
        persona1.mostrarInformacion();

        // Crear objeto usando el constructor con parámetros
        Persona persona2 = new Persona("Juan", 30);
        persona2.mostrarInformacion();
    }
}