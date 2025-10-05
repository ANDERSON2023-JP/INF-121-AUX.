class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad}")
        print(f"CI: {self.ci}")

    def mayorDeEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

    def modificarEdad(self, nuevo):
        self.edad = nuevo
        print(f"La edad de {self.nombre} ha sido modificada a {self.edad} años.")
p1 = Persona("Ana", "López", "García", 22, "1234567")
p2 = Persona("Carlos", "López", "Mamani", 17, "7654321")
p1.mostrarDatos()
p2.mostrarDatos()
p1.mayorDeEdad()
p2.mayorDeEdad()
p2.modificarEdad(18)
p2.mayorDeEdad()

if p1.paterno == p2.paterno:
    print("Ambas personas tienen el mismo apellido paterno.")
else:
    print("Los apellidos paternos son diferentes.")
