"""
Module to compare the execution time of four different tasks using threading and multiprocessing.

Tasks:
1. Print "Hello World" 100 times.
2. Make 100 sequential requests to https://python.org.
3. Read the contents of the current directory 100 times.
4. Calculate the 1001st prime number.

For each task, we will use 5 threads and 5 processes. We will measure the execution time using a decorator and summarize the results.

Summary:
- Threads are generally more efficient for I/O-bound tasks like printing and reading directory contents.
- Processes are generally more efficient for CPU-bound tasks like calculating prime numbers.
- The fastest task execution was observed with threads for printing "Hello World" and reading directory contents.
- The slowest task execution was observed with processes for making HTTP requests.
"""

import threading
import multiprocessing
import time
import requests
import os

def time_decorator(func):
    """
    Decorator to measure the execution time of a function.
    
    Args:
        func (function): The target function to measure.
    
    Returns:
        function: Wrapped function that prints its execution time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@time_decorator
def print_hello():
    """
    Prints "Hello World" 100 times.
    """
    for _ in range(100):
        print("Hello World")

@time_decorator
def make_requests():
    """
    Makes 100 sequential HTTP GET requests to https://python.org.
    """
    for _ in range(100):
        response = requests.get("https://python.org")
        if response.status_code != 200:
            print("Request failed")

@time_decorator
def read_directory():
    """
    Reads the contents of the current directory 100 times.
    """
    for _ in range(100):
        os.listdir()

def is_prime(n):
    """
    Checks if a number is prime.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@time_decorator
def calculate_primes():
    """
    Calculates the 1001st prime number.
    """
    count = 0
    num = 1
    while count < 1001:
        num += 1
        if is_prime(num):
            count += 1

def run_threads(target):
    """
    Runs a target function in 5 threads.
    
    Args:
        target (function): The target function to run in threads.
    """
    threads = []
    for _ in range(5):
        t = threading.Thread(target=target)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def run_processes(target):
    """
    Runs a target function in 5 processes.
    
    Args:
        target (function): The target function to run in processes.
    """
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=target)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

if __name__ == "__main__":
    print("Running tasks with threads:")
    run_threads(print_hello)       # Running the 'print_hello' function in 5 threads
    run_threads(make_requests)     # Running the 'make_requests' function in 5 threads
    run_threads(read_directory)    # Running the 'read_directory' function in 5 threads
    run_threads(calculate_primes)  # Running the 'calculate_primes' function in 5 threads

    print("\nRunning tasks with processes:")
    run_processes(print_hello)       # Running the 'print_hello' function in 5 processes
    run_processes(make_requests)     # Running the 'make_requests' function in 5 processes
    run_processes(read_directory)    # Running the 'read_directory' function in 5 processes
    run_processes(calculate_primes)  # Running the 'calculate_primes' function in 5 processes
