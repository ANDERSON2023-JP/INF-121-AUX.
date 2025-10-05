package EJERCICIO2;

import java.util.Scanner;

public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    public Videojuego() {
        this.nombre = "Sin nombre";
        this.plataforma = "Desconocida";
        this.cantidadJugadores = 0;
    }

    public Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = 0;
    }

    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    public void agregarJugadores() {
        this.cantidadJugadores += 1;
        System.out.println("Se agregó 1 jugador. Total: " + cantidadJugadores);
    }

    public void agregarJugadores(int cantidad) {
        this.cantidadJugadores += cantidad;
        System.out.println("Se agregaron " + cantidad + " jugadores. Total: " + cantidadJugadores);
    }

    public void mostrar() {
        System.out.println("Videojuego: " + nombre +
                " | Plataforma: " + plataforma +
                " | Jugadores: " + cantidadJugadores);
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            
            Videojuego v1 = new Videojuego("Call of Duty", "PlayStation", 4);
            Videojuego v2 = new Videojuego("Minecraft", "PC");

            v1.mostrar();
            v2.mostrar();

            
            v1.agregarJugadores(); 

            System.out.print("Ingrese cantidad de jugadores para añadir a Minecraft: ");
            int cantidad = sc.nextInt();
            v2.agregarJugadores(cantidad);

            v1.mostrar();
            v2.mostrar();
        }
    }
}
