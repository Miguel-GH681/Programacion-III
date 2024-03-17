import os
import graphviz

from PIL import Image
from nodo import Nodo

class ArbolBinario:

    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        self.raiz = self._insert(valor, self.raiz)

    def _insert(self, valor, nodo):
        if nodo is None:
            return Nodo(valor)

        if(valor < nodo.valor):
            nodo.izq = self._insert(valor, nodo.izq)
        elif(valor > nodo.valor):
            nodo.der = self._insert(valor, nodo.der)
        return nodo

    def inorden(self):
        self._inorden(self.raiz)
        print('')
    
    def _inorden(self, nodo):
        if nodo != None:
            self._inorden(nodo.izq)
            print(nodo.valor, end="-")
            self._inorden(nodo.der)

    def buscar(self, valor):
        self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if nodo is None:
            print("No encontrado")
            return Nodo(-1)
        if nodo.valor == valor:
            print('El valor encontrado es: ', nodo.valor)
            return nodo
        if(valor < nodo.valor):
            return self._buscar(valor, nodo.izq)
        else:
            return self._buscar(valor, nodo.der)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self._eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar(nodo.der, valor)
        else:
            if nodo.izq is None:
                temp = nodo.der
                nodo = None
                return temp
            elif nodo.der is None:
                temp = nodo.izq
                nodo = None
                return temp
            
            temp = self._valor_minimo(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self._eliminar(nodo.der, temp.valor)
        return nodo

    def _valor_minimo(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def generar_arbol_grafico(self):
        dot = graphviz.Digraph()
        self._generar_arbol_grafico(self.raiz, dot)

        archivo_salida = "arbol.dot"
        dot.render(archivo_salida, format='png', cleanup=True)

    def _generar_arbol_grafico(self, nodo, dot):
        if nodo is not None:
            dot.node(str(nodo.valor))
            if nodo.izq is not None:
                dot.edge(str(nodo.valor), str(nodo.izq.valor))
                self._generar_arbol_grafico(nodo.izq, dot)
            if nodo.der is not None:
                dot.edge(str(nodo.valor), str(nodo.der.valor))
                self._generar_arbol_grafico(nodo.der, dot)

    def abrir_imagen(self, ruta):
        ruta_absoluta = os.path.join(os.getcwd(), ruta)
        imagen = Image.open(ruta_absoluta)
        imagen.show()
