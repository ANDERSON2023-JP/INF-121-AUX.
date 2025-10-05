class Estudiante:
    def __init__(self, nombre="", apellidos="", parcial1=0, parcial2=0, exFinal=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.parcial1 = parcial1
        self.parcial2 = parcial2
        self.exFinal = exFinal
    def notaFinal(self, *args):
        if len(args) == 0:
            return self.parcial1 + self.parcial2 + self.exFinal
        elif len(args) == 1 and args[0] == "ponderado":
            return (self.parcial1 * 0.3) + (self.parcial2 * 0.3) + (self.exFinal * 0.4)
        else:
            print("Error: argumento no válido en notaFinal().")
            return None
    def aprobo(self, *args):
        nf = self.notaFinal("ponderado")

        if len(args) == 0:
            return nf >= 51
        elif len(args) == 1:
            minimo = args[0]
            return nf >= minimo
        elif len(args) == 2:
            minimo, extra = args
            return nf + extra >= minimo
        else:
            print("Error: cantidad de parámetros inválida en aprobo().")
            return None
    def mostrar(self, *args):
        if len(args) == 0:
            print(f"Nombre: {self.nombre} {self.apellidos}")
            print(f"Parcial 1: {self.parcial1}, Parcial 2: {self.parcial2}, ExFinal: {self.exFinal}")
        elif len(args) == 1 and args[0] == "final":
            nf = self.notaFinal("ponderado")
            print(f"{self.nombre} {self.apellidos} - Nota Final: {round(nf,2)}")
        else:
            print("Error: parámetro no válido en mostrar().")

e1 = Estudiante("Ana", "Pérez", 60, 70, 80)
e2 = Estudiante(nombre="Luis", apellidos="Torres", parcial1=40, parcial2=55, exFinal=65)
e3 = Estudiante()
e3.nombre = "Marta"
e3.apellidos = "López"
e3.parcial1 = 50
e3.parcial2 = 45
e3.exFinal = 70

e1.mostrar()
e1.mostrar("final")

print("Nota final ponderada e2:", e2.notaFinal("ponderado"))
print("Nota total e3:", e3.notaFinal())

print("¿e1 aprobó?", e1.aprobo())
print("¿e2 aprobó con mínimo 60?", e2.aprobo(60))
print("¿e3 aprobó con mínimo 70 y +10 extra?", e3.aprobo(70, 10))
