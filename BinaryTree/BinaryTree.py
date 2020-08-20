class BinaryTree:
    def __init__(self):
        self.__root = None

    def __str__(self):
        return str(self.__root)

    class __Node:
        def __init__(self, value):
            self.right = None
            self.left = None
            self.value = value

        def __str__(self):
            return str(self.value)

    def insert(self, value):
        node = self.__Node(value)
        if self.__root is None:
            self.__root = node
            return

        current = self.__root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

    def find(self, value):
        current = self.__root
        while current != None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else: return True
        return False

    def traversePreOrder(self):
        self.__traversePreOrder(self.__root)

    def __traversePreOrder(self, root):
        if root is None:
            return

        print(root.value)
        self.__traversePreOrder(root.left)
        self.__traversePreOrder(root.right)

    def traverseInOreder(self):
        self.__traverseInOreder(self.__root)

    def __traverseInOreder(self, root):
        if root is None:
            return
        self.__traverseInOreder(root.left)
        print(root.value)
        self.__traverseInOreder(root.right)

    def traversePostOreder(self):
        self.__traversePostOreder(self.__root)

    def __traversePostOreder(self, root):
        if root is None:
            return
        self.__traversePostOreder(root.left)
        self.__traversePostOreder(root.right)
        print(root.value)

    def height(self):
        return self.__height(self.__root)

    def __height(self, root):
        if root is None:
            return -1
        if root.left== None and root.right==None:
            return 0
        return 1 + max(self.__height(root.left), self.__height(root.right))







