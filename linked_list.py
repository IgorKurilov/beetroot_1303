class Node:

    def __init__(self, _id, value):
        self.id = _id
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node {self.id}: value {self.value}"

class LinkedList:

    def __init__(self):
        self.head = None

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current:
            current = self._current
            self._current = self._current.next
            return current
        else:
            raise StopIteration

    def add_node(self, value):
        _id = len(self) + 1
        if not self.head:
            self.head = Node(_id, value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(_id, value)

    def print_nodes(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def find_node_by_id(self, target_id):
        current = self.head
        while current:
            if current.id == target_id:
                return current
            current = current.next
        return None

    def remove_last_node(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_node_by_value(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

if __name__ == "__main__":
    container = LinkedList()
    container.add_node(10)
    container.add_node(20)
    container.add_node(30)
    print(len(container))
    container.print_nodes()

    # Test find_node_by_id
    print(container.find_node_by_id(2))  # Should print: Node 2: value 20

    # Test remove_last_node
    container.remove_last_node()
    print(len(container))  # Should print: 2

    # Test remove_node_by_value
    container.remove_node_by_value(20)
    container.print_nodes()  # Should print: Node 1: value 10

    for node in container:
        print(node)
