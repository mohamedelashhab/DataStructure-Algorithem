from Queuee import Queue

if __name__ == '__main__':
    queue = Queue(10)
    queue.enqueue(77)
    queue.enqueue(78)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    queue.enqueue(70)




    print(queue.toArray())

