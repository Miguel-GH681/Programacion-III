import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'controllers'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

from sparse_matrix import SparseMatrix
from my_model import MyModel

def main():
    #Crear una instancia de la matriz
    matrizEjemplo = SparseMatrix()


    matrizEjemplo.insert(MyModel(0, 'Transitable') ,MyModel(0, 'Transitable'), 'Transitable')
    matrizEjemplo.insert(MyModel(1, 'Restaurante') ,MyModel(1, 'Restaurante'),'Restaurante')
    matrizEjemplo.insert(MyModel(2, 'UnidadCivil') ,MyModel(2, 'UnidadCivil'),'UnidadCivil')
    matrizEjemplo.insert(MyModel(2, 'UnidadCivil') ,MyModel(0, 'UnidadCivil'),'UnidadCivil')
    matrizEjemplo.insert(MyModel(0, 'UnidadCivil') ,MyModel(2, 'UnidadCivil'),'UnidadCivil')


    # matrizEjemplo.insert(MyModel(2, 'UnidadCivil') ,MyModel(0, 'UnidadCivil'),'UnidadCivil')

    matrizEjemplo.insert(MyModel(0, 'Entrada') ,MyModel(1, 'Transitable'), 'Transitable')
    # matrizEjemplo.insert(3,3,{'id':1, 'tipo': 'UnidadCivil'})
    # matrizEjemplo.insert(3,1,{'id':8, 'tipo': 'Intransitable'})
    # matrizEjemplo.insert(4,4,{'id':5, 'tipo': 'Intransitable'})

    # Nombre para el archivo de salida de la gráfica
    nombre_grafica = 'matriz_ejemplo'

    # Generar la gráfica de la matriz dispersa
    matrizEjemplo.getGraph(nombre_grafica)

    #Mensaje de confirmación
    print(f"Matriz dispersa generada en {nombre_grafica}.png")




if __name__ == "__main__":
    main()
