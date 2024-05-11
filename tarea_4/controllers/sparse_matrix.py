import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'controllers'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

from head_list import HeadList
from cell_node import CellNode
from head_node import HeadNode
from my_model import MyModel

class SparseMatrix:
    def __init__(self):
        self.layer = 0
        self.rows = HeadList('fila')
        self.columns = HeadList('columna')

    def insert(self, pos_x : MyModel, pos_y : MyModel, type):
        new_cell = CellNode(pos_x, pos_y, type)
        node_X = self.rows.getHeader(pos_x.id)
        node_Y = self.columns.getHeader(pos_y.id)
        
        if node_X == None:
            node_X = HeadNode(pos_x)
            self.rows.insert(node_X)
        
        if node_Y == None:
            node_Y = HeadNode(pos_y)
            self.columns.insert(node_Y)

        
        if node_X.getAccess() == None:
            node_X.setAccess(new_cell)
        else:
            if new_cell.y_coordinate.id < node_X.getAccess().y_coordinate.id:
                new_cell.setRight(node_X.getAccess())
                node_X.getAccess().setLeft(new_cell)
                node_X.setAccess(new_cell)
            else:
                tmp : CellNode = node_X.getAccess()
                while tmp != None:
                    if new_cell.y_coordinate.id < tmp.y_coordinate.id:
                        new_cell.setRight(tmp)
                        new_cell.setLeft(tmp.getLeft())
                        tmp.getLeft().setRight(new_cell)
                        tmp.setLeft(new_cell)
                        break
                    elif new_cell.x_coordinate.id == tmp.x_coordinate.id and new_cell.y_coordinate.id == tmp.y_coordinate.id:
                        break
                    else:
                        if tmp.getRight() == None:
                            tmp.setRight(new_cell)
                            new_cell.setLeft(tmp)
                            break
                        else:
                            tmp = tmp.getRight()

        if node_Y.getAccess() == None:
            node_Y.setAccess(new_cell)
        else:
            if new_cell.x_coordinate.id < node_Y.getAccess().x_coordinate.id:
                new_cell.setDown(node_Y.getAccess())
                node_Y.getAccess().setUp(new_cell)
                node_Y.setAccess(new_cell)
            else:
                tmp2 : CellNode = node_Y.getAccess()
                while tmp2 != None:
                    if new_cell.x_coordinate.id < tmp2.x_coordinate.id:
                        new_cell.setDown(tmp2)
                        new_cell.setUp(tmp2.getUp())
                        tmp2.getUp().setDown(new_cell)
                        tmp2.setUp(new_cell)
                        break
                    elif new_cell.x_coordinate.id == tmp2.x_coordinate.id and new_cell.y_coordinate.id == tmp2.y_coordinate.id:
                        break
                    else:
                        if tmp2.getDown() == None:
                            tmp2.setDown(new_cell)
                            new_cell.setUp(tmp2)
                            break
                        else:
                            tmp2 = tmp2.getDown()


    def getGraph(self, name):
            content = '''digraph G{
        node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
        edge[style = "bold"]
        node[label = "capa:''' + str(self.layer) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
            content += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                        \n'''.format('\n'+name)

            pivot : HeadNode = self.rows.first
            posx = 0
            while pivot != None:
                content += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivot.item.id, 
                posx, pivot.item.id)
                pivot = pivot.next
                posx += 1
            pivot = self.rows.first
            while pivot.next != None:
                content += '\n\tx{}->x{};'.format(pivot.item.id, pivot.next.item.id)
                content += '\n\tx{}->x{}[dir=back];'.format(pivot.item.id, pivot.next.item.id)
                pivot = pivot.next
            content += '\n\traiz->x{};'.format(self.rows.first.item.id)

            # --graficar nodos columna
            pivoty : HeadNode = self.columns.first
            posy = 0
            while pivoty != None:
                content += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivoty.item.id, 
                posy, pivoty.item.id)
                pivoty = pivoty.next
                posy += 1
            pivoty = self.columns.first
            while pivoty.next != None:
                content += '\n\ty{}->y{};'.format(pivoty.item.id, pivoty.next.item.id)
                content += '\n\ty{}->y{}[dir=back];'.format(pivoty.item.id, pivoty.next.item.id)
                pivoty = pivoty.next
            content += '\n\traiz->y{};'.format(self.columns.first.item.id)

            #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
            pivot : CellNode = self.rows.first
            posx = 0
            while pivot != None:
                pivote_celda : HeadNode = pivot.access
                while pivote_celda != None:
                    # --- buscamos posy
                    pivoty = self.columns.first
                    posy_celda = 0
                    while pivoty != None:
                        if pivoty.item.id == pivote_celda.y_coordinate.id: break
                        posy_celda += 1
                        pivoty = pivoty.next
                    if pivote_celda.type == 'Intransitable':
                        content += '\n\tnode[label="Intransitable" fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                            posy_celda, posx, pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id
                        )
                    elif pivote_celda.type == 'Transitable':
                        content += '\n\tnode[label="Transitable" fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                            posy_celda, posx, pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id
                        )
                    elif pivote_celda.type == 'Entrada':
                        content += '\n\tnode[label="Entrada" fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                            posy_celda, posx, pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id
                        )
                    elif pivote_celda.type == 'UnidadCivil':
                        content += '\n\tnode[label="Unidad Civil" fillcolor="blue" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                            posy_celda, posx, pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id
                        )
                    elif pivote_celda.type == 'Restaurante':
                        content += '\n\tnode[label="Restaurante" fillcolor="lightgrey" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                            posy_celda, posx, pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id
                        )
                    else:
                        content += '\n\tnode[label="U" fillcolor="pink" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                            posy_celda, posx, pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id
                        ) 
                    pivote_celda = pivote_celda.right
                
                pivote_celda = pivot.access
                while pivote_celda != None:
                    if pivote_celda.right != None:
                        content += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id,
                        pivote_celda.right.x_coordinate.id, pivote_celda.right.y_coordinate.id)
                        content += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id,
                        pivote_celda.right.x_coordinate.id, pivote_celda.right.y_coordinate.id)
                    pivote_celda = pivote_celda.right
            
                content += '\n\tx{}->i{}_{};'.format(pivot.item.id, pivot.access.x_coordinate.id, pivot.access.y_coordinate.id)
                content += '\n\tx{}->i{}_{}[dir=back];'.format(pivot.item.id, pivot.access.x_coordinate.id, pivot.access.y_coordinate.id)
                pivot = pivot.next
                posx += 1
            
            pivot = self.columns.first
            while pivot != None:
                pivote_celda : CellNode = pivot.access
                while pivote_celda != None:
                    if pivote_celda.down != None:
                        content += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id,
                        pivote_celda.down.x_coordinate.id, pivote_celda.down.y_coordinate.id)
                        content += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.x_coordinate.id, pivote_celda.y_coordinate.id,
                        pivote_celda.down.x_coordinate.id, pivote_celda.down.y_coordinate.id) 
                    pivote_celda = pivote_celda.down
                content += '\n\ty{}->i{}_{};'.format(pivot.item.id, pivot.access.x_coordinate.id, pivot.access.y_coordinate.id)
                content += '\n\ty{}->i{}_{}[dir=back];'.format(pivot.item.id, pivot.access.x_coordinate.id, pivot.access.y_coordinate.id)
                pivot = pivot.next
                    
            content += '\n}'
            #--- se genera DOT y se procede a ecjetuar el comando
            dot = "matriz_{}_dot.txt".format(name)
            with open(dot, 'w') as grafo:
                grafo.write(content)
            result = "matriz_{}.png".format(name)
            os.system("neato -Tpng " + dot + " -o " + result)