class Stack(object):
    def __init__(self):
        self.__items = []
        self.__size = 0
        self.__top = -1

    def push(self, value):
        self.__items.append(value)
        self.__top += 1
        self.__size += 1

    def pop(self):
        if self.isEmpty(): return None
        self.__top -= 1
        self.__size -= 1
        return self.__items[self.__top]

    def isEmpty(self):
        return self.__size == 0

    def peak(self):
        return self.__items[self.__top]

    def toArray(self):
        return self.__items[:self.__top+1]

