class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, value):
        if self.leftChild is None:
            self.leftChild = BinaryTree(value)
        else:
            node = BinaryTree(value)
            node.leftChild = self.leftChild
            self.leftChild = node

    def insertRight(self, value):
        if self.rightChild is None:
            self.rightChild = BinaryTree(value)
        else:
            node = BinaryTree(value)
            node.rightChild = self.rightChild
            self.rightChild = node

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())






