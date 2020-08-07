from Stack import Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.pop()
    stack.peak()
    print(stack.toArray())
    stack.pop()
    stack.pop()

    print(stack.toArray())