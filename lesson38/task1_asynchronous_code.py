import asyncio
import math
import time

async def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

async def factorial(n):
    return math.factorial(n)

async def square(n):
    return n * n

async def cubic(n):
    return n * n * n

async def main_async():
    numbers = range(1, 11)
    fib_tasks = [fibonacci(n) for n in numbers]
    fact_tasks = [factorial(n) for n in numbers]
    square_tasks = [square(n) for n in numbers]
    cubic_tasks = [cubic(n) for n in numbers]

    fib_results = await asyncio.gather(*fib_tasks)
    fact_results = await asyncio.gather(*fact_tasks)
    square_results = await asyncio.gather(*square_tasks)
    cubic_results = await asyncio.gather(*cubic_tasks)

    return fib_results, fact_results, square_results, cubic_results

if __name__ == "__main__":
    start_time = time.time()
    fib_results, fact_results, square_results, cubic_results = asyncio.run(main_async())
    end_time = time.time()
    print(f"Async execution time: {end_time - start_time} seconds")
    print(f"Fibonacci: {fib_results}")
    print(f"Factorials: {fact_results}")
    print(f"Squares: {square_results}")
    print(f"Cubics: {cubic_results}")
