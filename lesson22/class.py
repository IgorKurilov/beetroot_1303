import logging

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type is not None:
            if issubclass(exc_type, IndexError):
                logging.error(f'Error occurred: {exc_value}')
                return True  # Помилка оброблена
            else:
                return False  # Передаємо інші типи помилок далі

# Приклад використання класу-менеджера контексту
with FileManager('example.txt') as file:
    file.write('Hello, World!')
    # Виклик помилки IndexError
    data = [1, 2, 3]
    print(data[4])
