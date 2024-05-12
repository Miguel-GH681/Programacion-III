import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'controllers'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

from sparse_matrix import SparseMatrix
from my_model import MyModel

def main():
    sparseMatrix = SparseMatrix()

    option = 0

    while option != 4:
        os.system('clear')
        print('---------------------')
        print('|    Menú principal  |')
        print('| 1. Carga inicial   |')
        print('| 2. Insertar dato   |')
        print('| 3. Generar grafico |')
        print('| 4. Salir           |')
        print('---------------------')
        option = int(input('Ingrese una opción: '))
        
        if option == 1:
            try:
                myPath = os.path.join(os.getcwd(), 'db', 'data.csv')
                with open(myPath, 'r') as myFile:
                    for i, line in enumerate(myFile):
                        myArray = [float(x) for x in line.split(',')]
                        for j, cell in enumerate(myArray):
                            if(cell != 0):
                                sparseMatrix.insert(MyModel(i) ,MyModel(j), cell)
                input('Presione enter para continuar\n')
            except:
                print('Ha ocurrido un error, inténtelo nuevamente')
                input('Presione enter para continuar')
        elif option == 2:
            try:
                columna = int(input('Ingrese el numero de columna: '))
                fila = int(input('Ingrese el numero de fila: '))
                value = int(input('Ingrese el valor que desea almacenar: '))
                sparseMatrix.insert(MyModel(fila), MyModel(columna), value)
                input('Presione enter para continuar\n')
            except:
                print('Ha ocurrido un error, inténtelo nuevamente')
                input('Presione enter para continuar')
        elif option == 3:
            print('Generando grafico...')
            nombre_grafica = 'matriz_ejemplo'
            sparseMatrix.getGraph(nombre_grafica)
            sparseMatrix.open_graph('matriz_matriz_ejemplo.png')
            input('Presione enter para continuar')
        elif option == 4:
            print('Cerrando programa...')
        else:
            print('Ingrese una opción válida')
            input('Presione enter para continuar')

if __name__ == "__main__":
    main()
