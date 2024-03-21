import os
import graphviz
import pickle

from arbol import Arbol

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        self.raiz = self._insert(self.raiz, valor)

    def _insert(self, nodo, valor):
        if nodo is None:
            return Arbol(valor)

        if valor.Id < nodo.valor.Id:
            nodo.izq = self._insert(nodo.izq, valor)

        elif valor.Id > nodo.valor.Id:
            nodo.der = self._insert(nodo.der, valor)

        return nodo

    def buscar(self, valor):
        self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if nodo is None:
            print("No encontrado")
            return Nodo(-1)
        if nodo.valor.Id == valor:
            print('El valor encontrado es: ', nodo.valor.Address1)
            return nodo
        if(valor < nodo.valor.Id):
            return self._buscar(valor, nodo.izq)
        else:
            return self._buscar(valor, nodo.der)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor.Id:
            nodo.izq = self._eliminar(nodo.izq, valor)
        elif valor > nodo.valor.Id:
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




