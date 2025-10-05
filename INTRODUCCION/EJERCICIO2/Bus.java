public class Bus {
    private int pasajerosActuales;
    private int capacidadPasajeros;
    private double costoPasaje;

    public Bus(int capacidadPasajeros, double costoPasaje){
        this.capacidadPasajeros = capacidadPasajeros;
        this.costoPasaje = costoPasaje;
        this.pasajerosActuales = 0;
    }

    public void subirPasajeros(int cantidad){
        if (pasajerosActuales + cantidad <= capacidadPasajeros) {
            pasajerosActuales += cantidad;
            System.out.println(cantidad + " pasajeros subieron. Ahora hay " + pasajerosActuales + " en el bus.");
        } else {
            int disponibles = capacidadPasajeros - pasajerosActuales;
            System.out.println("No se pueden subir " + cantidad + " pasajeros. Solo hay espacio para " + disponibles + ".");
        }
    }

    public void cobrarPasaje(){
        double total = pasajerosActuales * costoPasaje;
        System.out.println("Se cobró un total de Bs. " + total + " por " + pasajerosActuales + " pasajeros.");
    }

    public void asientosDisponibles(){
        int disponibles = capacidadPasajeros - pasajerosActuales;
        System.out.println("Asientos disponibles: " + disponibles);
    }

    public void mostrarInformacion(){
        System.out.println("--------------- INFORMACIÓN ---------------");
        System.out.println("Capacidad máxima: " + capacidadPasajeros);
        System.out.println("Pasajeros actuales: " + pasajerosActuales);
        System.out.println("Costo de pasaje: Bs. " + costoPasaje);
        System.out.println("------------------------------------------");
    }
    public static void main(String[] args) {
        Bus bus1 = new Bus(58, 1.50);
        bus1.mostrarInformacion();
        bus1.subirPasajeros(20);
        bus1.subirPasajeros(40);
        bus1.cobrarPasaje();
        bus1.asientosDisponibles();
    }
}
