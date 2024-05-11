import os
import sys

current_dir = os.path.dirname(__file__)
head_node_dir = os.path.join(current_dir, '../models')
sys.path.append(head_node_dir)

from head_node import HeadNode

class HeadList:
    def __init__(self, type):
        self.first = None
        self.last = None
        self.type = type
        self.size = 0

    def insert(self, newItem : HeadNode):
        self.size += 1

        if self.first == None:
            self.first = newItem
            self.last = newItem
        else:
            if newItem.item.id < self.first.item.id:
                newItem.next = self.first
                self.first.previous = newItem
                self.first = newItem
            elif newItem.item.id > self.last.item.id:
                self.last.next = newItem
                newItem.previous = self.last
                self.last = newItem
            else:
                tmp = self.first
                while tmp != None:
                    if newItem.item.id < tmp.item.id:
                        newItem.next = tmp
                        newItem.previous = tmp.previous
                        tmp.previous.next = newItem
                        tmp.previous = newItem
                        break
                    elif newItem.item.id > tmp.item.id:
                        tmp = tmp.next
                    else:
                        break
    
    def showHeaders(self):
        tmp = self.first
        while tmp != None:
            print('Cabecera: ', self.type, tmp.item.id)
            tmp = tmp.next
        
    def getHeader(self, id) -> HeadNode:
        tmp = self.first
        while tmp != None:
            if id == tmp.item.id:
                return tmp
            tmp = tmp.next
        return None
