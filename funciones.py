from estudiante import Estudiante
from profesor import Profesor
from carrera import Carrera
from curso import Curso
from archivo import Archivo
from datetime import datetime

estudiante1 = Estudiante("Sofia", "Marquez", "sofia", "contra1", 1, 2020)
profesor1 = Profesor("Jose", "Diaz", "jose", "contra2", "Programacion", 2019)
carrera1 = Carrera("Programacion", 3)
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
                    print("2 - Desmatricularse a un curso")
                    print("3 - Ver curso")
                    print("4 - Volver al menú principal")
                    opcionAlumno = input("Selecciona una opción: ")
                
                    if opcionAlumno == "1":
                        print("Cursos disponibles:")
                        for i, curso in enumerate(mis_cursos, 1):  # Reemplaza cursos_disponibles con tu lista real
                            print(f"{i} - {curso.nombre}")

                        curso_a_matricular = int(input("Ingresa el número del curso al que deseas matricularte: "))

                        if 1 <= curso_a_matricular <= len(mis_cursos):
                            curso_seleccionado = mis_cursos[curso_a_matricular - 1]

                            if curso_seleccionado not in estudiante.mis_cursos:
                                estudiante.matricular_en_curso(curso_seleccionado)
                                print(f"Te has matriculado en el curso: {curso_seleccionado.nombre}")
                            else:
                                print("Ya estás matriculado en este curso.")
                        else:
                            print("Número de curso no válido. Ingresa un número entre 1 y", len(mis_cursos))

                    elif opcionAlumno == "2":
                        if len(estudiante.mis_cursos) > 0:
                            print("Cursos en los que estás matriculado:")
                            for i, curso in enumerate(estudiante.mis_cursos, 1):
                                print(f"{i} - {curso.nombre}")

                            curso_a_desmatricular = int(input("Ingresa el número del curso al que deseas desmatricularte: "))

                            if 1 <= curso_a_desmatricular <= len(estudiante.mis_cursos):
                                curso_seleccionado = estudiante.mis_cursos[curso_a_desmatricular - 1]

                                if curso_seleccionado in estudiante.mis_cursos:
                                    estudiante.desmatricular_curso(curso_seleccionado)
                                    print(f"Te has desmatriculado del curso: Nombre: {curso_seleccionado.nombre}")
                                else:
                                    print("No estás matriculado en este curso.")
                            else:
                                print("Número de curso no válido.")
                        else:
                            print("No estás matriculado en ningún curso.")

                    elif opcionAlumno == "3":
                        if not estudiante.mis_cursos:
                            print("No estás matriculado en ningún curso.")
                        else:
                            print("Cursos matriculados:")
                            for i, curso in enumerate(estudiante.mis_cursos, 1):
                                print(f"{i} {curso.nombre}")

                            curso_seleccionado = input("Ingresa el número del curso que deseas ver: ")
                            if curso_seleccionado.isdigit():
                                curso_seleccionado = int(curso_seleccionado)
                                if 1 <= curso_seleccionado <= len(estudiante.mis_cursos):
                                    curso = estudiante.mis_cursos[curso_seleccionado - 1]
                                    print(f"Nombre del curso: {curso.nombre}")

                                    # Ordenar los archivos del curso del más antiguo al más nuevo
                                    curso.archivos.sort(key=lambda archivo: archivo.fecha)

                                    for archivo in curso.archivos:
                                        print("Archivos en el curso:")
                                        print(archivo.nombre)
                                else:
                                    print("Número de curso no válido. Ingresa un número entre 1 y", len(estudiante.mis_cursos))
                            else:
                                print("Ingrese un número válido.")

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
                        contrasena_curso = input("Ingrese una contraseña: ")
                        codigo_curso = int(input("Ingrese un código: "))

                        nuevo_curso = Curso(nombre_curso, contrasena_curso, codigo_curso)

                        profesor.dictar_curso(nuevo_curso)
                        mis_cursos.append(nuevo_curso)

                        print(f"Curso dado de alta con éxito:")
                        print(f"Nombre: {nuevo_curso.nombre}")
                        print(f"Código: {nuevo_curso.codigo}")
                        print(f"Contraseña: {nuevo_curso.contraseña_matriculacion}")

                    elif opcionProfesor == "2":
                        if not profesor.mis_cursos:
                            print("No tienes cursos asignados.")
                        else:
                            print("Cursos disponibles:")
                            for i, curso in enumerate(profesor.mis_cursos, 1):
                                print(f"{i} {curso.nombre}")

                            curso_seleccionado = input("Ingresa el número del curso que deseas ver: ")

                            if curso_seleccionado.isdigit(): #verificar si una cadena de caracteres (string) contiene únicamente dígitos numéricos.
                                curso_seleccionado = int(curso_seleccionado)
                                if 1 <= curso_seleccionado <= len(profesor.mis_cursos):
                                    curso = profesor.mis_cursos[curso_seleccionado - 1]
                                    print(f"Nombre: {curso.nombre}")
                                    print(f"Código: {curso.codigo}")
                                    print(f"Contraseña: {curso.contraseña_matriculacion}")

                                    agregar_archivo = input("¿Deseas agregar un archivo adjunto? (S/N): ")
                                    if agregar_archivo.upper() == "S":
                                        nombre_archivo = input("Ingrese el nombre del archivo: ")
                                        formato_archivo = input("Ingrese el formato del archivo: ")
                                        
                                        fecha_actual = datetime.now()  # Obtener la fecha actual
                                        nuevo_archivo = Archivo(nombre_archivo, fecha_actual, formato_archivo)

                                        curso.nuevo_archivo(nuevo_archivo)
                                        print(f"Cantidad de archivos en el curso: {curso.cantidad_archivos}")


                                        print("Archivo adjunto dado de alta con éxito.")
                                else:
                                    print("Número de curso no válido. Ingresa un número entre 1 y", len(profesor.mis_cursos))
                            else:
                                print("Ingrese un número válido.")

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
    cursos_ordenados = [curso.nombre for curso in mis_cursos]
    cursos_ordenados.sort()
    for curso in cursos_ordenados:
        print(f"Nombre del curso: {curso}")