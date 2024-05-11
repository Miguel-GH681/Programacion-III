class HeadNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None
        self.access = None

    def getAccess(self):
        return self.access

    def setAccess(self, new_access):
        self.access = new_access
