class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)

    def pop(self, index=-1):
        return self.items.pop(index)

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.items[start:stop]

# Example usage:
my_list = UnsortedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print(my_list.items)  # Output: [1, 2, 3, 4, 5]

print(my_list.index(3))  # Output: 2

print(my_list.pop())  # Output: 5
print(my_list.items)  # Output: [1, 2, 3, 4]

my_list.insert(2, 10)
print(my_list.items)  # Output: [1, 2, 10, 3, 4]

print(my_list.slice(1, 4))  # Output: [2, 10, 3]
