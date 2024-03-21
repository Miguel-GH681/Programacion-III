from nodo_lista import NodoLista

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, valor):
        nuevo_nodo = NodoLista(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_primero(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def eliminar_ultimo(self):
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = None
