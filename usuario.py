from abc import ABC

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contraseña):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contraseña = contraseña
        self.mis_cursos = []

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def contraseña(self):
        return self.__contraseña
    
    def __str__(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}\nContraseña: {self.contraseña}'
    def validar_credenciales(self, email, contraseña):

        return self.email == email and self.contraseña == contraseña