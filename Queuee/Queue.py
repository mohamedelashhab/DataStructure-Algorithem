class Queue(object):
    def __init__(self, length):
        self.__items = [0] * length
        self.__front = 0
        self.__rear =  0
        self.__size =  0
        self.__length = length

    def enqueue(self, value):
        if self.isFull():raise BufferError
        self.__items[self.__rear] = value
        self.__rear = (self.__rear + 1) % self.__length
        self.__size += 1


    def dequeue(self):
        if self.isEmpty(): raise BufferError

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
        items = []
        while self.__front != self.__rear:
            items.append(self.__items[self.__front])
            self.__front = (self.__front + 1) % self.__length
        return items

    def isFull(self):
        return self.__length == self.__size
