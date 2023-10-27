import random
import string

class Curso:
    def __init__(self, nombre, codigo, contraseña_matriculacion):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__contraseña_matriculacion = contraseña_matriculacion
        self.archivos = []
        self.cantidad_archivos = 0 
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def contraseña_matriculacion(self):
        return self.__contraseña_matriculacion
    
    def __str__(self):
        return f'Nombre: {self.nombre}\nContraseña de matriculación: {self.contraseña_matriculacion}'
    
    def nuevo_archivo(self, archivo):
        self.archivos.append(archivo)
        self.cantidad_archivos += 1

    def generar_contasenia(self):
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
    
    @property
    def generar_contrasenia(self):
        return self.generar_contasenia()