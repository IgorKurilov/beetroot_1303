import threading

# Global variables
counter = 0
rounds = 100000
lock = threading.Lock()

class Counter(threading.Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            with lock:
                counter += 1

# Create and start threads
thread1 = Counter()
thread2 = Counter()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Check the result of the counter
print("Final counter value:", counter)
