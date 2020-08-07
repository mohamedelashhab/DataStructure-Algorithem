from Queue import Queue

if __name__ == '__main__':
    queue = Queue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(60)
    queue.dequeue()
    queue.enqueue(70)




    print(queue.toArray())

