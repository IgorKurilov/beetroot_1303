# Реалізація __contains__ та __len__ методів для HashTable
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = []
        self.table[index].append((key, value))

    def __contains__(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return True
        return False

    def __len__(self):
        count = 0
        for bucket in self.table:
            if bucket:
                count += len(bucket)
        return count

# Приклад використання
ht = HashTable(10)
ht.insert("key1", "value1")
ht.insert("key2", "value2")

print("key1" in ht)  # Output: True
print("key3" in ht)  # Output: False
print(len(ht))       # Output: 2
