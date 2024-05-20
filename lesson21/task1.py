import logging

class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        logging.info(f"Opened file: {self.filename} in mode: {self.mode}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        logging.info(f"Closed file: {self.filename}")
        if exc_type is not None:
            logging.error(f"Error: {exc_val}")
        return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    with FileContextManager("test.txt", "w") as f:
        f.write("Hello, world!")
