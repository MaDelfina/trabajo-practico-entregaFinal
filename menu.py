from funciones import *

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