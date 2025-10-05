package EJERCICIO3;
public class Producto {
    private String nombre;
    private double precio;
    private int stock;

    // Constructor
    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    // Método vender
    public void vender(int cantidad) {
        if (cantidad <= stock) {
            stock -= cantidad;
            System.out.println("Se vendieron " + cantidad + " unidades de " + nombre + "."+"y su precio es"+precio+".");
        } else {
            System.out.println("No hay suficiente stock para realizar la venta.");
        }
    }

    // Método reabastecer
    public void reabastecer(int cantidad) {
        stock += cantidad;
        System.out.println("Se reabastecieron " + cantidad + " unidades de " + nombre + ".");
    }

    // Método principal (main)
    public static void main(String[] args) {
        Producto p1 = new Producto("Cereal", 15.5, 20);
        p1.vender(5);
        p1.reabastecer(10);
    }
}
