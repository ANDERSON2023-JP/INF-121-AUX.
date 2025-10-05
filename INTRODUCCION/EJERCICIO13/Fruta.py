class Fruta:
    def __init__(self, nombre, tipo, vitaminas):
        self.nombre = nombre
        self.tipo = tipo
        self.vitaminas = vitaminas
        self.nroVitaminas = len(vitaminas)

    def mostrar(self):
        print(f"Fruta: {self.nombre}, Tipo: {self.tipo}, "
              f"Nro de Vitaminas: {self.nroVitaminas}, "
              f"Vitaminas: {', '.join(self.vitaminas)}")

    def contarVitaminas(self):
        return self.nroVitaminas

    def esCitrica(self):
        return "C" in self.vitaminas


#Instanciar de 3 maneras diferentes
fruta1 = Fruta("Naranja", "Cítrica", ["C", "A", "B1"])
fruta2 = Fruta(nombre="Manzana", tipo="Templada", vitaminas=["B6", "E", "C"])
fruta3 = Fruta("Kiwi", "Subtropical", list(("C", "E", "K")))

frutas = [fruta1, fruta2, fruta3]

#Fruta con más vitaminas
fruta_max = max(frutas, key=lambda f: f.contarVitaminas())
print(f"La fruta con más vitaminas es: {fruta_max.nombre}")

#Mostrar las vitaminas de la fruta 'Kiwi'
for f in frutas:
    if f.nombre.lower() == "kiwi":
        print(f"Vitaminas del {f.nombre}: {', '.join(f.vitaminas)}")

#Cuántas frutas tienen vitamina C (cítricas)
citricas = sum(f.esCitrica() for f in frutas)
print(f"Cantidad de frutas con vitamina C: {citricas}")

#Ordenado  las vitaminas en forma alfabéticamente
for f in frutas:
    f.vitaminas.sort()

print("\n--- Frutas ordenadas alfabéticamente por vitaminas ---")
for f in frutas:
    f.mostrar()
