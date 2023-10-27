class Carrera:
    def __init__(self, nombre, cant_anios):
        self.__nombre = nombre
        self.__cant_anios = cant_anios

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cant_anios(self):
        return self.__cant_anios
    
    def __str__(self):
        return f'Nombre: {self.nombre}\n Cantidad de años: {self.cant_anios}'