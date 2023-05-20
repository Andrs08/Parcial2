from typing import List, Dict
#Se crea la clase persona que servira el conductor y los asistentes
class Persona:
    def __init__(self, id: int, nombre: str, apellido: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
#Se crea la clase camion y se le asigna un conductor y dos asistentes a traves de instancias de la clase persona 
class Camion:
    def __init__(self, id: int, conductor: Persona, asistente1: Persona, asistente2: Persona):
        self.id = id
        self.conductor = conductor
        self.asistente1 = asistente1
        self.asistente2 = asistente2
#Se establece un punto geografico conformado por una latitud y longitud
class Ubicacion:
    def __init__(self, latitud: float, longitud: float):
        self.latitud = latitud
        self.longitud = longitud
#Se hace una lista de puntos geograficos que describira una ruta
class Ruta:
    def __init__(self, puntos: List[Ubicacion]):
        self.puntos = puntos
#La clase turno le asignara a un camion conformado por conductor y asistentes, una ruta y definira la fecha en la que empieza y termina su turno
class Turno:
    def __init__(self, camion: Camion, fecha_inicio, fecha_fin, ruta: Ruta):
        self.camion = camion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.ruta = ruta
        self.residuos = {
            "vidrio": 0,
            "papel": 0,
            "plastico": 0,
            "metal": 0,
            "residuos_organicos": 0,
        }
#Este metodo se encarga de establecer la cantidad de residuos recogida en este turno, para ello actualizara su valor en el diccionario
    def recolectar_residuos(self, residuos: Dict):
        for tipo_residuo, cantidad in residuos.items():
            if tipo_residuo in self.residuos:
                self.residuos[tipo_residuo] += cantidad
            else:
                raise ValueError(f"Tipo de residuo desconocido: {tipo_residuo}")

class CentroAcopio:
#Se usa el patrón de diseño Singleton para garantizar que solo haya una instancia de la clase CentroAcopio en todo el programa
    instance = None

    @staticmethod
    #Este metodo se encarga de instanciar centro de aocpio siempre y cuando no exista una instancia anterior a esta 
    def getInstance():
        if CentroAcopio.instance is None:
            CentroAcopio.instance = CentroAcopio()
        return CentroAcopio.instance

    def __init__(self):
        if CentroAcopio.instance is not None:
            raise Exception("Esta clase es un Singleton. Utilice el método getInstance() para obtener su instancia.")
        self.turnos = []
#Se añaden diferentes turnos a una lista
    def agregar_turno(self, turno: Turno, fecha):
        self.turnos.append((turno, fecha))
#Este metodo recorrera la lista de turnos y sumara el vidrio recogido en cada uno de ellos siempre y cuando se hayan realizado el dia especificado
    def vidrio_recolectado_por_dia(self, dia):
        total_vidrio = 0.0
        for turno, fecha in self.turnos:
            if fecha == dia:
                total_vidrio += turno.residuos.get("vidrio", 0)
        return total_vidrio

class Factory:
#Se utiliza el patron de diseño Factory Method para simplificar y centralizar la creación de objetos de diferentes clases
    def crear_camion(self, id: int, conductor: Persona, asistente1: Persona, asistente2: Persona) -> Camion:
        return Camion(id, conductor, asistente1, asistente2)

    def crear_persona(self, id: int, nombre: str, apellido: str) -> Persona:
        return Persona(id, nombre, apellido)

    def crear_ruta(self, puntos: List[Ubicacion]) -> Ruta:
        return Ruta(puntos)

    def crear_ubicacion(self, latitud: float, longitud: float) -> Ubicacion:
        return Ubicacion(latitud, longitud)

    def crear_turno(self, camion: Camion, fecha_inicio, fecha_fin, ruta: Ruta) -> Turno:
        return Turno(camion, fecha_inicio, fecha_fin, ruta)
#Se usa el patron Decorator para agregar funcionalidades adicionales a un objeto de tipo Turno sin modificar su estructura o comportamiento original
class TurnoDecorator(Turno):
    def __init__(self, turno: Turno):
        self.turno = turno

    def add_residuos(self, residuos: Dict):
        self.turno.add_residuos(residuos)

class TurnoConParadas(TurnoDecorator):
    def incrementar_paradas(self):
        pass

    def add_residuos(self, residuos: Dict):
        super().add_residuos(residuos)

        

factory = Factory()
#Se usa el patron de diseño Factory para crear las instancias necesarias para crear el camion y el turno
#Turno1
conductor = factory.crear_persona(1, "Juan", "Pérez")
asistente1 = factory.crear_persona(2, "Pedro", "García")
asistente2 = factory.crear_persona(3, "María", "Rodríguez")
camion = factory.crear_camion(1, conductor, asistente1, asistente2)
ubicacion1 = factory.crear_ubicacion(12.34, 56.78)
ubicacion2 = factory.crear_ubicacion(23.45, 67.89)
ruta = factory.crear_ruta([ubicacion1, ubicacion2])
fecha_inicio = "2023-05-19"
fecha_fin = "2023-05-19"
turno = factory.crear_turno(camion, fecha_inicio, fecha_fin, ruta)
#Se establece las cantidades de residuos recogidos en el turno
residuos = {"vidrio": 17, "papel": 5, "plastico": 8}
turno.recolectar_residuos(residuos)
#Se instancia el centro de acopio
centroacopio = CentroAcopio.getInstance()
# Agregar el turno al CentroAcopio
centroacopio.agregar_turno(turno, fecha_inicio)

#turno2
conductor = factory.crear_persona(4, "Luis", "Martinez")
asistente1 = factory.crear_persona(5, "Santiago", "Ortiz")
asistente2 = factory.crear_persona(6, "Camila", "Miranda")
camion = factory.crear_camion(2, conductor, asistente1, asistente2)
ubicacion1 = factory.crear_ubicacion(8.91, 43.1)
ubicacion2 = factory.crear_ubicacion(17.56, 91.5)
ruta = factory.crear_ruta([ubicacion1, ubicacion2])
fecha_inicio = "2023-05-19"
fecha_fin = "2023-05-19"
turno = factory.crear_turno(camion, fecha_inicio, fecha_fin, ruta)
residuos = {"vidrio": 16, "papel": 5, "plastico": 8}
turno.recolectar_residuos(residuos)
centroacopio.agregar_turno(turno, fecha_inicio)

#turno3
conductor = factory.crear_persona(7, "Esteban", "Ruiz")
asistente1 = factory.crear_persona(8, "Sandra", "Iriarte")
asistente2 = factory.crear_persona(9, "Juana", "Rodriguez")
camion = factory.crear_camion(3, conductor, asistente1, asistente2)
ubicacion1 = factory.crear_ubicacion(12.34, 56.78)
ubicacion2 = factory.crear_ubicacion(23.45, 67.89)
ruta = factory.crear_ruta([ubicacion1, ubicacion2])
fecha_inicio = "2023-05-19"
fecha_fin = "2023-05-19"
turno = factory.crear_turno(camion, fecha_inicio, fecha_fin, ruta)
residuos = {"vidrio": 23, "papel": 5, "plastico": 8}
turno.recolectar_residuos(residuos)
centroacopio.agregar_turno(turno, fecha_inicio)

#turno4
conductor = factory.crear_persona(10, "Jorge", "Gonzalez")
asistente1 = factory.crear_persona(11, "Adrian", "Marquez")
asistente2 = factory.crear_persona(12, "Lina", "Blanco")
camion = factory.crear_camion(4, conductor, asistente1, asistente2)
ubicacion1 = factory.crear_ubicacion(12.34, 56.78)
ubicacion2 = factory.crear_ubicacion(83.2, 72.46)
ruta = factory.crear_ruta([ubicacion1, ubicacion2])
fecha_inicio = "2023-05-18"
fecha_fin = "2023-05-18"
turno = factory.crear_turno(camion, fecha_inicio, fecha_fin, ruta)
residuos = {"vidrio": 10, "papel": 5, "plastico": 8}
turno.recolectar_residuos(residuos)
centroacopio.agregar_turno(turno, fecha_inicio)

# Calcular la cantidad de vidrio recogido en un día específico, la cantidad recogida en el turno 4 no se sumara, ya que se realizo en un dia diferente
dia = "2023-05-19"
total_vidrio = centroacopio.vidrio_recolectado_por_dia(dia)
print(f"La cantidad de vidrio recogido en toneladas el {dia} fue de: {total_vidrio}")