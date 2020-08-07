class Queue(object):
    def __init__(self, length):
        self.__items = [0] * length
        self.__front = 0
        self.__rear =  0
        self.__size =  0
        self.__length = length

    def enqueue(self, value):
        if self.__size >= self.__length:
            raise OverflowError

        self.__items[self.__rear] = value
        self.__rear = (self.__rear + 1) % self.__length
        self.__size += 1


    def dequeue(self):
        if self.isEmpty(): raise ValueError

        self.__items[self.__front] = 0
        self.__front = (self.__front + 1) % self.__length
        self.__size -= 1


    def isEmpty(self):
        return self.__size == 0

    def size(self):
        return self.__size

    def peek(self):
        return self.__items[self.__rear]

    def toArray(self):
        return self.__items
