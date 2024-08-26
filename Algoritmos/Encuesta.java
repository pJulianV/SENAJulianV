import java.util.Random;

public class Encuesta {
    public static void main(String[] args) {
        int cantidadPersonas = 10;
        int[] sexo = new int[cantidadPersonas]; // 1=masculino, 2=femenino
        int[] trabaja = new int[cantidadPersonas]; // 1=si trabaja, 2=no trabaja
        int[] sueldo = new int[cantidadPersonas]; // Sueldo entre 300000 y 2000000

        Random random = new Random();

        // Generar datos aleatorios
        for (int i = 0; i < cantidadPersonas; i++) {
            sexo[i] = random.nextInt(2) + 1; // 1 o 2
            trabaja[i] = random.nextInt(2) + 1; // 1 o 2
            sueldo[i] = (trabaja[i] == 1) ? random.nextInt(1700001) + 300000 : 0; // Sueldo solo si trabaja
        }

        // Calcular porcentajes y sueldos
        int hombres = 0, mujeres = 0;
        int hombresTrabajan = 0, mujeresTrabajan = 0;
        int totalSueldoHombres = 0, totalSueldoMujeres = 0;

        for (int i = 0; i < cantidadPersonas; i++) {
            if (sexo[i] == 1) {
                hombres++;
                if (trabaja[i] == 1) {
                    hombresTrabajan++;
                    totalSueldoHombres += sueldo[i];
                }
            } else {
                mujeres++;
                if (trabaja[i] == 1) {
                    mujeresTrabajan++;
                    totalSueldoMujeres += sueldo[i];
                }
            }
        }

        // Calcular porcentajes
        double porcentajeHombres = (double) hombres / cantidadPersonas * 100;
        double porcentajeMujeres = (double) mujeres / cantidadPersonas * 100;
        double porcentajeHombresTrabajan = (double) hombresTrabajan / hombres * 100;
        double porcentajeMujeresTrabajan = (double) mujeresTrabajan / mujeres * 100;
        double sueldoPromedioHombres = (hombresTrabajan > 0) ? (double) totalSueldoHombres / hombresTrabajan : 0;
        double sueldoPromedioMujeres = (mujeresTrabajan > 0) ? (double) totalSueldoMujeres / mujeresTrabajan : 0;

        // Mostrar resultados
        System.out.printf("Porcentaje de hombres: %.2f%%\n", porcentajeHombres);
        System.out.printf("Porcentaje de mujeres: %.2f%%\n", porcentajeMujeres);
        System.out.printf("Porcentaje de hombres que trabajan: %.2f%%\n", porcentajeHombresTrabajan);
        System.out.printf("Porcentaje de mujeres que trabajan: %.2f%%\n", porcentajeMujeresTrabajan);
        System.out.printf("Sueldo promedio de hombres que trabajan: %.2f\n", sueldoPromedioHombres);
        System.out.printf("Sueldo promedio de mujeres que trabajan: %.2f\n", sueldoPromedioMujeres);
    }
}