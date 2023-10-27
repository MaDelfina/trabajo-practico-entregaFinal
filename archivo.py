class Archivo:
    def __init__(self, nombre, fecha, formato):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__formato = formato

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def formato(self):
        return self.__formato
    
    def __str__(self):
        return f'Nombre: {self.nombre}\n Fecha: {self.fecha}\n Formato: {self.formato}'
