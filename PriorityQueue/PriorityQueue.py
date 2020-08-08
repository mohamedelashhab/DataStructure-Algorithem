class PriorityQueue(object):
    def __init__(self, length):
        self.__items = [0] * length
        self.__size = 0
        self.__length = length

    def enqueue(self, item):
        if (self.isEmpty()):
            self.__items[0] = item
            self.__size += 1
            return

        i = self.ShiftItemsToInsert(item)
        self.__items[i] = item
        self.__size += 1



    def ShiftItemsToInsert(self, item):
        if self.isFull(): raise BufferError
        i = self.__size-1
        for i in range(i,-1,-1):
            if (item < self.__items[i]):
                self.__items[i + 1] = self.__items[i]
            else:
                break
            i = i - 1
        return i + 1

    def dequeue(self):
        if(self.isEmpty()):
            raise BufferError
        item = self.shiftToLeft()
        self.__size -= 1
        return item

    def shiftToLeft(self):
        item = self.__items[0]
        for i in range(1, self.__size, 1):
            self.__items[i-1] = self.__items[i]
        self.__items[self.__size - 1] = 0
        return item

    def peek(self):
        if self.isEmpty(): raise BufferError
        return self.__items[0]

    def toArray(self):
        return self.__items[0:self.__size]

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__length == self.__size
