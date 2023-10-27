from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contraseña)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    @property
    def legajo(self):
        return self.__legajo
    
    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    def __str__(self):
        return f'{super().__str()}\nLegajo: {self.legajo}\nAño de inscripción a la carrera: {self.anio_inscripcion_carrera}'
    
    def matricular_en_curso(self, curso):
        self.mis_cursos.append(curso)
        
    def desmatricular_curso(self, curso):
        self.mis_cursos.remove(curso)