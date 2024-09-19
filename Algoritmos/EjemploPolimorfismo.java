package SENAJulianV.Algoritmos;

class Animal {  
    public void hacerRuido() {
        System.out.println("El animal hace un ruido");
    }
}

class Perro extends Animal {  
    @Override
    public void hacerRuido() {
        System.out.println("El perro ladra");
    }
}

class Gato extends Animal {  
    @Override
    public void hacerRuido() {
        System.out.println("El gato maúlla");
    }
}

public class EjemploPolimorfismo {
    public static void main(String[] args) {
        Animal miAnimal1 = new Perro();  // Un perro como animal
        Animal miAnimal2 = new Gato();   // Un gato como animal
        
        miAnimal1.hacerRuido();  // Imprime "El perro ladra"
        miAnimal2.hacerRuido();  // Imprime "El gato maúlla"
    }
}