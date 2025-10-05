class Sistema:
    def __init__(self, admins=None, autos=None):
        if admins is None:
            self.admins = []
            self.autos = []
            self.nroAdmins = 0
            self.nroAutos = 0
        else:
            self.admins = admins
            self.autos = autos
            self.nroAdmins = len(admins)
            self.nroAutos = len(autos)
    def mostrar(self):
        print("=== SISTEMA ===")
        print("Administradores:")
        for i, admin in enumerate(self.admins):
            print(f" {i+1}. {admin}")
        print("\nAutos:")
        for i, auto in enumerate(self.autos):
            print(f" {i+1}. Marca: {auto[0]}, Modelo: {auto[1]}, Color: {auto[2]}")
        print("-------------------------")
    def adicionar(self, *args):
        if len(args) == 1:
            admin = args[0]
            self.admins.append(admin)
            self.nroAdmins += 1
            print(f"Admin '{admin}' agregado correctamente.")
        elif len(args) == 3:
            marca, modelo, color = args
            self.autos.append((marca, modelo, color))
            self.nroAutos += 1
            print(f"Auto {marca} {modelo} {color} agregado correctamente.")
        else:
            print("Error: cantidad de argumentos inválida.")

s1 = Sistema()
s1.adicionar("Carlos")                 
s1.adicionar("Toyota", "Corolla", "Rojo")  
s1.adicionar("Nissan", "Versa", "Azul")
s1.mostrar()

admins_iniciales = ["Ana", "Pedro"]
autos_iniciales = [("Ford", "Fiesta", "Gris"), ("Kia", "Rio", "Negro")]
s2 = Sistema(admins_iniciales, autos_iniciales)
s2.mostrar()
