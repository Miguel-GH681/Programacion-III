class CellNode:
    def __init__(self, x, y, type):
        self.x_coordinate = x
        self.y_coordinate = y
        self.type = type
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def setUp(self, up):
        self.up = up
    
    def getUp(self):
        return self.up

    def setDown(self, down):
        self.down = down
    
    def getDown(self):
        return self.down
    
    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left
    
    def setRight(self, right):
        self.right = right

    def getRight(self):
        return self.right