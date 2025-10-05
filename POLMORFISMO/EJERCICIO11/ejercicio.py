class Pasajero:
    def __init__(self, nombre="", sexo="", nroHabitacion=0, costoPasaje=0):
        self.nombre = nombre
        self.sexo = sexo
        self.nroHabitacion = nroHabitacion
        self.costoPasaje = costoPasaje

    def __str__(self):
        return f"{self.nombre} ({self.sexo}) - Habitación {self.nroHabitacion}, Bs {self.costoPasaje}"


class Crucero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pasajeros = []
    def __iadd__(self, pasajero):
        self.pasajeros.append(pasajero)
        return self
    def __isub__(self, other):
        print(f"\n=== Datos del Crucero {self.nombre} ===")
        for p in self.pasajeros:
            print(p)
        return self
    def __eq__(self, other):
        total = sum(p.costoPasaje for p in self.pasajeros)
        print(f"Suma total del crucero {self.nombre}: Bs {total}")
        return total
    def __add__(self, other):
        if len(self.pasajeros) == len(other.pasajeros):
            print("Ambos cruceros tienen la MISMA cantidad de pasajeros.")
        else:
            print("Los cruceros tienen DIFERENTE cantidad de pasajeros.")
        return None
    def __sub__(self, other):
        hombres = sum(1 for p in self.pasajeros if p.sexo.lower() == "m")
        mujeres = sum(1 for p in self.pasajeros if p.sexo.lower() == "f")
        print(f"Crucero {self.nombre}: {hombres} hombres, {mujeres} mujeres.")
        return None

p1 = Pasajero("Juan Vargas", "M", 502, 500)
p2 = Pasajero("Martina Vasques", "F", 603, 1000)
p3 = Pasajero("Wilmer Montero", "M", 401, 925)
p4 = Pasajero("Lucía Pérez", "F", 404, 800)
p5 = Pasajero("Carlos Díaz", "M", 505, 700)

c1 = Crucero("Pacific Sun")
c2 = Crucero("Ocean Dream")

c1 += p1
c1 += p2
c1 += p3

c2 += p4
c2 += p5

c1 -= None
c2 -= None

c1 == c2  
c2 == c1  

c1 + c2

c1 - None
c2 - None
