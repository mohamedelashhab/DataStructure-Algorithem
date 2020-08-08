class Stack(object):
    def __init__(self, length):
        self.__items = [0] * length
        self.__size = 0
        self.__top = -1
        self.__length = length

    def push(self, value):
        if self.isFull():
            raise BufferError
        self.__top += 1
        self.__items[self.__top] = value
        self.__size += 1

    def pop(self):
        if self.isEmpty(): raise BufferError
        self.__top -= 1
        self.__size -= 1
        return self.__items[self.__top]

    def isEmpty(self):
        return self.__size == 0

    def peek(self):
        return self.__items[self.__top]

    def toArray(self):
        return self.__items[:self.__top+1]

    def isFull(self):
        return self.__length == self.__size

