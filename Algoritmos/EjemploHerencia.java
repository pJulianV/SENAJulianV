package SENAJulianV.Algoritmos;

class Animal {  // Clase padre
    public void hacerRuido() {
        System.out.println("El animal hace un ruido");
    }
}

class Perro extends Animal {  // Clase hija
    @Override
    public void hacerRuido() {
        System.out.println("El perro ladra");
    }
}

public class EjemploHerencia {
    public static void main(String[] args) {
        Perro miPerro = new Perro();
        miPerro.hacerRuido();  // Llama al método del perro
    }
}