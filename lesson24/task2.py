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


def is_balanced(sequence):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in sequence:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if opening_brackets.index(top_char) != closing_brackets.index(char):
                return False
    return stack.is_empty()


if __name__ == "__main__":
    sequence = input("Enter a sequence of characters: ")
    if is_balanced(sequence):
        print("The parentheses, braces, and curly brackets are balanced.")
    else:
        print("The parentheses, braces, and curly brackets are not balanced.")
