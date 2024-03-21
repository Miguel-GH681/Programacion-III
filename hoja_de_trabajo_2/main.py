import os
import sys
import csv
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'modelos'))

from arbol_binario import ArbolBinario
from covid import Covid
from utilities import Utilities

arbol_binario = ArbolBinario()
utilities = Utilities()
opcion = 0

while(opcion != 5):
    os.system('clear')
    print('---------------------')
    print('|        Menú principal  |')
    print('| 1. Leer documento (ABB) |')
    print('| 2. Buscar dato (ABB)    |')
    print('| 3. Eliminar dato (ABB)  |')
    print('| 1. Leer documento (LS) |')
    print('| 2. Buscar dato (LS)    |')
    print('| 3. Eliminar dato (LS)  |')
    print('| 4. Salir                |')
    print('---------------------------')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        try:
            ruta = input('Seleccione un archivo CSV: ')
            with open(ruta, 'r', newline='') as csvfile:
              lector_csv = csv.DictReader(csvfile)
              init_time = time.time()
              print(init_time)
              for fila in lector_csv:
                  arbol_binario.insert(Covid(fila['Provider Name'], fila['Address1'], fila['Address2'], fila['City'], fila['State'], int(fila['Id']), fila['Last Report Date'], fila['Public Website'], fila['Phone Number'], fila['Geopoint'], fila['Demo']))
              final_time = time.time()
              print(final_time)
            input('Presione enter para continuar\n')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 2:
        try:
            valor = int(input('Ingrese el valor que desea buscar: '))
            arbol_binario.buscar(valor)
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 3:
        try:
            valor = int(input('Ingrese el valor que desea eliminar: '))
            arbol_binario.eliminar(valor)
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 4:
        print('Cerrando programa...')
    else:
        print('Ingrese una opción válida')
        input('Presione enter para continuar')

