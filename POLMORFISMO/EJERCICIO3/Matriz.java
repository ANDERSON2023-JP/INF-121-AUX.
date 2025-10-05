package EJERCICIO3;
public class Matriz {
    private float[][] matriz;
    private int n; 

    
    public Matriz(int n) {
        this.n = n;
        this.matriz = new float[n][n];
        for (int i = 0; i < n; i++) {
            matriz[i][i] = 1; 
        }
    }

    
    public Matriz(float[][] valores) {
        this.n = valores.length;
        this.matriz = new float[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                this.matriz[i][j] = valores[i][j];
            }
        }
    }

    public Matriz sumar(Matriz otra) {
        float[][] resultado = new float[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                resultado[i][j] = this.matriz[i][j] + otra.matriz[i][j];
            }
        }
        return new Matriz(resultado);
    }

    public Matriz restar(Matriz otra) {
        float[][] resultado = new float[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                resultado[i][j] = this.matriz[i][j] - otra.matriz[i][j];
            }
        }
        return new Matriz(resultado);
    }

    public boolean igual(Matriz otra) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (this.matriz[i][j] != otra.matriz[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public void mostrar() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        float[][] datos1 = {
                {1, 2},
                {3, 4}
        };

        float[][] datos2 = {
                {5, 6},
                {7, 8}
        };

        Matriz m1 = new Matriz(datos1);
        Matriz m2 = new Matriz(datos2);
        Matriz identidad = new Matriz(2);

        System.out.println("Matriz 1:");
        m1.mostrar();

        System.out.println("Matriz 2:");
        m2.mostrar();

        System.out.println("Matriz Identidad:");
        identidad.mostrar();

        Matriz suma = m1.sumar(m2);
        System.out.println("Suma de matrices:");
        suma.mostrar();

        Matriz resta = m1.restar(m2);
        System.out.println("Resta de matrices:");
        resta.mostrar();

        System.out.println("¿Matriz 1 es igual a Matriz 2?: " + m1.igual(m2));
    }
}

