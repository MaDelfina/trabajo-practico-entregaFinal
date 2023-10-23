from abc import ABC
import random
import string

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

class Curso:
    def __init__(self, prox_cod, nombre, codigo, contraseña_matriculacion):
        self.__prox_cod = prox_cod
        self.__nombre = nombre
        self.__codigo = codigo
        self.__contraseña_matriculacion = contraseña_matriculacion
    @property 
    def prox_cod(self):
        return self.__prox_cod
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
    #def nuevo_archivo(self, archivo):
    def generar_contasenia(self):
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
    @property
    def generar_contrasenia(self):
        return self.generar_contasenia()
    
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
    #def get_cantidad_materias(self):

estudiante1 = Estudiante("Sofia", "Marquez", "sofiamarquez@gmail.com", "contra1", 1, 2020)
profesor1 = Profesor("Jose", "Diaz", "josediaz@gmail.com", "contra2", "Programacion", 2019)
carrera = Carrera("Programacion", 3)
mis_cursos = []

def ingresar_como_alumno():
    email = input("Ingresa tu email: ")
    password = input("Ingresa tu contraseña: ")

    for estudiante in [estudiante1]:
        if estudiante.email == email:
            if estudiante.email == email and estudiante.contraseña == password:
                print("Acceso permitido como alumno.")
            
                while True:
                    print("\nSubmenú de alumno:")
                    print("1 - Matricularse a un curso")
                    print("2 - desmatricularse a un curso")
                    print("3 - Ver curso")
                    print("4 - Volver al menú principal")
                    opcionAlumno = input("Selecciona una opción: ")
                
                    if opcionAlumno == "1":
                        print("Cursos disponibles:")
                        for i, curso in enumerate(mis_cursos,1): #enumerate sirve para recorrer la lista de cursos matriculados y comenzar el índice en 1. Esto nos permite enumerar los cursos matriculados y mostrar su nombre junto con su índice en la lista.
                            print(f"{i} - {curso.nombre}")
    
                        curso_a_matricular = int(input("Ingresa el número del curso al que deseas matricularte: "))
        
                        if 1 <= curso_a_matricular <= len(mis_cursos):
                         curso_seleccionado = mis_cursos[curso_a_matricular - 1] #porque arranca en 0
            
                         if curso_seleccionado not in estudiante.mis_cursos:
                           estudiante.matricular_en_curso(curso_seleccionado)
                           print(f"Te has matriculado en el curso: Nombre: {curso_seleccionado.nombre}\n Codigo: {curso_seleccionado.codigo} Contraseña: {curso_seleccionado.contraseña_matriculacion}")
                         else:
                            print("Ya estás matriculado en este curso.")
                        else:
                            print("Número de curso no válido. Ingresa un número entre 1 y", len(mis_cursos))

                    elif opcionAlumno == "2":
                        for i, curso in enumerate(curso_seleccionado, 1):
                            print(f"{i} - {curso.nombre}")
                        
                        curso_a_desmatricular = input("Ingrese el numero del curso al que se quiere desmatricular: ")

                        if 1 <= curso_a_desmatricular <= len(mis_cursos):
                            curso_seleccionado = mis_cursos[curso_a_desmatricular - 1]

                            if curso_seleccionado not in estudiante.mis_cursos:
                                estudiante.desmatricular_curso(curso_seleccionado)
                                print(f"Te has matriculado en el curso: Nombre: {curso_seleccionado.nombre}\n Codigo: {curso_seleccionado.codigo} Contraseña: {curso_seleccionado.contraseña_matriculacion}")
                            else:
                                print("Ya te desmatriculaste de este curso.")
                        else:
                            print("Número de curso no válido. Ingresa un número entre 1 y", len(mis_cursos))

                    elif opcionAlumno == "3":
                        if not estudiante.mis_cursos:
                            print("No estás matriculado en ningún curso.")
                        else:
                            print("Cursos en los que estás matriculado:")
                            for i, curso in enumerate(estudiante.mis_cursos, 1):
                              print(f"{i} - {curso.nombre}")

                    elif opcionAlumno == "4":
                        print("Volviendo al menú principal.")
                        break
                    else:
                     print("Opción no válida. Por favor, elige una opción válida.")
            else:
                print("Contraseña incorrecta. Acceso denegado.")
        else:
            print("El email no está registrado como alumno. Debes darte de alta.")

def ingresar_como_profesor():
    email = input("Ingresa tu email como profesor: ")
    password = input("Ingresa tu contraseña: ")

    for profesor in [profesor1]:
        if profesor.email == email:
            if profesor.email == email and profesor.contraseña == password:
                print("Acceso permitido como profesor.")
            
                while True:
                    print("\nSubmenú de profesor:")
                    print("1 - Dictar curso")
                    print("2 - Ver curso")
                    print("3 - Volver al menú principal")
                    opcionProfesor = input("Selecciona una opción: ")
                
                    if opcionProfesor == "1":
                        nombre_curso = input("Ingrese el nombre del curso: ")
                        contrasena_curso = nuevo_curso.generar_contrasenia() #se tiene que generar automaticamente pero no nos sale
                        codigo_curso = input("Ingrese el codigo del curso: ")

                        nuevo_curso = Curso(nombre_curso, contrasena_curso)
                        profesor.dictar_curso(nuevo_curso)
                        mis_cursos.append(nuevo_curso)  # Agregar el curso a la lista mis_cursos

                        print(f"Nombre: {nombre_curso}")
                        print(f"Contraseña: {contrasena_curso}")
                        print(f"Codigo: {codigo_curso}")

                    elif opcionProfesor == "2":
                        if not profesor.mis_cursos:
                            print("No tienes cursos asignados.")
                        else:
                            print("Cursos:")
                            for curso in profesor.mis_cursos:
                                print(curso.nombre)

                    elif opcionProfesor == "3":
                        print("Volviendo al menú principal.")
                        break
                    else:
                        print("Opción no válida. Por favor, elige una opción válida.")
            else:
                print("Contraseña incorrecta. Acceso denegado.")
        else:
            print("El email no está registrado como profesor. Debes darte de alta.")
    
def ver_cursos():
    print("Cursos disponibles:")
    for curso in mis_cursos:
        print(curso.nombre)

def mostrar_menu():
    print("Menú:")
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

while True:
    opcion = mostrar_menu()
    if opcion == "1":
        ingresar_como_alumno()
        
    elif opcion == "2":
        ingresar_como_profesor()

    elif opcion == "3":
        ver_cursos()
    
    elif opcion == "4":
        print('Salir')
        break
    else:
        print('Error')