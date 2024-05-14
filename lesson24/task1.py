class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_sequence(sequence):
    stack = Stack()
    for char in sequence:
        stack.push(char)

    reversed_sequence = ""
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    return reversed_sequence


if __name__ == "__main__":
    sequence = input("Enter a sequence of characters: ")
    reversed_sequence = reverse_sequence(sequence)
    print("Reversed sequence:", reversed_sequence)
