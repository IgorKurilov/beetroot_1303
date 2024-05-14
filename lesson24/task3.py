class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_from_stack(self, e):
        temp_stack = Stack()
        found = False
        while not self.is_empty():
            item = self.pop()
            if item == e:
                found = True
                break
            temp_stack.push(item)
        
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return e
        else:
            raise ValueError(f"{e} not found in the stack")


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_from_queue(self, e):
        if e in self.items:
            idx = self.items.index(e)
            return self.items.pop(idx)
        else:
            raise ValueError(f"{e} not found in the queue")


if __name__ == "__main__":
    # Example usage of Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.get_from_stack(2))  # Output: 2
    print(stack.items)  # Output: [3, 1]

    # Example usage of Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.get_from_queue(2))  # Output: 2
    print(queue.items)  # Output: [1, 3]
