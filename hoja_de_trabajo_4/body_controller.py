from arbol_model import ArbolModel

class BodyController:
    def __init__(self):
        self.root = None

    def insert_body(self, value):
        self.root = self._insert_body(self.root, value)

    def _insert_body(self, root, value):
        if root is None:
            return ArbolModel(value)
        elif value.bodyId < root.value.bodyId:
            root.left = self._insert_body(root.left, value)
        elif value.bodyId > root.value.bodyId:
            root.right = self._insert_body(root.right, value)
        return root

    def get_body(self, value):
        return self._get_body(self.root, value)

    def _get_body(self, root, value):
        if root is None:
            return None
        elif value == root.value.bodyId:
            return root.value
        elif value < root.value.bodyId:
            return self._get_body(root.left, value)
        elif value > root.value.bodyId:
            return self._get_body(root.right, value)

    def inorden(self):
        self._inorden(self.root)
        print('')

    def _inorden(self, nodo):
        if nodo != None:
            self._inorden(nodo.left)
            print(nodo.value.englishName, end="-")
            self._inorden(nodo.right)
