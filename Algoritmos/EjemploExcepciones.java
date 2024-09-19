package SENAJulianV.Algoritmos;


public class EjemploExcepciones {
    public static void main(String[] args) {
        try {
            int resultado = dividir(10, 0);  // Intentamos dividir por cero
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: No se puede dividir por cero.");  // Captura el error
        }
    }

    public static int dividir(int a, int b) {
        return a / b;  // Realiza la división
    }
}