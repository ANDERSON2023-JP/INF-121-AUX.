class CamaraSeguridad:
    def __init__(self, id_camara, ubicacion, estado, resolucion):
        self.id_camara = id_camara
        self.ubicacion = ubicacion
        self.estado = estado
        self.resolucion = resolucion

    def activar(self):
        self.estado = "Activa"
        print(f"Cámara {self.id_camara} activada.")

    def mostrar(self):
        print(f"Cámara {self.id_camara} | Ubicación: {self.ubicacion} | Estado: {self.estado} | Resolución: {self.resolucion}")

class OficialEncubierto:
    def __init__(self, nombre, rango, edad, disfraz):
        self.nombre = nombre
        self.rango = rango
        self.edad = edad
        self.disfraz = disfraz

    def patrullar(self):
        print(f"El oficial {self.nombre} ({self.disfraz}) está patrullando la zona.")

    def mostrar(self):
        print(f"Oficial: {self.nombre}, Rango: {self.rango}, Edad: {self.edad}, Disfraz: {self.disfraz}")

class SistemaRadio:
    def __init__(self, frecuencia, canal, estado, alcance):
        self.frecuencia = frecuencia
        self.canal = canal
        self.estado = estado
        self.alcance = alcance

    def transmitir(self, mensaje):
        print(f"Transmitiendo en canal {self.canal}: {mensaje}")

    def mostrar(self):
        print(f"Radio | Frecuencia: {self.frecuencia} | Canal: {self.canal} | Estado: {self.estado} | Alcance: {self.alcance} m")

class CocineroPolicial:
    def __init__(self, nombre, experiencia, especialidad, entrenamiento):
        self.nombre = nombre
        self.experiencia = experiencia
        self.especialidad = especialidad
        self.entrenamiento = entrenamiento

    def prepararComida(self):
        print(f"{self.nombre} está preparando salchipapas ({self.especialidad}).")

    def responderEmergencia(self):
        print(f"{self.nombre} activa protocolo de defensa policial.")

    def mostrar(self):
        print(f"Cocinero: {self.nombre} | Experiencia: {self.experiencia} años | Especialidad: {self.especialidad} | Entrenamiento: {self.entrenamiento}")
        
camara1 = CamaraSeguridad(1, "Entrada", "Inactiva", "1080p")
oficial1 = OficialEncubierto("Luis Pérez", "Sargento", 30, "Vendedor de salchipapas")
radio1 = SistemaRadio("2.4GHz", 7, "Activa", 500)
cocinero1 = CocineroPolicial("Carlos Gómez", 5, "Salchipapas con papas rústicas", "Artes Marciales")

camara1.activar()
oficial1.patrullar()
radio1.transmitir("Todo bajo control en el puesto.")
cocinero1.prepararComida()
cocinero1.responderEmergencia()

print("\n--- Estado del sistema encubierto ---")
camara1.mostrar()
oficial1.mostrar()
radio1.mostrar()
cocinero1.mostrar()
