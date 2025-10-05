class Cliente:
    def __init__(self, nombre, mesa):
        self.__nombre = nombre
        self.__mesa = mesa
        print(f"Cliente {self.__nombre} ha llegado y se ha sentado en la mesa {self.__mesa}.")
    def get_nombre(self):
        return self.__nombre

    def get_mesa(self):
        return self.__mesa
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_mesa(self, nueva_mesa):
        self.__mesa = nueva_mesa

    def __del__(self):
        print(f"Cliente {self.__nombre} se ha retirado de la cafetería.")

    def mostrar(self):
        print(f"Cliente: {self.__nombre} | Mesa: {self.__mesa}")


class Pedido:
    def __init__(self, producto, estado):
        self.__producto = producto
        self.__estado = estado
        print(f"Pedido de {self.__producto} registrado en estado '{self.__estado}'.")

    def get_producto(self):
        return self.__producto

    def get_estado(self):
        return self.__estado

    def set_producto(self, nuevo_producto):
        self.__producto = nuevo_producto

    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def __del__(self):
        print(f"Pedido de {self.__producto} ha sido eliminado del sistema.")

    def mostrar(self):
        print(f"Producto: {self.__producto} | Estado: {self.__estado}")


cliente1 = Cliente("Laura", 4)
pedido1 = Pedido("Capuchino", "Registrado")

print("\n--- Datos actuales ---")
cliente1.mostrar()
pedido1.mostrar()

cliente1.set_nombre("Laura Gómez")
pedido1.set_estado("Entregado")

print("\n--- Después de la actualización ---")
cliente1.mostrar()
pedido1.mostrar()
