class Mascota:
    def __init__(self, nombre, tipo, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia

    def alimentar(self):
        self.energia += 20
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nombre} fue alimentado. Energía actual: {self.energia}")

    def jugar(self):
        self.energia -= 15
        if self.energia < 0:
            self.energia = 0
        print(f"{self.nombre} jugó. Energía actual: {self.energia}")
m1 = Mascota("Firulais", "Perro", 60)
m2 = Mascota("Michi", "Gato", 80)
print(f"Energía inicial de {m1.nombre}: {m1.energia}")
print(f"Energía inicial de {m2.nombre}: {m2.energia}")
m1.alimentar()
m1.jugar()
m1.jugar()
m2.jugar()
m2.alimentar()
