class Celular:
    def __init__(self, nroTel, dueno, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueno = dueno
        self.espacio = espacio  
        self.ram = ram          
        self.nroApp = nroApp

    def __add__(self, other):
        self.nroApp += 10
        print(f"Se aumentaron 10 aplicaciones. Total actual: {self.nroApp}")
        return self

    def __sub__(self, other):
        self.espacio -= 5
        if self.espacio < 0:
            self.espacio = 0
        print(f"Se redujo el espacio en 5 GB. Espacio disponible: {self.espacio} GB")
        return self

    def mostrar(self):
        print(f"Celular [Número: {self.nroTel}, Dueño: {self.dueno}, "
              f"Espacio: {self.espacio} GB, RAM: {self.ram} GB, Apps: {self.nroApp}]")

if __name__ == "__main__":
    c1 = Celular("78965412", "Carlos López", 64, 8, 25)

    print("=== Datos iniciales ===")
    c1.mostrar()

    print("\nAplicando operador ++ (aumentar número de apps)")
    c1 + 1   

    print("\nAplicando operador -- (reducir espacio)")
    c1 - 1   

    print("\n=== Datos finales ===")
    c1.mostrar()
