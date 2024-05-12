
# Tarea 4 - Matriz dispersa
Una matriz dispersa es una matriz de gran tamaño en la cual la mayoria de sus elementos son cero, esto ayuda a reducir de manera significativa la cantidad de memoria que se necesita para almacenar datos.

En esta tarea se construyo una matriz dispersa utilzando listas doblemente enlazadas.

## Estructura
La estructura del proyecto es la siguiente:
```
|-controllers/
|           |-head_list.py
|           |-sparse_matrix.py
|-models/
|        |-cell_node.py
|        |-head_node.py   
|        |-my_model.py
|-db/
|   |-data.csv
|-main.py
|-matriz_matriz_ejemplo.png
```

## Clases
A continuacion se realiza una breve descripcion de la funcionalidad de cada una de las clases que componen el proyecto.
#### CellNode
```
class CellNode:
    def __init__(self, x, y, type):
        self.x_coordinate = x
        self.y_coordinate = y
        self.type = type
        self.up = None
        self.down = None
        self.left = None
        self.right = None
```
Esta clase representa a un nodo dentro de la matriz y es la encargada de mantener los apuntadores hacia los nodos que se encuentran a la izquierda, derecha, arriba y/o abajo del nodo. Tambien contiene las coordenadas actuales del nodo.

#### HeadNode
```
class HeadNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None
        self.access = None
```
Esta clase representa a un nodo dentro de la lista doblemente enlazada.

### HeadList
```
class HeadList:
    def __init__(self, type):
        self.first = None
        self.last = None
        self.type = type
        self.size = 0
```
Esta clase tiene la funcion de controlador, es la encargada de agregar nodos a la lista doblemente enlazada.

### SparseMatrix
```
class SparseMatrix:
    def __init__(self):
        self.layer = 0
        self.rows = HeadList('fila')
        self.columns = HeadList('columna')
```
Esta clase es la encargada de unificar todas las listas a fin de generar una matriz, por medio de esta clase se realizan las inserciones de nodos a la matriz.
## Ejecucion

Cuando se haya clonado el repositorio por favor colocar los siguientes comandos en una terminal

```bash
  cd Programacion-III
  cd tarea_4
```

Cuando se encuentre dentro de la carpeta adecuada ejecute el siguiente comando en una terminal

```bash
  python3 main.py
```
    
## Autores

- Alvaro Miguel Gonzalez Hic - 9490224805 - 100%
- Walter Daniel Palacios De León - 9490212140 - 100%

