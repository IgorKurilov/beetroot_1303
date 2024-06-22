import math
import time
from multiprocessing import Pool

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial(n):
    return math.factorial(n)

def square(n):
    return n * n

def cubic(n):
    return n * n * n

def main_multiprocessing():
    numbers = range(1, 11)
    with Pool() as pool:
        fib_results = pool.map(fibonacci, numbers)
        fact_results = pool.map(factorial, numbers)
        square_results = pool.map(square, numbers)
        cubic_results = pool.map(cubic, numbers)

    return fib_results, fact_results, square_results, cubic_results

if __name__ == "__main__":
    start_time = time.time()
    fib_results, fact_results, square_results, cubic_results = main_multiprocessing()
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time} seconds")
    print(f"Fibonacci: {fib_results}")
    print(f"Factorials: {fact_results}")
    print(f"Squares: {square_results}")
    print(f"Cubics: {cubic_results}")
