import os
import time
import csv
from random import*

def limpiar():
    os.system('cls')

acceso=1
trabajadores=[["Juan peréz"], ["María garcía"], ["Carlos peréz"], ["Ana Martínez"], ["Pedro Rodríguez"], ["Laura Hernández"], ["Miguel Sánchez"], ["Isabel Gómez"], ["Francisco Díaz"], ["Elena Fernández"]]

def menuprincipal():
    print('''
        1. Asignar sueldo aleatorios
        2. Clasificar sueldo
        3. Ver estadisticas.
        4. Reporte de sueldos
        5. Salir del programa''')
    while acceso==1:
        try:
            opc=int(input("Seleccione una opción del 1 al 5: "))
        except ValueError:
            print('Opción ingresada no válida, ingrese nuevamente.')
            continue
        if opc==1:
            limpiar()
            asignarsueldos()
            seguir()
        elif opc==2:
            limpiar()
            clasificarsueldos()
            seguir()
        elif opc==3:
            limpiar()
            verestadisticas()
            seguir()
        elif opc==4:
            limpiar()
            reportesueldos()
            seguir()
        elif opc==5:
            print('Finalizando el programa... Desarrollado por José Castillo Rut 21.914.890-9')
            quit()
        else:
            print('adiós')

def seguir():
        access=1
        while access==1:
            try:
                sino=int(input('''
                        Desea volver al menu?
                        1. sí 
                        2. no
                        Seleccione una opción: '''))
            except ValueError:
                print('Opción incorrecta, vuelva a intentarlo.')
            break
        if sino==1:
            menuprincipal()
        elif sino==2:
            print('adiós')
            quit()

def asignarsueldos():
    print('Sueldos de los trabajadores: ')
    sueldos=randint(300000, 2500000)
    for fila in trabajadores:
        print(sueldos,trabajadores)

def clasificarsueldos():
    with open('archivoexamen2.csv', '', newline='') as archivoexamen_csv:
        print

def verestadisticas():
    print('3')  

def reportesueldos():
    sueldobase=2000000
    descuentosalud=(sueldobase*0,7)
    descuentoafp=(sueldobase*0,12)
    sueldoliquido=(sueldobase and descuentosalud and descuentoafp)
    print(f'Sueldo: {sueldobase}, {descuentosalud}, {descuentoafp}, {sueldoliquido}')
menuprincipal()