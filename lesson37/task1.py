import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(n):
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

def filter_primes_threadpool(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, is_prime in zip(numbers, results) if is_prime]

def filter_primes_processpool(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, is_prime in zip(numbers, results) if is_prime]

if __name__ == "__main__":
    # Using ThreadPoolExecutor
    start_time = time.time()
    prime_numbers_threadpool = filter_primes_threadpool(NUMBERS)
    end_time = time.time()
    print(f"ThreadPoolExecutor found primes: {prime_numbers_threadpool} in {end_time - start_time} seconds")

    # Using ProcessPoolExecutor
    start_time = time.time()
    prime_numbers_processpool = filter_primes_processpool(NUMBERS)
    end_time = time.time()
    print(f"ProcessPoolExecutor found primes: {prime_numbers_processpool} in {end_time - start_time} seconds")
