class LinkedList:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    class __Node:
        def __init__(self, value:int):
            self.__value = value
            self.__next = None

    def addLast(self, item: int):
        node = self.__Node(item)
        if self.__isEmpty():
            self.__first = self.__last = node
        else:
            self.__last._Node__next = node
            self.__last = node
        self.__size+=1

    def addFirst(self, item: int):
        node = self.__Node(item)
        if self.__isEmpty():
            self.__first = self.__last = node
        else:
            node._Node__next = self.__first
            self.__first = node
        self.__size += 1

    def indexOf(self, item):
        index = 0
        current = self.__first
        while (current != None):
            print(current._Node__value)

            if current._Node__value == item:
                return index
            else:
                index += 1
                current = current._Node__next
        return -1

    def contains(self, item: int):
        return  self.indexOf(item) != -1

    def removeFirst(self):
        if self.__isEmpty():
            raise BufferError


        if self.__first == self.__last:
            self.__first = self.__last = None
        else:
            second = self.__first._Node__next
            self.__first._Node__next = None
            self.__first = second

        self.__size -= 1

    def removeLast(self):
        if self.__isEmpty():
            raise BufferError

        if self.__first == self.__last:
            self.__first = self.__last = None
        else:
            previous = self.getPrevious(self.__last)
            self.__last = previous
            self.__last._Node__next = None
        self.__size -= 1



    def getPrevious(self, node):
        current = self.__first
        while (current != None):
            if current._Node__next == node: return current
            current = current._Node__next
        return None

    def toArray(self):
        arr = []
        current = self.__first
        while current != None:
            arr.append(current._Node__value)
            current = current._Node__next
        return arr

    # [10 <- 20 -> 30 -> 40 -> 50 ]
    #        p    c     n
    def reverse(self):
        current = self.__first._Node__next
        previous = self.__first
        while current != None:
            next = current._Node__next
            current._Node__next = previous
            previous = current
            current = next

        temp = self.__first
        self.__first = self.__last
        self.__last = temp
        self.__last._Node__next = None








    def __isEmpty(self):
        return self.__first is None

    def size(self):
        return self.__size


