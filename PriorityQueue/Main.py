from PriorityQueue import PriorityQueue

if __name__ == '__main__':
    pq = PriorityQueue(3)
    pq.enqueue(50)
    pq.enqueue(20)
    pq.enqueue(40)
    pq.enqueue(30)
    pq.enqueue(10)
    pq.enqueue(-1)
    pq.dequeue()
    pq.dequeue()








    print(pq.toArray());