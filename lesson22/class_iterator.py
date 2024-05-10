import logging

class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            if issubclass(exc_type, IndexError):
                logging.error(f'Error occurred: {exc_value}')
                return True  # Помилка оброблена
            else:
                return False  # Передаємо інші типи помилок далі

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line[:10]
        else:
            raise StopIteration

# Приклад використання класу FileReader
with FileReader('example.txt') as reader:
    for line in reader:
        print(line)
