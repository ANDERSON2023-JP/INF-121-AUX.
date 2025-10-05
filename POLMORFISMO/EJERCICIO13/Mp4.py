class MP4:
    def __init__(self, cap_max=1000):
        self.canciones = [
            {"nombre": "Back To Black", "artista": "Amy Winehouse", "peso": 100},
            {"nombre": "Lost On You", "artista": "LP", "peso": 150}
        ]
        self.videos = [
            {"nombre": "Heathens", "artista": "twenty one pilots", "peso": 50},
            {"nombre": "Harmonica Andromeda", "artista": "KSHMR", "peso": 70},
            {"nombre": "Without Me", "artista": "Halsey", "peso": 30}
        ]
        self.cap_max = cap_max  

    def borrar(self, *args):
        if len(args) == 1:
            clave = args[0].lower()
            antes = len(self.canciones)
            self.canciones = [
                c for c in self.canciones
                if c["nombre"].lower() != clave and c["artista"].lower() != clave
            ]
            if len(self.canciones) < antes:
                print(f"Canción '{args[0]}' eliminada por nombre o artista.")
            else:
                print("No se encontró coincidencia.")
        elif len(args) == 2:
            nombre, peso = args
            antes = len(self.canciones)
            self.canciones = [
                c for c in self.canciones
                if not (c["nombre"].lower() == nombre.lower() and c["peso"] == peso)
            ]
            if len(self.canciones) < antes:
                print(f"Canción '{nombre}' eliminada por nombre y peso.")
            else:
                print("No se encontró coincidencia.")
        else:
            print("Error: parámetros inválidos para borrar().")

    def __add__(self, cancion):
        existe = any(c["nombre"].lower() == cancion["nombre"].lower()
                     for c in self.canciones)
        if not existe:
            if self.capacidadDisponible() >= cancion["peso"]:
                self.canciones.append(cancion)
                print(f"Canción '{cancion['nombre']}' añadida exitosamente.")
            else:
                print("No hay suficiente espacio para la canción.")
        else:
            print("La canción ya existe en el MP4.")
        return self

    def __sub__(self, video):
        existe = any(v["nombre"].lower() == video["nombre"].lower()
                     for v in self.videos)
        if not existe:
            if self.capacidadDisponible() >= video["peso"]:
                self.videos.append(video)
                print(f"Video '{video['nombre']}' añadido exitosamente.")
            else:
                print("No hay suficiente espacio para el video.")
        else:
            print("El video ya existe en el MP4.")
        return self

    def mostrar(self):
        print("\n=== Canciones ===")
        for c in self.canciones:
            print(f"{c['nombre']} - {c['artista']} ({c['peso']} Kb)")
        print("\n=== Videos ===")
        for v in self.videos:
            print(f"{v['nombre']} - {v['artista']} ({v['peso']} Mb)")
        print(f"\nCapacidad disponible: {self.capacidadDisponible()} Mb")

    def capacidadDisponible(self):
        total_canciones = sum(c["peso"] for c in self.canciones) / 1024  
        total_videos = sum(v["peso"] for v in self.videos)
        return round(self.cap_max - (total_canciones + total_videos), 2)


mp4 = MP4()

mp4.mostrar()

mp4.borrar("Lost On You")

mp4 + {"nombre": "Rolling in the Deep", "artista": "Adele", "peso": 120}

mp4 - {"nombre": "Believer", "artista": "Imagine Dragons", "peso": 40}

mp4.mostrar()
