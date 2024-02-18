class Student:
    def __init__(self, name, last_name, student_card):
        self.name = name
        self.last_name = last_name
        self.student_card = student_card

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Lista:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.first == None

    def addEnd(self, data):
        if self.isEmpty():
            self.first = self.last = Nodo(data)
        else:
            aux = self.last
            self.last = aux.next = Nodo(data)
            self.last.previous = aux
        self.size += 1

    def addStart(self, data):
        if self.isEmpty():
            self.first = self.last = Nodo(data)
        else:
            aux = Nodo(data)
            aux.next = self.first
            self.first.previous = None
            self.first = aux
        self.size += 1

    def getAll(self):
        aux = self.first
        description = ''
        while aux != None:
            print('Nombre: ' + aux.data.name + ' Apellido: ' + aux.data.last_name + " Carnet: " + aux.data.student_card)
            aux = aux.next
        print(description)
    
    def delete(self):
        if self.isEmpty():
            print('Lista vacía')
        elif self.first.next == None:
            self.first = self.last = None
            self.size = 0
        else:
            self.first = self.first.next
            self.first.previous = None
            self.size -= 1