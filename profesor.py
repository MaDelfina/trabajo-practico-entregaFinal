from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, titulo, año_egreso):
        super().__init__(nombre, apellido, email, contraseña)
        self.__titulo = titulo
        self.__año_egreso = año_egreso

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def año_egreso(self):
        return self.__año_egreso
    
    def dictar_curso(self, curso):
        self.mis_cursos.append(curso)

    def __str__(self):
        return f'{super().__str__()}\nTitulo: {self.titulo}\nAño de egreso: {self.año_egreso}'