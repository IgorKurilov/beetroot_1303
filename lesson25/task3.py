class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            removed = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # Output: 1 -> 2 -> 3 -> None

print("Dequeued:", queue.dequeue())  # Output: Dequeued: 1
queue.display()  # Output: 2 -> 3 -> None

print("Peek:", queue.peek())  # Output: Peek: 2
